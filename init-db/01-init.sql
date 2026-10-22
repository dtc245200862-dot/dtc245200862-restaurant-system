-- ====================================================================
-- HỆ THỐNG QUẢN LÝ NHÀ HÀNG & ĐẶT MÓN (ORDER) - ĐỀ 12
-- Sinh viên: Hồ Quang Huy - MSV: DTC245200862 - Lớp: CNTT K23h
-- Trường: ĐH Công nghệ Thông tin và Truyền thông (ICTU)
-- Cơ sở dữ liệu: PostgreSQL 16
-- ====================================================================

-- 1. BẢNG NGƯỜI DÙNG & PHÂN QUYỀN (USERS)
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('admin', 'staff', 'customer')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. BẢNG DANH MỤC MÓN ĂN (CATEGORIES)
CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- 3. BẢNG MÓN ĂN & TỒN KHO THÀNH PHẨM (MENU_ITEMS)
CREATE TABLE IF NOT EXISTS menu_items (
    id SERIAL PRIMARY KEY,
    category_id INT REFERENCES categories(id) ON DELETE SET NULL,
    name VARCHAR(150) NOT NULL,
    price NUMERIC(12, 2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 50 CHECK (stock_quantity >= 0),
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. BẢNG BÀN ĂN (TABLES)
CREATE TABLE IF NOT EXISTS tables (
    id SERIAL PRIMARY KEY,
    table_number VARCHAR(20) NOT NULL UNIQUE,
    capacity INT DEFAULT 4,
    status VARCHAR(20) DEFAULT 'available' CHECK (status IN ('available', 'occupied', 'reserved')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 5. BẢNG ĐƠN HÀNG (ORDERS)
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE SET NULL,
    customer_name VARCHAR(100) DEFAULT 'Khách hàng',
    order_type VARCHAR(20) DEFAULT 'dine_in' CHECK (order_type IN ('dine_in', 'take_away')),
    table_number VARCHAR(20) DEFAULT 'Mang về',
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'cooking', 'served', 'completed', 'cancelled')),
    total_amount NUMERIC(12, 2) DEFAULT 0,
    note TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. BẢNG CHI TIẾT ĐƠN HÀNG (ORDER_ITEMS)
CREATE TABLE IF NOT EXISTS order_items (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id) ON DELETE CASCADE,
    menu_item_id INT REFERENCES menu_items(id) ON DELETE RESTRICT,
    quantity INT NOT NULL DEFAULT 1 CHECK (quantity > 0),
    unit_price NUMERIC(12, 2) NOT NULL,
    subtotal NUMERIC(12, 2) NOT NULL
);

-- 7. BẢNG ĐÁNH GIÁ MÓN ĂN TỪ KHÁCH HÀNG (REVIEWS)
CREATE TABLE IF NOT EXISTS reviews (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE SET NULL,
    customer_name VARCHAR(100) NOT NULL,
    menu_item_name VARCHAR(150) NOT NULL,
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 8. BẢNG HÓA ĐƠN NHẬP NGUYÊN LIỆU / TÀI CHÍNH (INVENTORY_INVOICES)
CREATE TABLE IF NOT EXISTS inventory_invoices (
    id SERIAL PRIMARY KEY,
    invoice_name VARCHAR(150) NOT NULL,
    purchase_cost NUMERIC(12, 2) NOT NULL DEFAULT 0,
    shipping_fee NUMERIC(12, 2) NOT NULL DEFAULT 0,
    total_cost NUMERIC(12, 2) NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ====================================================================
-- DỮ LIỆU KHỞI TẠO MẪU (SEED DATA CHO DEMO NHÀ HÀNG)
-- ====================================================================

-- 1. Tài khoản mặc định cho 3 vai trò
INSERT INTO users (username, password, full_name, role) VALUES
('admin', '123456789', 'Hồ Quang Huy (Quản lý Nhà hàng)', 'admin'),
('nhanvien', '123456789', 'Lê Thu Ngân (Nhân viên Phục vụ)', 'staff'),
('sinhvien', '123456789', 'Nguyễn Văn An (Khách hàng)', 'customer')
ON CONFLICT (username) DO NOTHING;

-- 2. Danh mục món ăn Nhà hàng
INSERT INTO categories (name, description) VALUES
('Món khai vị & Salad', 'Các món khai vị thanh mát, kích thích vị giác'),
('Món chính thượng hạng', 'Bò bít tết, cá hồi và các món ăn đậm đà bổ dưỡng'),
('Món nướng & Lẩu đặc biệt', 'Set lẩu hải sản và sườn cừu nướng cao cấp'),
('Đồ uống & Tráng miệng', 'Rượu vang, nước ép trái cây tươi và món tráng miệng')
ON CONFLICT (name) DO NOTHING;

-- 3. Món ăn, đơn giá và tồn kho suất ăn ban đầu
INSERT INTO menu_items (category_id, name, price, stock_quantity, is_available) VALUES
(1, 'Salad rong nho sốt mè rang', 45000, 30, true),
(1, 'Khoai tây chiên bơ tỏi Pháp', 35000, 40, true),
(2, 'Bò bít tết sốt tiêu đen Wagyu', 150000, 25, true),
(2, 'Cá hồi áp chảo sốt chanh leo', 180000, 20, true),
(2, 'Gà nướng thảo mộc ngũ vị', 120000, 25, true),
(3, 'Set Lẩu Thái Hải Sản Hoàng Gia', 350000, 15, true),
(4, 'Trà đào cam sả thảo mộc', 30000, 50, true),
(4, 'Nước ép dưa hấu tươi mát lạnh', 25000, 40, true)
ON CONFLICT DO NOTHING;

-- 4. Bàn ăn trong nhà hàng
INSERT INTO tables (table_number, capacity, status) VALUES
('Bàn 01 (VIP)', 4, 'available'),
('Bàn 02', 4, 'occupied'),
('Bàn 03', 2, 'available'),
('Bàn 04 (Gia đình)', 6, 'available'),
('Bàn 05 (Sảnh tiệc)', 8, 'available')
ON CONFLICT (table_number) DO NOTHING;

-- 5. Đơn hàng mẫu ban đầu
INSERT INTO orders (user_id, customer_name, order_type, table_number, status, total_amount, note, created_at) VALUES
(3, 'Nguyễn Văn An (Khách hàng)', 'dine_in', 'Bàn 02', 'cooking', 225000, 'Bò bít tết làm chín vừa (medium-rare), cho nhiều sốt tiêu', CURRENT_TIMESTAMP - INTERVAL '15 minutes'),
(3, 'Nguyễn Văn An (Khách hàng)', 'take_away', 'Mang về', 'completed', 150000, 'Đóng hộp mang về chu đáo', CURRENT_TIMESTAMP - INTERVAL '2 hours')
ON CONFLICT DO NOTHING;

-- 6. Chi tiết đơn hàng mẫu
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price, subtotal) VALUES
(1, 3, 1, 150000, 150000),
(1, 1, 1, 45000, 45000),
(1, 7, 1, 30000, 30000),
(2, 3, 1, 150000, 150000)
ON CONFLICT DO NOTHING;

-- 7. Đánh giá món ăn mẫu
INSERT INTO reviews (user_id, customer_name, menu_item_name, rating, comment) VALUES
(3, 'Nguyễn Văn An (Khách hàng)', 'Bò bít tết sốt tiêu đen Wagyu', 5, 'Bò bít tết thịt rất mềm, sốt tiêu đen đậm đà chuẩn vị Âu. Phục vụ chu đáo 10/10!'),
(3, 'Nguyễn Văn An (Khách hàng)', 'Cá hồi áp chảo sốt chanh leo', 5, 'Cá hồi tươi, vỏ giòn sốt chanh leo chua ngọt vừa vặn.')
ON CONFLICT DO NOTHING;

-- 8. Hóa đơn nhập hàng mẫu cho quản trị tài chính nhà hàng
INSERT INTO inventory_invoices (invoice_name, purchase_cost, shipping_fee, total_cost, created_at) VALUES
('Nhập thịt bò Wagyu & Cá hồi Nauy tươi', 4500000, 80000, 4580000, CURRENT_TIMESTAMP - INTERVAL '2 days'),
('Nhập nguyên liệu đồ uống & rượu vang nhập khẩu', 2200000, 50000, 2250000, CURRENT_TIMESTAMP - INTERVAL '1 day'),
('Nhập rau củ quả Đà Lạt hữu cơ chuẩn VietGAP', 1200000, 30000, 1230000, CURRENT_TIMESTAMP - INTERVAL '5 hours')
ON CONFLICT DO NOTHING;
