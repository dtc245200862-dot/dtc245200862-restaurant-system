CREATE TABLE IF NOT EXISTS tables (
    id SERIAL PRIMARY KEY,
    table_number VARCHAR(20) NOT NULL UNIQUE,
    capacity INT DEFAULT 4,
    status VARCHAR(20) DEFAULT 'available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE IF NOT EXISTS menu_items (
    id SERIAL PRIMARY KEY,
    category_id INT REFERENCES categories(id) ON DELETE SET NULL,
    name VARCHAR(150) NOT NULL,
    price NUMERIC(12, 2) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    table_id INT REFERENCES tables(id) ON DELETE SET NULL,
    customer_name VARCHAR(100) DEFAULT 'Khách tại bàn',
    status VARCHAR(20) DEFAULT 'pending',
    total_amount NUMERIC(12, 2) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS order_items (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id) ON DELETE CASCADE,
    menu_item_id INT REFERENCES menu_items(id) ON DELETE RESTRICT,
    quantity INT NOT NULL DEFAULT 1,
    unit_price NUMERIC(12, 2) NOT NULL,
    subtotal NUMERIC(12, 2) NOT NULL
);

INSERT INTO tables (table_number, capacity, status) VALUES
('Bàn 01', 4, 'available'),
('Bàn 02', 4, 'occupied'),
('Bàn 03', 2, 'available'),
('Bàn 04', 6, 'reserved'),
('Bàn 05', 8, 'available')
ON CONFLICT (table_number) DO NOTHING;

INSERT INTO categories (name, description) VALUES
('Món khai vị', 'Các món nhẹ kích thích vị giác'),
('Món chính', 'Món ăn đậm đà, bổ dưỡng'),
('Món nướng & lẩu', 'Set lẩu và đồ nướng'),
('Đồ uống & Tráng miệng', 'Nước ép và tráng miệng')
ON CONFLICT (name) DO NOTHING;

INSERT INTO menu_items (category_id, name, price, is_available) VALUES
(1, 'Salad rong nho sốt mè rang', 45000, true),
(1, 'Khoai tây chiên bơ tỏi', 35000, true),
(2, 'Bò bít tết sốt tiêu đen', 150000, true),
(2, 'Cá hồi áp chảo sốt chanh leo', 180000, true),
(2, 'Gà quay thảo mộc ngũ vị', 120000, true),
(3, 'Set Lẩu Thái Hải Sản đặc biệt', 350000, true),
(4, 'Trà đào cam sả thảo mộc', 30000, true),
(4, 'Nước ép dưa hấu tươi', 25000, true);

INSERT INTO orders (table_id, customer_name, status, total_amount) VALUES
(2, 'Nguyễn Văn An', 'cooking', 225000);

INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price, subtotal) VALUES
(1, 3, 1, 150000, 150000),
(1, 1, 1, 45000, 45000),
(1, 7, 1, 30000, 30000);
