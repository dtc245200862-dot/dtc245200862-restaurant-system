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
app.secret_key = os.getenv('SECRET_KEY', 'canteen-secure-secret-2026-dtc245200862')

# Structured JSON Logging
log_handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter(
    fmt='%(asctime)s %(levelname)s %(name)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
log_handler.setFormatter(formatter)
logger = logging.getLogger("canteen-app")
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)
logger.propagate = False

# Prometheus Metrics
HTTP_REQUESTS_TOTAL = Counter(
    'canteen_http_requests_total',
    'Tổng số lượt request HTTP',
    ['method', 'endpoint', 'status_code']
)
HTTP_REQUEST_DURATION = Histogram(
    'canteen_http_request_duration_seconds',
    'Thời gian xử lý HTTP request',
    ['method', 'endpoint', 'status_code'],
    buckets=[0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5]
)

def get_db():
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
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

def role_required(*allowed_roles):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if 'user_id' not in session:
                return redirect(url_for('login'))
            if session.get('role') not in allowed_roles:
                flash('Bạn không có quyền truy cập khu vực này!', 'danger')
                role = session.get('role')
                if role == 'admin':
                    return redirect(url_for('admin_dashboard'))
                elif role == 'staff':
                    return redirect(url_for('staff_dashboard'))
                else:
                    return redirect(url_for('customer_menu'))
            return f(*args, **kwargs)
        return decorated
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
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.close()
        conn.close()
        return jsonify({
            'status': 'healthy',
            'database': 'connected',
            'student': 'Ho Quang Huy - DTC245200862',
            'system': 'He thong Quan ly Nha hang / Căng tin'
        }), 200
    except Exception as e:
        logger.error("Health check failed", extra={'error': str(e)})
        return jsonify({'status': 'unhealthy', 'error': str(e)}), 500

