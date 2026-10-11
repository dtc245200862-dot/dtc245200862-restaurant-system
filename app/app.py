import os
import time
import logging
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash
import psycopg2
from psycopg2.extras import RealDictCursor
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from pythonjsonlogger import jsonlogger

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'ictu-restaurant-secure-key-2026-dtc245200862')

# Structured JSON Logging
log_handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter(
    fmt='%(asctime)s %(levelname)s %(name)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
log_handler.setFormatter(formatter)
logger = logging.getLogger("restaurant-app")
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)
logger.propagate = False

# Prometheus Metrics
HTTP_REQUESTS_TOTAL = Counter(
    'restaurant_http_requests_total',
    'Tổng số lượt request HTTP',
    ['method', 'endpoint', 'status_code']
)
HTTP_REQUEST_DURATION = Histogram(
    'restaurant_http_request_duration_seconds',
    'Thời gian xử lý HTTP request',
    ['method', 'endpoint', 'status_code'],
    buckets=[0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5]
)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST', 'db'),
        port=int(os.getenv('DB_PORT', '5432')),
        database=os.getenv('DB_NAME', 'restaurant_db'),
        user=os.getenv('DB_USER', 'restaurant_user'),
        password=os.getenv('DB_PASSWORD', 'StrongPass#2026'),
        cursor_factory=RealDictCursor
    )

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def role_required(*allowed_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return redirect(url_for('login'))
            user_role = session.get('role', '')
            if user_role not in allowed_roles and 'admin' not in allowed_roles:
                flash('Bạn không có quyền truy cập chức năng này!', 'danger')
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    if hasattr(request, 'start_time'):
        duration = time.time() - request.start_time
        endpoint = request.endpoint or request.path
        status = str(response.status_code)
        HTTP_REQUESTS_TOTAL.labels(method=request.method, endpoint=endpoint, status_code=status).inc()
        HTTP_REQUEST_DURATION.labels(method=request.method, endpoint=endpoint, status_code=status).observe(duration)
        
        logger.info("HTTP Access Log", extra={
            'method': request.method,
            'path': request.path,
            'status': response.status_code,
            'duration_ms': round(duration * 1000, 2),
            'remote_ip': request.headers.get('X-Forwarded-For', request.remote_addr),
            'user': session.get('username', 'anonymous'),
            'student_id': 'DTC245200862'
        })
    return response

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/health')
def health():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.close()
        conn.close()
        return jsonify({
            'status': 'healthy',
            'database': 'connected',
            'student': 'Ho Quang Huy - DTC245200862',
            'topic': 'De 12 - Quan ly Nha hang / Order'
        }), 200
    except Exception as e:
        logger.error("Health check failed", extra={'error': str(e)})
        return jsonify({'status': 'unhealthy', 'error': str(e)}), 500

# ================= AUTHENTICATION ROUTES =================
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s;", (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()
        
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['full_name'] = user['full_name']
            session['role'] = user['role']
            logger.info("Đăng nhập thành công", extra={'user': username, 'role': user['role']})
            return redirect(url_for('index'))
        else:
            flash('Tên đăng nhập hoặc mật khẩu không chính xác!', 'danger')
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    user = session.get('username', '')
    session.clear()
    logger.info("Đăng xuất thành công", extra={'user': user})
    return redirect(url_for('login'))

# ================= NGHIỆP VỤ NHÀ HÀNG =================
@app.route('/')
@login_required
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) as total, COUNT(*) FILTER (WHERE status='available') as avail, COUNT(*) FILTER (WHERE status='occupied') as occ, COUNT(*) FILTER (WHERE status='reserved') as res FROM tables;")
    table_stats = cur.fetchone()
    
    cur.execute("SELECT COUNT(*) as total_orders, COUNT(*) FILTER (WHERE status='pending') as pending, COUNT(*) FILTER (WHERE status='cooking') as cooking, COALESCE(SUM(total_amount), 0) as revenue FROM orders;")
    order_stats = cur.fetchone()
    
    cur.execute("SELECT COUNT(*) as total_menu FROM menu_items WHERE is_available = true;")
    menu_stats = cur.fetchone()
    
    cur.execute("SELECT o.*, t.table_number FROM orders o LEFT JOIN tables t ON o.table_id = t.id ORDER BY o.created_at DESC LIMIT 6;")
    recent_orders = cur.fetchall()
    
    cur.close()
    conn.close()
    return render_template('index.html', tables=table_stats, orders=order_stats, menu_count=menu_stats['total_menu'], recent_orders=recent_orders)

@app.route('/tables', methods=['GET', 'POST'])
@login_required
def tables():
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        if session.get('role') not in ['admin', 'staff']:
            flash('Chỉ Quản trị viên và Nhân viên mới có quyền thêm bàn!', 'danger')
            return redirect(url_for('tables'))
        table_number = request.form.get('table_number')
        capacity = request.form.get('capacity', 4)
        cur.execute("INSERT INTO tables (table_number, capacity, status) VALUES (%s, %s, 'available');", (table_number, capacity))
        conn.commit()
        logger.info("Thêm bàn ăn mới", extra={'table_number': table_number, 'by': session.get('username')})
        cur.close()
        conn.close()
        return redirect(url_for('tables'))
        
    cur.execute("SELECT * FROM tables ORDER BY table_number ASC;")
    all_tables = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('tables.html', tables=all_tables)

