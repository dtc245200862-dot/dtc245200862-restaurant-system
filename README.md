# HỆ THỐNG QUẢN LÝ NHÀ HÀNG / ORDER (ĐỀ 12)
**HỌC PHẦN: TRIỂN KHAI VÀ QUẢN TRỊ HỆ THỐNG PHẦN MỀM**  
**TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN VÀ TRUYỀN THÔNG (ICTU)**

* **Sinh viên thực hiện:** Hồ Quang Huy
* **Mã sinh viên:** `DTC245200862`
* **Email:** `dtc245200862@ictu.edu.vn`
* **Lớp:** CNTT K23h - Khoa Công nghệ Thông tin

---

## 1. Giới thiệu Đề tài
Dự án triển khai một hệ thống quản lý nhà hàng và đặt món (Order) hoàn chỉnh theo kiến trúc Microservices và Container hóa bằng **Docker & Docker Compose**. Hệ thống bao gồm đầy đủ các phân hệ nghiệp vụ, cơ sở dữ liệu quan hệ, reverse proxy bảo mật SSL, hệ thống giám sát metrics thời gian thực, hệ thống thu thập log tập trung và các giải pháp tăng cường bảo mật (Hardening).

### Công nghệ sử dụng:
* **Web App:** Python 3.12 (Flask + Gunicorn), EJS/HTML5, Bootstrap 5 Responsive.
* **Cơ sở dữ liệu:** PostgreSQL 16 (Alpine).
* **Quản trị CSDL:** pgAdmin 4.
* **Reverse Proxy & SSL:** Nginx Alpine (HTTPS tự ký, Security Headers, Rate Limiting).
* **Giám sát (Monitoring):** Prometheus + Grafana + cAdvisor + Node Exporter.
* **Log tập trung (Logging):** Grafana Loki + Promtail (LogQL queries).
* **Điều phối & Tự động hóa:** Docker Compose.

---

## 2. Kiến trúc Hệ thống & Phân chia Mạng (Network Isolation)
Toàn bộ hệ thống được cô lập thành 3 mạng bridge nội bộ nhằm đạt tiêu chuẩn bảo mật (Hardening):
1. **`frontend-net`:** Giao tiếp giữa người dùng bên ngoài, Nginx, Web App và pgAdmin.
2. **`backend-net`:** Giao tiếp nội bộ giữa Web App, pgAdmin và Cơ sở dữ liệu PostgreSQL. Cổng 5432 của DB **không mở ra ngoài host**.
3. **`monitoring-net`:** Giao tiếp an toàn giữa Prometheus, Grafana, Loki, Promtail, cAdvisor và Web App.

---

## 3. Lịch sử 03 Commit trên Git theo đúng yêu cầu đề bài
Repository được xây dựng với đúng 3 commit mốc theo tiêu chuẩn của đề bài:
* **Commit 1:** `1458fb8` - *commit 1: Trien khai Website Quan ly Nha hang, PostgreSQL, pgAdmin va Nginx Reverse Proxy voi SSL*
* **Commit 2:** `f43e56a` - *commit 2: Tich hop he thong giam sat Prometheus va Grafana cho web, DB va container*
* **Commit 3:** `2cca163` - *commit 3: Trien khai log tap trung Loki, Promtail va Hardening bao mat he thong*

---

## 4. Hướng dẫn Khởi chạy Hệ thống (1 câu lệnh)

### Bước 1: Clone kho mã nguồn về máy
```bash
git clone https://github.com/dtc245200862/dtc245200862-restaurant-system.git
cd dtc245200862-restaurant-system
```

### Bước 2: Tạo chứng chỉ SSL tự ký cho Nginx (đã tạo sẵn)
```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout nginx/ssl/server.key \
  -out nginx/ssl/server.crt \
  -subj "/C=VN/ST=ThaiNguyen/L=ThaiNguyen/O=ICTU/OU=CNTT/CN=localhost"
```

### Bước 3: Khởi chạy toàn bộ hệ thống bằng Docker Compose
```bash
docker compose up -d --build
```

---

## 5. Danh sách các Cổng và Đường dẫn Dịch vụ

| Dịch vụ | Địa chỉ truy cập | Giao thức | Tài khoản / Mật khẩu |
| :--- | :--- | :--- | :--- |
| **Website Nhà hàng** | `https://localhost/` hoặc `https://<IP>/` | HTTPS (SSL) | Khách / Thu ngân |
| **Health Check** | `https://localhost/health` | HTTPS | Trả về JSON trạng thái |
| **App Metrics** | `https://localhost/metrics` | HTTPS | Prometheus metrics |
| **pgAdmin 4** | `https://localhost/pgadmin/` | HTTPS (Reverse proxy) | `dtc245200862@ictu.edu.vn` / `StrongPass#2026` |
| **Prometheus** | `http://localhost:9090` | HTTP | Không cần đăng nhập |
| **Grafana** | `http://localhost:3000` | HTTP | `admin` / `StrongPass#2026` |
| **Loki** | `http://localhost:3100` | HTTP | API nhận log |

---

## 6. Các câu truy vấn LogQL mẫu (Loki)
Tại giao diện Grafana (`http://localhost:3000`) > **Explore** > Chọn Data Source **Loki**:

1. **Truy vấn toàn bộ log của Web App:**
   ```logql
   {job="docker-containers"} |= "restaurant-web"
   ```
2. **Truy vấn lọc các request HTTP 200 thành công dạng JSON:**
   ```logql
   {job="docker-containers"} |= "HTTP Access Log" | json | status == 200
   ```
3. **Truy vấn phát hiện lỗi (ERROR hoặc Exception):**
   ```logql
   {job="docker-containers"} |= "error" or "ERROR" or "failed"
   ```

---

## 7. Các biện pháp Tăng cường Bảo mật (Hardening) đã áp dụng
1. **Non-root Container:** Web App chạy dưới user `appuser` (UID: 1001), không chạy bằng `root`.
2. **Network Isolation:** Chia 3 mạng độc lập (`frontend-net`, `backend-net`, `monitoring-net`). Cơ sở dữ liệu bị cô lập hoàn toàn trong `backend-net`.
3. **Dropping Capabilities:** Loại bỏ toàn bộ Linux capabilities dư thừa (`cap_drop: - ALL`).
4. **Nginx Security Headers & SSL:** Tích hợp HSTS, CSP, X-Frame-Options (chống Clickjacking), X-Content-Type-Options (chống MIME sniffing), Rate Limiting (chống brute-force / DDoS).
5. **Mật khẩu mạnh & Biến môi trường:** Không hard-code mật khẩu, quản lý tập trung qua file `.env`.