# ================= AUTHENTICATION & REDIRECT =================
@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    role = session.get('role')
    if role == 'admin':
        return redirect(url_for('admin_dashboard'))
    elif role == 'staff':
        return redirect(url_for('staff_dashboard'))
    else:
        return redirect(url_for('customer_menu'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        conn = get_db()
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
            
            # Điều hướng vào đúng giao diện riêng của từng vai trò
            if user['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            elif user['role'] == 'staff':
                return redirect(url_for('staff_dashboard'))
            else:
                return redirect(url_for('customer_menu'))
        else:
            flash('Tên đăng nhập hoặc mật khẩu không chính xác!', 'danger')
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ================= 1. GIAO DIỆN KHÁCH HÀNG / SINH VIÊN (/customer) =================
@app.route('/customer/menu')
@login_required
@role_required('customer', 'admin')
def customer_menu():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM categories ORDER BY id ASC;")
    categories = cur.fetchall()
    
    cat_id = request.args.get('category')
    if cat_id:
        cur.execute("SELECT m.*, c.name as category_name FROM menu_items m LEFT JOIN categories c ON m.category_id = c.id WHERE m.category_id = %s ORDER BY m.id ASC;", (cat_id,))
    else:
        cur.execute("SELECT m.*, c.name as category_name FROM menu_items m LEFT JOIN categories c ON m.category_id = c.id ORDER BY m.id ASC;")
    menu_items = cur.fetchall()
    
    cur.execute("SELECT * FROM tables WHERE status = 'available' ORDER BY table_number ASC;")
    tables = cur.fetchall()
    
    cur.close()
    conn.close()
    return render_template('customer/menu.html', categories=categories, menu_items=menu_items, tables=tables, active_cat=cat_id)

@app.route('/customer/order', methods=['POST'])
@login_required
@role_required('customer', 'admin')
def customer_order():
    menu_item_id = request.form.get('menu_item_id')
    quantity = int(request.form.get('quantity', 1))
    order_type = request.form.get('order_type', 'dine_in')
    table_number = request.form.get('table_number', 'Mang về')
    note = request.form.get('note', '')
    
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM menu_items WHERE id = %s;", (menu_item_id,))
    item = cur.fetchone()
    
    if not item or not item['is_available'] or item['stock_quantity'] < quantity:
        flash('Món ăn đã hết suất hoặc không đủ số lượng tồn kho!', 'danger')
        cur.close()
        conn.close()
        return redirect(url_for('customer_menu'))
        
    price = float(item['price'])
    total = price * quantity
    user_id = session.get('user_id')
    customer_name = session.get('full_name')
    
    # Tạo đơn
    cur.execute(
        "INSERT INTO orders (user_id, customer_name, order_type, table_number, status, total_amount, note) VALUES (%s, %s, %s, %s, 'pending', %s, %s) RETURNING id;",
        (user_id, customer_name, order_type, table_number, total, note)
    )
    order_id = cur.fetchone()['id']
    
    cur.execute(
        "INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price, subtotal) VALUES (%s, %s, %s, %s, %s);",
        (order_id, menu_item_id, quantity, price, total)
    )
    
    # Giảm tồn kho
    cur.execute("UPDATE menu_items SET stock_quantity = stock_quantity - %s WHERE id = %s;", (quantity, menu_item_id))
    
    # Nếu ăn tại bàn thì cập nhật trạng thái bàn
    if order_type == 'dine_in':
        cur.execute("UPDATE tables SET status = 'occupied' WHERE table_number = %s;", (table_number,))
        
    conn.commit()
    logger.info("Sinh viên đặt món thành công", extra={'order_id': order_id, 'user': session.get('username')})
    cur.close()
    conn.close()
    flash('Đặt món thành công! Bạn có thể theo dõi tiến độ ở mục Đơn hàng của tôi.', 'success')
    return redirect(url_for('customer_orders'))

@app.route('/customer/orders')
@login_required
@role_required('customer', 'admin')
def customer_orders():
    conn = get_db()
    cur = conn.cursor()
    user_id = session.get('user_id')
    cur.execute("""
        SELECT o.*, 
               STRING_AGG(CONCAT(m.name, ' (x', oi.quantity, ')'), ', ') as items_summary
        FROM orders o
        LEFT JOIN order_items oi ON o.id = oi.order_id
        LEFT JOIN menu_items m ON oi.menu_item_id = m.id
        WHERE o.user_id = %s
        GROUP BY o.id
        ORDER BY o.created_at DESC;
    """, (user_id,))
    my_orders = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('customer/orders.html', orders=my_orders)

@app.route('/customer/review', methods=['POST'])
@login_required
@role_required('customer', 'admin')
def customer_review():
    menu_item_name = request.form.get('menu_item_name')
    rating = int(request.form.get('rating', 5))
    comment = request.form.get('comment', '')
    user_id = session.get('user_id')
    customer_name = session.get('full_name')
    
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO reviews (user_id, customer_name, menu_item_name, rating, comment) VALUES (%s, %s, %s, %s, %s);",
        (user_id, customer_name, menu_item_name, rating, comment)
    )
    conn.commit()
    cur.close()
    conn.close()
    flash('Cảm ơn bạn đã gửi đánh giá món ăn!', 'success')
    return redirect(url_for('customer_orders'))

# ================= 2. GIAO DIỆN NHÂN VIÊN CĂNG TIN (/staff) =================
@app.route('/staff/dashboard')
@login_required
@role_required('staff', 'admin')
def staff_dashboard():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) as total FROM menu_items WHERE is_available = true;")
    total_menu = cur.fetchone()['total']
    
    cur.execute("SELECT COUNT(*) as pending_count FROM orders WHERE status = 'pending';")
    pending_count = cur.fetchone()['pending_count']
    
    cur.execute("SELECT COALESCE(SUM(total_amount), 0) as revenue FROM orders WHERE status = 'completed';")
    revenue = cur.fetchone()['revenue']
    
    cur.execute("SELECT * FROM menu_items WHERE stock_quantity <= 10 ORDER BY stock_quantity ASC;")
    low_stock = cur.fetchall()
    
    cur.execute("SELECT o.*, STRING_AGG(CONCAT(m.name, ' (x', oi.quantity, ')'), ', ') as items FROM orders o LEFT JOIN order_items oi ON o.id = oi.order_id LEFT JOIN menu_items m ON oi.menu_item_id = m.id GROUP BY o.id ORDER BY o.created_at DESC LIMIT 5;")
    recent_orders = cur.fetchall()
    
    cur.close()
    conn.close()
    return render_template('staff/dashboard.html', total_menu=total_menu, pending_count=pending_count, revenue=revenue, low_stock=low_stock, recent_orders=recent_orders)

@app.route('/staff/orders')
@login_required
@role_required('staff', 'admin')
def staff_orders():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT o.*, 
               STRING_AGG(CONCAT(m.name, ' (x', oi.quantity, ')'), ', ') as items
        FROM orders o
        LEFT JOIN order_items oi ON o.id = oi.order_id
        LEFT JOIN menu_items m ON oi.menu_item_id = m.id
        GROUP BY o.id
        ORDER BY o.created_at DESC;
    """)
    all_orders = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('staff/orders.html', orders=all_orders)

@app.route('/staff/orders/<int:order_id>/status', methods=['POST'])
@login_required
@role_required('staff', 'admin')
def staff_order_status(order_id):
    status = request.form.get('status')
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE orders SET status = %s, updated_at = NOW() WHERE id = %s;", (status, order_id))
    
    if status in ['completed', 'cancelled']:
        cur.execute("SELECT table_number FROM orders WHERE id = %s;", (order_id,))
        res = cur.fetchone()
        if res and res['table_number'] and res['table_number'] != 'Mang về':
            t_num = res['table_number']
            cur.execute("SELECT COUNT(*) as cnt FROM orders WHERE table_number = %s AND status IN ('pending', 'cooking', 'served');", (t_num,))
            if cur.fetchone()['cnt'] == 0:
                cur.execute("UPDATE tables SET status = 'available' WHERE table_number = %s;", (t_num,))
                
    conn.commit()
    cur.close()
    conn.close()
    flash(f'Đã cập nhật trạng thái đơn #{order_id} thành {status}!', 'success')
    return redirect(url_for('staff_orders'))

@app.route('/staff/menu')
@login_required
@role_required('staff', 'admin')
def staff_menu():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT m.*, c.name as category_name FROM menu_items m LEFT JOIN categories c ON m.category_id = c.id ORDER BY m.id ASC;")
    items = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('staff/menu.html', menu_items=items)

@app.route('/staff/menu/<int:item_id>/stock', methods=['POST'])
@login_required
@role_required('staff', 'admin')
def staff_menu_stock(item_id):
    stock = int(request.form.get('stock', 0))
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE menu_items SET stock_quantity = %s, is_available = (%s > 0) WHERE id = %s;", (stock, stock, item_id))
    conn.commit()
    cur.close()
    conn.close()
    flash('Cập nhật số lượng tồn kho thành công!', 'success')
    return redirect(url_for('staff_menu'))

@app.route('/staff/menu/<int:item_id>/toggle', methods=['POST'])
@login_required
@role_required('staff', 'admin')
def staff_menu_toggle(item_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE menu_items SET is_available = NOT is_available WHERE id = %s;", (item_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('staff_menu'))

@app.route('/staff/tables')
@login_required
@role_required('staff', 'admin')
def staff_tables():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tables ORDER BY table_number ASC;")
    tables = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('staff/tables.html', tables=tables)

@app.route('/staff/tables/<int:table_id>/status', methods=['POST'])
@login_required
@role_required('staff', 'admin')
def staff_table_status(table_id):
    status = request.form.get('status')
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE tables SET status = %s WHERE id = %s;", (status, table_id))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('staff_tables'))

@app.route('/staff/reviews')
@login_required
@role_required('staff', 'admin')
def staff_reviews():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM reviews ORDER BY created_at DESC;")
    reviews = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('staff/reviews.html', reviews=reviews)

# ================= 3. GIAO DIỆN QUẢN TRỊ VIÊN ADMIN (/admin) =================
@app.route('/admin/dashboard')
@login_required
@role_required('admin')
def admin_dashboard():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT COALESCE(SUM(total_amount), 0) as revenue FROM orders WHERE status = 'completed';")
    revenue = float(cur.fetchone()['revenue'])
    
    cur.execute("SELECT COUNT(*) as total_orders FROM orders;")
    total_orders = cur.fetchone()['total_orders']
    
    cur.execute("SELECT COALESCE(SUM(total_cost), 0) as cost FROM inventory_invoices;")
    cost = float(cur.fetchone()['cost'])
    
    profit = revenue - cost
    
    cur.execute("SELECT * FROM inventory_invoices ORDER BY created_at DESC LIMIT 5;")
    recent_invoices = cur.fetchall()
    
    cur.execute("SELECT o.* FROM orders o ORDER BY o.created_at DESC LIMIT 5;")
    recent_orders = cur.fetchall()
    
    cur.close()
    conn.close()
    return render_template('admin/dashboard.html', revenue=revenue, total_orders=total_orders, cost=cost, profit=profit, invoices=recent_invoices, orders=recent_orders)

@app.route('/admin/reports')
@login_required
@role_required('admin')
def admin_reports():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT DATE(created_at) as order_date, COUNT(*) as count, SUM(total_amount) as daily_revenue
        FROM orders
        WHERE status = 'completed'
        GROUP BY DATE(created_at)
        ORDER BY order_date DESC;
    """)
    daily_reports = cur.fetchall()
    
    cur.execute("SELECT * FROM orders WHERE status = 'completed' ORDER BY created_at DESC;")
    completed_orders = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('admin/reports.html', daily_reports=daily_reports, completed_orders=completed_orders)

