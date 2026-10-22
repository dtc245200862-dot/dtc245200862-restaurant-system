-- ====================================================================
-- HỆ THỐNG QUẢN LÝ NHÀ HÀNG / CĂNG TIN & ĐẶT MÓN (ORDER) - ĐỀ 12
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

-- 7. BẢNG ĐÁNH GIÁ MÓN ĂN TỪ SINH VIÊN (REVIEWS)
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
-- DỮ LIỆU KHỞI TẠO MẪU (SEED DATA CHO DEMO)
-- ====================================================================

-- 1. Tài khoản mặc định cho 3 vai trò
INSERT INTO users (username, password, full_name, role) VALUES
('admin', '123456789', 'Quản trị viên Căng tin', 'admin'),
('nhanvien', '123456789', 'Nhân viên Phục vụ Căng tin', 'staff'),
('sinhvien', '123456789', 'Hồ Quang Huy (DTC245200862)', 'customer')
ON CONFLICT (username) DO NOTHING;

-- 2. Danh mục món ăn
INSERT INTO categories (name, description) VALUES
('Cơm suất sinh viên', 'Cơm suất nóng hổi, đầy đủ dinh dưỡng cho sinh viên'),
('Bún - Phở - Mì', 'Món nước ăn sáng và trưa hấp dẫn'),
('Bánh mì & Đồ ăn nhanh', 'Phục vụ nhanh gọn giữa các ca học'),
('Đồ uống & Tráng miệng', 'Trà đào, nước ép và đồ tráng miệng thanh mát')
ON CONFLICT (name) DO NOTHING;

-- 3. Món ăn, đơn giá và tồn kho suất ăn ban đầu
INSERT INTO menu_items (category_id, name, price, stock_quantity, is_available) VALUES
(1, 'Cơm sườn nướng mật ong', 35000, 30, true),
(1, 'Cơm gà sốt nấm xé tay', 30000, 25, true),
(1, 'Cơm thịt kho tàu trứng cút', 30000, 20, true),
(2, 'Bún bò Huế giò heo', 35000, 25, true),
(2, 'Phở gà ta lá chanh', 30000, 20, true),
(3, 'Bánh mì pate trứng nướng bơ', 20000, 40, true),
(3, 'Khoai tây chiên lắc phô mai', 25000, 35, true),
(4, 'Trà đào cam sả thảo mộc', 18000, 50, true),
(4, 'Trà sữa trân châu hoàng gia', 22000, 40, true)
ON CONFLICT DO NOTHING;

-- 4. Bàn ăn trong căng tin
INSERT INTO tables (table_number, capacity, status) VALUES
('Bàn 01', 4, 'available'),
('Bàn 02', 4, 'occupied'),
('Bàn 03', 2, 'available'),
('Bàn 04', 6, 'available'),
('Bàn 05', 8, 'available')
ON CONFLICT (table_number) DO NOTHING;

-- 5. Đơn hàng mẫu ban đầu
INSERT INTO orders (user_id, customer_name, order_type, table_number, status, total_amount, note, created_at) VALUES
(3, 'Hồ Quang Huy (DTC245200862)', 'dine_in', 'Bàn 02', 'cooking', 53000, 'Không lấy hành tây, cho nhiều ớt', CURRENT_TIMESTAMP - INTERVAL '15 minutes'),
(3, 'Hồ Quang Huy (DTC245200862)', 'take_away', 'Mang về', 'completed', 35000, 'Đóng gói mang về lớp K23h', CURRENT_TIMESTAMP - INTERVAL '2 hours')
ON CONFLICT DO NOTHING;

-- 6. Chi tiết đơn hàng mẫu
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price, subtotal) VALUES
(1, 1, 1, 35000, 35000),
(1, 8, 1, 18000, 18000),
(2, 4, 1, 35000, 35000)
ON CONFLICT DO NOTHING;

-- 7. Đánh giá món ăn mẫu
INSERT INTO reviews (user_id, customer_name, menu_item_name, rating, comment) VALUES
(3, 'Hồ Quang Huy (DTC245200862)', 'Cơm sườn nướng mật ong', 5, 'Sườn nướng rất mềm và thơm, sốt mật ong vừa vị. 10/10!'),
(3, 'Hồ Quang Huy (DTC245200862)', 'Trà đào cam sả thảo mộc', 5, 'Trà thơm mát, rất giải nhiệt sau giờ học căng thẳng.')
ON CONFLICT DO NOTHING;

-- 8. Hóa đơn nhập hàng mẫu cho quản trị tài chính
INSERT INTO inventory_invoices (invoice_name, purchase_cost, shipping_fee, total_cost, created_at) VALUES
('Nhập thực phẩm tươi sống (Gà, Sườn, Thịt)', 2500000, 50000, 2550000, CURRENT_TIMESTAMP - INTERVAL '2 days'),
('Nhập nguyên liệu đồ uống (Trà, Sữa, Siro)', 1200000, 30000, 1230000, CURRENT_TIMESTAMP - INTERVAL '1 day'),
('Nhập rau củ quả Đà Lạt chuẩn VietGAP', 800000, 20000, 820000, CURRENT_TIMESTAMP - INTERVAL '5 hours')
ON CONFLICT DO NOTHING;