@app.route('/tables/<int:table_id>/status', methods=['POST'])
@login_required
def update_table_status(table_id):
    status = request.form.get('status')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE tables SET status = %s WHERE id = %s;", (status, table_id))
    conn.commit()
    logger.info("Cập nhật trạng thái bàn", extra={'table_id': table_id, 'status': status, 'by': session.get('username')})
    cur.close()
    conn.close()
    return redirect(url_for('tables'))

@app.route('/menu', methods=['GET', 'POST'])
@login_required
def menu():
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        if session.get('role') != 'admin':
            flash('Chỉ Quản trị viên mới có quyền thay đổi thực đơn!', 'danger')
            return redirect(url_for('menu'))
        name = request.form.get('name')
        category_id = request.form.get('category_id')
        price = request.form.get('price')
        cur.execute("INSERT INTO menu_items (name, category_id, price, is_available) VALUES (%s, %s, %s, true);", (name, category_id, price))
        conn.commit()
        logger.info("Thêm món ăn mới", extra={'name': name, 'price': price, 'by': session.get('username')})
        cur.close()
        conn.close()
        return redirect(url_for('menu'))

    cur.execute("SELECT * FROM categories ORDER BY id ASC;")
    categories = cur.fetchall()
    cur.execute("SELECT m.*, c.name as category_name FROM menu_items m LEFT JOIN categories c ON m.category_id = c.id ORDER BY m.id ASC;")
    items = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('menu.html', categories=categories, menu_items=items)

@app.route('/menu/<int:item_id>/toggle', methods=['POST'])
@login_required
def toggle_menu(item_id):
    if session.get('role') not in ['admin', 'kitchen']:
        flash('Chỉ Quản trị viên hoặc Bếp mới được đổi trạng thái món!', 'danger')
        return redirect(url_for('menu'))
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE menu_items SET is_available = NOT is_available WHERE id = %s;", (item_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('menu'))

@app.route('/menu/<int:item_id>/delete', methods=['POST'])
@login_required
def delete_menu(item_id):
    if session.get('role') != 'admin':
        flash('Chỉ Quản trị viên mới được xóa món ăn!', 'danger')
        return redirect(url_for('menu'))
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM menu_items WHERE id = %s;", (item_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('menu'))

@app.route('/orders', methods=['GET', 'POST'])
@login_required
def orders():
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        table_id = request.form.get('table_id')
        customer_name = request.form.get('customer_name', 'Khách tại bàn')
        menu_item_id = request.form.get('menu_item_id')
        quantity = int(request.form.get('quantity', 1))
        
        cur.execute("SELECT price FROM menu_items WHERE id = %s;", (menu_item_id,))
        item = cur.fetchone()
        price = float(item['price']) if item else 0
        total = price * quantity
        
        cur.execute("INSERT INTO orders (table_id, customer_name, status, total_amount) VALUES (%s, %s, 'pending', %s) RETURNING id;", (table_id, customer_name, total))
        order_id = cur.fetchone()['id']
        
        cur.execute("INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price, subtotal) VALUES (%s, %s, %s, %s, %s);", (order_id, menu_item_id, quantity, price, total))
        
        if table_id:
            cur.execute("UPDATE tables SET status = 'occupied' WHERE id = %s;", (table_id,))
            
        conn.commit()
        logger.info("Tạo đơn hàng mới", extra={'order_id': order_id, 'total': total, 'by': session.get('username')})
        cur.close()
        conn.close()
        return redirect(url_for('orders'))
        
    cur.execute("SELECT o.*, t.table_number FROM orders o LEFT JOIN tables t ON o.table_id = t.id ORDER BY o.created_at DESC;")
    all_orders = cur.fetchall()
    cur.execute("SELECT * FROM tables ORDER BY table_number ASC;")
    tables = cur.fetchall()
    cur.execute("SELECT * FROM menu_items WHERE is_available = true ORDER BY name ASC;")
    menu_items = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('orders.html', orders=all_orders, tables=tables, menu_items=menu_items)

@app.route('/orders/<int:order_id>/status', methods=['POST'])
@login_required
def update_order_status(order_id):
    status = request.form.get('status')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE orders SET status = %s, updated_at = NOW() WHERE id = %s;", (status, order_id))
    
    if status in ['completed', 'cancelled']:
        cur.execute("SELECT table_id FROM orders WHERE id = %s;", (order_id,))
        res = cur.fetchone()
        if res and res['table_id']:
            t_id = res['table_id']
            cur.execute("SELECT COUNT(*) as cnt FROM orders WHERE table_id = %s AND status IN ('pending', 'cooking', 'served');", (t_id,))
            if cur.fetchone()['cnt'] == 0:
                cur.execute("UPDATE tables SET status = 'available' WHERE id = %s;", (t_id,))
                
    conn.commit()
    logger.info("Cập nhật trạng thái đơn hàng", extra={'order_id': order_id, 'status': status, 'by': session.get('username')})
    cur.close()
    conn.close()
    return redirect(url_for('orders'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