@app.route('/admin/inventory', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def admin_inventory():
    conn = get_db()
    cur = conn.cursor()
    if request.method == 'POST':
        name = request.form.get('invoice_name')
        purchase_cost = float(request.form.get('purchase_cost', 0))
        shipping_fee = float(request.form.get('shipping_fee', 0))
        total_cost = purchase_cost + shipping_fee
        cur.execute(
            "INSERT INTO inventory_invoices (invoice_name, purchase_cost, shipping_fee, total_cost) VALUES (%s, %s, %s, %s);",
            (name, purchase_cost, shipping_fee, total_cost)
        )
        conn.commit()
        flash('Đã thêm hóa đơn nhập hàng mới!', 'success')
        cur.close()
        conn.close()
        return redirect(url_for('admin_inventory'))
        
    cur.execute("SELECT * FROM inventory_invoices ORDER BY created_at DESC;")
    invoices = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('admin/inventory.html', invoices=invoices)

@app.route('/admin/accounts', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def admin_accounts():
    conn = get_db()
    cur = conn.cursor()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        full_name = request.form.get('full_name')
        role = request.form.get('role')
        cur.execute("INSERT INTO users (username, password, full_name, role) VALUES (%s, %s, %s, %s);", (username, password, full_name, role))
        conn.commit()
        flash('Tạo tài khoản mới thành công!', 'success')
        cur.close()
        conn.close()
        return redirect(url_for('admin_accounts'))
        
    cur.execute("SELECT * FROM users ORDER BY id ASC;")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('admin/accounts.html', users=users)

@app.route('/admin/menu', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def admin_menu():
    conn = get_db()
    cur = conn.cursor()
    if request.method == 'POST':
        name = request.form.get('name')
        category_id = request.form.get('category_id')
        price = request.form.get('price')
        stock = request.form.get('stock', 25)
        cur.execute("INSERT INTO menu_items (name, category_id, price, stock_quantity, is_available) VALUES (%s, %s, %s, %s, true);", (name, category_id, price, stock))
        conn.commit()
        flash('Thêm món ăn thành công!', 'success')
        cur.close()
        conn.close()
        return redirect(url_for('admin_menu'))
        
    cur.execute("SELECT * FROM categories ORDER BY id ASC;")
    categories = cur.fetchall()
    cur.execute("SELECT m.*, c.name as category_name FROM menu_items m LEFT JOIN categories c ON m.category_id = c.id ORDER BY m.id ASC;")
    items = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('admin/menu.html', categories=categories, menu_items=items)

@app.route('/admin/menu/<int:item_id>/delete', methods=['POST'])
@login_required
@role_required('admin')
def admin_menu_delete(item_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM menu_items WHERE id = %s;", (item_id,))
    conn.commit()
    cur.close()
    conn.close()
    flash('Đã xóa món ăn!', 'success')
    return redirect(url_for('admin_menu'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
