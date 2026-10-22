# TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN VÀ TRUYỀN THÔNG (ICTU)
## KHOA CÔNG NGHỆ THÔNG TIN

=======================================================
# BÁO CÁO ĐÁNH GIÁ KỸ NĂNG / BÀI TẬP LỚN
### HỌC PHẦN: TRIỂN KHAI VÀ QUẢN TRỊ HỆ THỐNG PHẦN MỀM

## ĐỀ TÀI:
# ĐỀ 12: HỆ THỐNG QUẢN LÝ NHÀ HÀNG & ĐẶT MÓN (ORDER)
**(Website Quản lý Món ăn, Đơn hàng, Sơ đồ Bàn ăn, Báo cáo Doanh thu)**

**Giảng viên hướng dẫn:** Bộ môn Hệ thống Thông tin & Mạng máy tính  
**Sinh viên thực hiện:**
| Họ và tên | Mã sinh viên | Email | Lớp |
| :--- | :--- | :--- | :--- |
| **Hồ Quang Huy** | **DTC245200862** | **dtc245200862@ictu.edu.vn** | CNTT K23h |

*Thái Nguyên, năm 2026*
=======================================================

## MỤC LỤC
1. [CHƯƠNG 1: TỔNG QUAN ĐỀ TÀI VÀ KIẾN TRÚC TỔNG THỂ HỆ THỐNG](#chương-1-tổng-quan-đề-tài-và-kiến-trúc-tổng-thể-hệ-thống)
   - 1.1. Bối cảnh và Mục tiêu của Đề tài (Đề 12)
   - 1.2. Phân hệ 3 Giao diện Người dùng Độc lập (RBAC)
   - 1.3. Mô hình Kiến trúc 10 Container với Docker Compose
   - 1.4. Thiết kế Phân chia Mạng Cô lập (Network Isolation)
2. [CHƯƠNG 2: QUẢN LÝ MÃ NGUỒN VÀ QUY ƯỚC COMMIT TRÊN GITHUB (1.5 ĐIỂM)](#chương-2-quản-lý-mã-nguồn-và-quy-ước-commit-trên-github-15-điểm)
   - 2.1. Cấu trúc Tổ chức Thư mục Dự án
   - 2.2. Tài khoản GitHub và Quy ước Đặt tên theo MSV
   - 2.3. Lịch sử Commit và Tiến trình Phát triển
   - 2.4. Tài liệu Hướng dẫn Triển khai (README.md) và Cấu hình .env
3. [CHƯƠNG 3: TRIỂN KHAI ỨNG DỤNG WEB & CSDL POSTGRESQL + PGADMIN (1.5 ĐIỂM)](#chương-3-triển-khai-ứng-dụng-web--csdl-postgresql--pgadmin-15-điểm)
   - 3.1. Thiết kế Mô hình CSDL Quan hệ PostgreSQL (8 Bảng)
   - 3.2. Xây dựng Website Quản lý Nhà hàng / Order bằng Python Flask
   - 3.3. Tích hợp Công cụ Quản trị CSDL pgAdmin 4
   - 3.4. Cơ chế Kiểm tra Sức khỏe (Healthcheck) và Tự phục hồi
4. [CHƯƠNG 4: TRIỂN KHAI NGINX REVERSE PROXY VÀ BẢO MẬT SSL/HTTPS (1.5 ĐIỂM)](#chương-4-triển-khai-nginx-reverse-proxy-và-bảo-mật-sslhttps-15-điểm)
   - 4.1. Vai trò của Nginx Reverse Proxy làm Cổng vào Duy nhất
   - 4.2. Khởi tạo và Cấu hình Chứng chỉ Bảo mật SSL Tự ký (HTTPS)
   - 4.3. Chuyển hướng HTTP sang HTTPS Tự động (301 Permanent Redirect)
   - 4.4. Cấu hình Security Headers Chống Tấn công Web Phổ biến
   - 4.5. Cơ chế Giới hạn Tần suất Truy cập (Rate Limiting)
5. [CHƯƠNG 5: HỆ THỐNG GIÁM SÁT THỜI GIAN THỰC PROMETHEUS & GRAFANA (1.5 ĐIỂM)](#chương-5-hệ-thống-giám-sát-thời-gian-thực-prometheus--grafana-15-điểm)
   - 5.1. Kiến trúc Hệ thống Giám sát Metrics Thời gian thực
   - 5.2. Thu thập Metrics Nghiệp vụ từ Ứng dụng Web (/metrics)
   - 5.3. Giám sát Container (cAdvisor) và Hệ điều hành (Node Exporter)
   - 5.4. Thiết lập Dashboard Hiển thị Trực quan trên Grafana
6. [CHƯƠNG 6: HỆ THỐNG THU THẬP LOG TẬP TRUNG LOKI & PROMTAIL (1.5 ĐIỂM)](#chương-6-hệ-thống-thu-thập-log-tập-trung-loki--promtail-15-điểm)
   - 6.1. Kiến trúc Hệ thống Quản trị Log Tập trung Loki + Promtail
   - 6.2. Cấu hình Structured JSON Logging cho Ứng dụng Web
   - 6.3. Cấu hình Promtail Tự động Thu thập Log Container Docker
   - 6.4. Thực hành và Minh chứng 03 Câu truy vấn LogQL Thực tế
7. [CHƯƠNG 7: TĂNG CƯỜNG BẢO MẬT HỆ THỐNG (SYSTEM HARDENING) (1.5 ĐIỂM)](#chương-7-tăng-cường-bảo-mật-hệ-thống-system-hardening-15-điểm)
   - 7.1. Chạy Container với Người dùng Đặc quyền thấp (Non-root User)
   - 7.2. Cô lập Mạng 3 Tầng (Multi-tier Network Isolation)
   - 7.3. Tước bỏ Linux Capabilities Nguy hiểm (cap_drop: ALL)
   - 7.4. Bảo mật CSDL và Kiểm soát Biến môi trường (.env)
   - 7.5. Ẩn Thông tin Phiên bản Máy chủ Web (server_tokens off)
8. [CHƯƠNG 8: TỔNG THỂ HỆ THỐNG, HƯỚNG DẪN DEMO VÀ KẾT LUẬN (1.0 ĐIỂM)](#chương-8-tổng-thể-hệ-thống-hướng-dẫn-demo-và-kết-luận-10-điểm)
   - 8.1. Hướng dẫn Vận hành 1 Lệnh Duy nhất bằng Docker Compose
   - 8.2. Danh mục Tài khoản và Kịch bản Nghiệm thu (Demo Checklist)
   - 8.3. Bảng Đối chiếu Kết quả với 7 Tiêu chí Đánh giá của Học phần
   - 8.4. Kết luận và Hướng phát triển Đề tài

---

# CHƯƠNG 1: TỔNG QUAN ĐỀ TÀI VÀ KIẾN TRÚC TỔNG THỂ HỆ THỐNG

## 1.1. Bối cảnh và Mục tiêu của Đề tài (Đề 12)
Trong thời đại chuyển đổi số ngành dịch vụ ẩm thực (F&B), các nhà hàng hiện đại đòi hỏi một hệ thống phần mềm vận hành trực tuyến, có khả năng xử lý đơn đặt món (Order) tức thời, quản lý chặt chẽ trạng thái bàn ăn và cập nhật thực đơn theo thời gian thực.
Đồng thời, theo yêu cầu của học phần **Triển khai và Quản trị Hệ thống Phần mềm** tại Trường Đại học Công nghệ Thông tin và Truyền thông (ICTU), hệ thống không chỉ dừng lại ở mặt lập trình ứng dụng đơn thuần mà phải được **triển khai theo chuẩn công nghiệp DevOps**:
- Triển khai toàn bộ các dịch vụ bằng **Docker Compose**.
- Đảm bảo an toàn bảo mật mạng thông qua **Nginx Reverse Proxy với giao thức HTTPS/SSL**.
- Xây dựng hệ thống giám sát tải, tài nguyên phần cứng và hiệu năng bằng **Prometheus + Grafana**.
- Quản trị log tập trung, phân tích sự cố bằng **Loki + Promtail** với ngôn ngữ truy vấn **LogQL**.
- Áp dụng các kỹ thuật **Hardening** bảo mật nâng cao nhằm bảo vệ hạ tầng máy chủ.

## 1.2. Phân hệ 3 Giao diện Người dùng Độc lập (RBAC)
Hệ thống được thiết kế hoàn toàn theo mô hình phân quyền người dùng (Role-Based Access Control) với 3 không gian làm việc chuyên biệt:
1. **Khách hàng (`/customer`):**
   - Xem thực đơn được phân theo 4 danh mục ẩm thực sang trọng.
   - Chọn hình thức ăn tại bàn (từ Bàn 01 đến Bàn 08) hoặc mang về.
   - Thêm món, điều chỉnh số lượng, đặt món với nút bấm gọn gàng và giá tiền hiển thị chuẩn xác.
   - Theo dõi trạng thái đơn hàng thời gian thực (*Đang nấu*, *Đã phục vụ*, *Hoàn thành*).
   - Đánh giá chất lượng phục vụ và món ăn (1 đến 5 sao kèm phản hồi chi tiết).
2. **Nhân viên Phục vụ Nhà hàng (`/staff`):**
   - Tiếp nhận và duyệt đơn đặt món tức thời theo từng bàn.
   - Cập nhật tiến độ chế biến đơn hàng theo vòng đời: `Chờ xử lý -> Đang nấu -> Đã lên món -> Hoàn tất`.
   - Xem danh sách món ăn trong từng đơn rõ ràng (tên món và số lượng, không bị lỗi mã hệ thống).
   - Kiểm soát tồn kho món ăn thành phẩm, bật/tắt trạng thái phục vụ của món.
   - Theo dõi trực quan sơ đồ bàn ăn của nhà hàng (*Bàn trống*, *Có khách*, *Đặt trước*).
3. **Quản trị viên Admin (`/admin`):**
   - Bảng điều khiển tài chính trực quan: Doanh thu thực nhận, Chi phí nhập nguyên liệu, Lợi nhuận ròng.
   - Quản lý hóa đơn nhập nguyên liệu, phí vận chuyển và công nợ nhà cung cấp.
   - Quản lý danh sách tài khoản người dùng, phân quyền nhân viên và khách hàng.
   - Xuất dữ liệu báo cáo phục vụ công tác thanh quyết toán định kỳ.

## 1.3. Mô hình Kiến trúc 10 Container với Docker Compose
Toàn bộ hệ thống gồm 10 container dịch vụ chuyên biệt hoạt động phối hợp nhịp nhàng:
1. `restaurant-web`: Ứng dụng Backend/Frontend viết bằng Python Flask + Gunicorn, chạy trên nền Alpine Linux siêu nhẹ.
2. `restaurant-db`: Hệ quản trị CSDL quan hệ PostgreSQL 16 Alpine, lưu trữ dữ liệu bền vững qua Docker Named Volume (`postgres_data`).
3. `restaurant-pgadmin`: Giao diện quản trị CSDL pgAdmin 4 trực quan.
4. `restaurant-nginx`: Máy chủ Nginx Reverse Proxy làm chốt chặn duy nhất mở cổng ra bên ngoài (Port 80/443), tiếp nhận request HTTPS và phân phối vào mạng nội bộ.
5. `restaurant-prometheus`: Máy chủ giám sát, định kỳ 5s cào metrics từ các dịch vụ.
6. `restaurant-grafana`: Nền tảng trực quan hóa số liệu giám sát và log.
7. `restaurant-cadvisor`: Công cụ của Google thu thập metrics tài nguyên phần cứng của từng Docker Container.
8. `restaurant-node-exporter`: Thu thập chỉ số tài nguyên phần cứng máy chủ Linux (CPU, RAM, Disk, Network).
9. `restaurant-loki`: Máy chủ lưu trữ và lập chỉ mục log tập trung.
10. `restaurant-promtail`: Log agent tự động thu thập log từ Docker daemon đẩy về Loki.

## 1.4. Thiết kế Phân chia Mạng Cô lập (Network Isolation)
Thay vì sử dụng một mạng bridge mặc định tiềm ẩn nguy cơ bảo mật, hệ thống được chia tách thành **03 mạng độc lập (Network Isolation)**:
* **`frontend-net`:** Chỉ chứa `nginx`, `web` và `pgadmin`. Nơi tiếp nhận lưu lượng truy cập từ người dùng.
* **`backend-net`:** Chỉ chứa `web`, `pgadmin` và `db`. Cơ sở dữ liệu PostgreSQL tuyệt đối không có cổng kết nối ra ngoài Internet, ngăn ngừa hoàn toàn các cuộc tấn công quét cổng CSDL.
* **`monitoring-net`:** Chỉ chứa `web`, `prometheus`, `grafana`, `cadvisor`, `node-exporter`, `loki` và `promtail`. Mạng chuyên dụng cho giám sát, tách biệt khỏi luồng dữ liệu nghiệp vụ của khách hàng.

---

# CHƯƠNG 2: QUẢN LÝ MÃ NGUỒN VÀ QUY ƯỚC COMMIT TRÊN GITHUB (1.5 ĐIỂM)

## 2.1. Cấu trúc Tổ chức Thư mục Dự án
Dự án được sắp xếp khoa học, phân chia module rõ ràng:
```text
dtc245200862-restaurant-system/
├── app/                        # Mã nguồn ứng dụng Web Quản lý Nhà hàng
│   ├── app.py                  # Backend Flask xử lý logic nghiệp vụ, metrics, logs
│   ├── requirements.txt        # Danh sách thư viện Python
│   ├── Dockerfile              # Dockerfile đa tầng, non-root user (Hardening)
│   ├── templates/              # Giao diện HTML (customer, staff, admin, login)
│   └── static/                 # Tệp CSS, JS tĩnh (Bootstrap 5, Icons, Chart.js)
├── init-db/                    # Tập lệnh khởi tạo CSDL
│   └── 01-init.sql             # Schema 8 bảng, khóa ngoại và dữ liệu mẫu nhà hàng
├── nginx/                      # Cấu hình Nginx Reverse Proxy & SSL
│   ├── nginx.conf              # File cấu hình proxy, security headers, rate limit
│   └── ssl/                    # Chứng chỉ số SSL tự ký (server.crt, server.key)
├── prometheus/                 # Cấu hình máy chủ Prometheus
│   └── prometheus.yml          # Scrape configs định kỳ cho web, node, cadvisor
├── grafana/                    # Cấu hình tự động Provisioning cho Grafana
│   └── provisioning/
│       └── datasources/        # Tự động nạp Prometheus và Loki làm Data Sources
├── loki/                       # Cấu hình máy chủ Log Loki
│   └── loki-config.yml         # Cấu hình schema, storage chunks cho log
├── promtail/                   # Cấu hình Log Shipper Promtail
│   └── promtail-config.yml     # Cấu hình cào docker container log đẩy vào Loki
├── .env                        # Biến môi trường mật khẩu (bảo mật)
├── .env.example                # Mẫu biến môi trường an toàn đẩy lên GitHub
├── docker-compose.yml          # File điều phối khởi chạy toàn bộ 10 dịch vụ
└── README.md                   # Hướng dẫn chi tiết cài đặt và vận hành hệ thống
```

## 2.2. Tài khoản GitHub và Quy ước Đặt tên theo MSV
Theo đúng yêu cầu của đề tài:
- Tài khoản GitHub: **`dtc245200862-dot`**
- Tên Repository: **`dtc245200862-restaurant-system`**  
  URL: `https://github.com/dtc245200862-dot/dtc245200862-restaurant-system.git`
- Email tác giả commit: `dtc245200862@ictu.edu.vn`
- Tác giả: `Hồ Quang Huy` (MSV: `DTC245200862`)

## 2.3. Lịch sử Commit và Tiến trình Phát triển
Kho mã nguồn phản ánh trung thực tiến trình xây dựng hệ thống với các commit mốc rõ ràng:
1. **Commit 1 (`1458fb8`):**  
   *Thông điệp:* `commit 1: Trien khai Website Quan ly Nha hang, PostgreSQL, pgAdmin va Nginx Reverse Proxy voi SSL`  
   *Nội dung:* Đóng gói ứng dụng web quản lý món ăn, bàn ăn, đơn hàng; tích hợp CSDL PostgreSQL 16 và pgAdmin; thiết lập Nginx Reverse Proxy với HTTPS tự ký và Security Headers.
2. **Commit 2 (`f43e56a`):**  
   *Thông điệp:* `commit 2: Tich hop he thong giam sat Prometheus va Grafana cho web, DB va container`  
   *Nội dung:* Tích hợp endpoint `/metrics` trong Flask, bổ sung Prometheus Server, cAdvisor, Node Exporter và Grafana tự động nạp Data Source.
3. **Commit 3 (`2cca163`):**  
   *Thông điệp:* `commit 3: Trien khai log tap trung Loki, Promtail va Hardening bao mat he thong`  
   *Nội dung:* Xây dựng hệ thống log tập trung với Grafana Loki và Promtail; cấu hình structured JSON logging; áp dụng các biện pháp bảo mật Hardening (non-root container, network isolation, drop capabilities).
4. **Commit Tinh chỉnh & Nâng cấp Giao diện (`b466d39`):**  
   *Thông điệp:* `fix(ui): thu nho nut danh muc, gia tien va sua loi hien thi mon da goi o trang quan ly`  
   *Nội dung:* Chuẩn hóa kích thước nút danh mục dạng pill nhỏ gọn, điều chỉnh font giá món ăn cân đối, giải quyết triệt để lỗi xung đột `dict.items` trên trang quản lý đơn của nhân viên.

Minh chứng lệnh kiểm tra lịch sử commit trong hệ thống:
```bash
hohuy@ubuntu:~/dtc245200862-restaurant-system$ git log --oneline -n 5
b466d39 fix(ui): thu nho nut danh muc, gia tien va sua loi hien thi mon da goi o trang quan ly
4457744 feat(branding): chuan hoa 100% thuong hieu Nha Hang (Restaurant Management System) cho De 12
6aee903 feat(ui): tich hop thu vien Bootstrap 5 va Icon offline truc tiep vao static assets
23ae29f fix(system): dong bo CSDL init.sql, xu ly hoan ton kho khi huy don va cap quyen root cho Promtail
4a27b3b docs: them bao cao he thong va huong dan readme
```

## 2.4. Tài liệu Hướng dẫn Triển khai (README.md) và Cấu hình .env
Tệp `README.md` cung cấp đầy đủ thông tin:
- Thông tin sinh viên, mã đề tài, trường lớp.
- Kiến trúc mạng và bảng danh mục các cổng kết nối.
- Hướng dẫn vận hành hệ thống bằng một dòng lệnh `docker compose up -d`.
- Danh sách tài khoản mẫu truy cập pgAdmin và Grafana.
- Mẫu các câu truy vấn LogQL minh họa.
Tệp `.env.example` liệt kê đầy đủ các biến môi trường cần thiết nhưng không chứa mật khẩu nhạy cảm, trong khi tệp `.env` thật được lưu trữ cục bộ an toàn.

---

# CHƯƠNG 3: TRIỂN KHAI ỨNG DỤNG WEB & CSDL POSTGRESQL + PGADMIN (1.5 ĐIỂM)

## 3.1. Thiết kế Mô hình CSDL Quan hệ PostgreSQL (8 Bảng)
Cơ sở dữ liệu `restaurant_db` được thiết kế chuẩn hóa bậc 3 (3NF), gồm 8 bảng với các ràng buộc khóa ngoại chặt chẽ:
1. **`users` (Người dùng & Phân quyền):** Lưu `id`, `username`, mật khẩu băm, họ tên và vai trò (`role IN ('admin', 'staff', 'customer')`).
2. **`categories` (Danh mục Món ăn):** 4 nhóm ẩm thực nhà hàng chính: *Món khai vị & Salad*, *Món chính thượng hạng*, *Món nướng & Lẩu đặc biệt*, *Đồ uống & Tráng miệng*.
3. **`menu_items` (Món ăn & Tồn kho):** Tên món, đơn giá, số lượng tồn kho thành phẩm (`stock_quantity >= 0`), trạng thái phục vụ (`is_available`), liên kết khóa ngoại với `categories(id)`.
4. **`tables` (Sơ đồ Bàn ăn):** Lưu mã số bàn (`table_number`), sức chứa (`capacity`), trạng thái (`status IN ('available', 'occupied', 'reserved')`).
5. **`orders` (Đơn đặt món):** Khách hàng (`customer_name`), hình thức (`order_type IN ('dine_in', 'take_away')`), số bàn, trạng thái (`status IN ('pending', 'cooking', 'served', 'completed', 'cancelled')`), tổng tiền, ghi chú chế biến.
6. **`order_items` (Chi tiết Đơn hàng):** Khóa ngoại liên kết `orders(id)` và `menu_items(id)`, lưu số lượng (`quantity`), đơn giá tại thời điểm đặt (`unit_price`), thành tiền (`subtotal`).
7. **`reviews` (Đánh giá Khách hàng):** Lưu đánh giá chất lượng món ăn (1 đến 5 sao) và bình luận trải nghiệm của thực khách.
8. **`inventory_invoices` (Chi phí Nhập hàng):** Ghi nhận hóa đơn mua nguyên vật liệu, tiền vận chuyển, tổng chi phí để phục vụ phân hệ tính lợi nhuận ròng của Quản trị viên.

Tệp `init-db/01-init.sql` được gắn tự động vào thư mục `/docker-entrypoint-initdb.d` của PostgreSQL để khởi tạo toàn bộ cấu trúc và dữ liệu mẫu khi hệ thống khởi chạy lần đầu.

## 3.2. Xây dựng Website Quản lý Nhà hàng / Order bằng Python Flask
Ứng dụng web được phát triển bằng Python 3.12 sử dụng micro-framework Flask kết hợp server Gunicorn chuẩn công nghiệp:
- Giao diện thân thiện, chuẩn Bootstrap 5 responsive trên cả điện thoại và máy tính.
- Tích hợp toàn bộ thư viện tĩnh (Bootstrap CSS/JS, Bootstrap Icons) cục bộ trong `/static`, đảm bảo hệ thống hiển thị trọn vẹn ngay cả trong môi trường máy chủ nội bộ không có kết nối Internet.
- Xử lý giao dịch an toàn với cơ chế Connection Pooling (`psycopg2.pool`) và Transaction (`BEGIN ... COMMIT / ROLLBACK`), đảm bảo tính nhất quán dữ liệu khi tạo đơn hàng gồm nhiều món ăn.
- Endpoint `/health` cung cấp trạng thái sống còn của ứng dụng và kết nối CSDL, trả về JSON chuẩn RESTful.

## 3.3. Tích hợp Công cụ Quản trị CSDL pgAdmin 4
pgAdmin 4 được container hóa trong dịch vụ `restaurant-pgadmin`:
- Hoạt động ổn định trên cùng mạng `backend-net` với PostgreSQL.
- Được Nginx Reverse Proxy điều hướng qua đường dẫn `https://<IP>/pgadmin/`.
- Tài khoản quản trị khởi tạo tự động theo biến môi trường:
  - Email: `dtc245200862@ictu.edu.vn`
  - Mật khẩu: `StrongPass#2026`
- Hỗ trợ trực quan hóa bảng biểu, thực thi truy vấn SQL, sao lưu và phục hồi dữ liệu nhà hàng nhanh chóng.

## 3.4. Cơ chế Kiểm tra Sức khỏe (Healthcheck) và Tự phục hồi
Container CSDL PostgreSQL được cấu hình chỉ thị `healthcheck`:
```yaml
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U restaurant_user -d restaurant_db"]
  interval: 5s
  timeout: 5s
  retries: 5
```
Dịch vụ Web App thiết lập phụ thuộc điều kiện:
```yaml
depends_on:
  db:
    condition: service_healthy
```
Điều này đảm bảo ứng dụng Web chỉ khởi động khi cơ sở dữ liệu đã hoàn toàn sẵn sàng nhận kết nối, loại bỏ triệt để lỗi "Database connection refused" thường gặp khi khởi động đồng loạt.

---

# CHƯƠNG 4: TRIỂN KHAI NGINX REVERSE PROXY VÀ BẢO MẬT SSL/HTTPS (1.5 ĐIỂM)

## 4.1. Vai trò của Nginx Reverse Proxy làm Cổng vào Duy nhất
Nginx đóng vai trò là "người gác cổng" (Edge Gateway/Reverse Proxy) duy nhất của hệ thống:
- Chiếm dụng hai cổng chuẩn Internet: Port 80 (HTTP) và Port 443 (HTTPS).
- Người dùng từ bên ngoài không thể truy cập trực tiếp vào các cổng nội bộ của Web (5000), pgAdmin (80), hay PostgreSQL (5432).
- Mọi kết nối đều phải đi qua Nginx để kiểm tra tính hợp lệ, mã hóa SSL và bảo vệ an ninh.

## 4.2. Khởi tạo và Cấu hình Chứng chỉ Bảo mật SSL Tự ký (HTTPS)
Chứng chỉ bảo mật SSL (X.509) được tạo tự động với thuật toán mã hóa RSA 2048-bit, thời hạn 365 ngày:
```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048   -keyout nginx/ssl/server.key   -out nginx/ssl/server.crt   -subj "/C=VN/ST=ThaiNguyen/L=ThaiNguyen/O=ICTU/OU=CNTT/CN=localhost"
```
Nginx được cấu hình sử dụng các giao thức mã hóa an toàn nhất hiện nay là **TLSv1.2** và **TLSv1.3**, loại bỏ các giao thức cũ tiềm ẩn lỗ hổng như SSLv3, TLSv1.0:
```nginx
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers HIGH:!aNULL:!MD5;
```

## 4.3. Chuyển hướng HTTP sang HTTPS Tự động (301 Permanent Redirect)
Khi người dùng truy cập bằng giao thức không an toàn qua cổng 80 (`http://`), Nginx sẽ tự động trả về mã chuyển hướng vĩnh viễn 301 chuyển sang cổng 443 (`https://`):
```nginx
server {
    listen 80;
    server_name localhost;
    return 301 https://$host$request_uri;
}
```

## 4.4. Cấu hình Security Headers Chống Tấn công Web Phổ biến
Nginx được thiết lập các tiêu đề HTTP bảo mật nâng cao nhằm ngăn chặn các kỹ thuật tấn công phổ biến:
```nginx
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
add_header Content-Security-Policy "default-src 'self' https: 'unsafe-inline' 'unsafe-eval'; img-src 'self' data: https:;" always;
```
- **X-Frame-Options (SAMEORIGIN):** Chống tấn công Clickjacking, ngăn chặn kẻ xấu nhúng website vào iframe của trang lừa đảo.
- **X-Content-Type-Options (nosniff):** Ngăn chặn trình duyệt đoán sai định dạng MIME (MIME-sniffing exploit).
- **Strict-Transport-Security (HSTS):** Bắt buộc trình duyệt luôn giao tiếp qua HTTPS trong vòng 1 năm.
- **Content-Security-Policy (CSP):** Kiểm soát nguồn gốc tải tài nguyên (scripts, images, styles), chống tấn công Cross-Site Scripting (XSS).

## 4.5. Cơ chế Giới hạn Tần suất Truy cập (Rate Limiting)
Nginx thiết lập vùng kiểm soát tần suất truy cập dựa trên địa chỉ IP (`$binary_remote_addr`):
```nginx
limit_req_zone $binary_remote_addr zone=one:10m rate=10r/s;
...
location / {
    limit_req zone=one burst=20 nodelay;
    proxy_pass http://restaurant_web;
    ...
}
```
Mỗi địa chỉ IP chỉ được phép gửi tối đa 10 request/giây (cho phép cụm tối đa 20 request). Khi vượt quá ngưỡng này, Nginx sẽ từ chối với mã lỗi HTTP 503, giúp bảo vệ Web App khỏi các đợt càn quét brute-force hoặc tấn công từ chối dịch vụ.

---

# CHƯƠNG 5: HỆ THỐNG GIÁM SÁT THỜI GIAN THỰC PROMETHEUS & GRAFANA (1.5 ĐIỂM)

## 5.1. Kiến trúc Hệ thống Giám sát Metrics Thời gian thực
Hệ thống áp dụng mô hình giám sát chủ động (Pull-based Model) của **Prometheus**:
- Prometheus đóng vai trò trung tâm, định kỳ 5 giây (`scrape_interval: 5s`) gửi HTTP request đến các endpoint `/metrics` của từng thành phần để lấy thông số.
- Các thông số được lưu dưới dạng chuỗi thời gian (Time-series data) kèm nhãn (Labels) giúp truy vấn linh hoạt.

## 5.2. Thu thập Metrics Nghiệp vụ từ Ứng dụng Web (/metrics)
Ứng dụng Python Flask được tích hợp thư viện `prometheus-client`, cung cấp các chỉ số đo lường tùy biến:
- `restaurant_http_requests_total`: Bộ đếm (Counter) tổng lượt request phân loại theo phương thức HTTP (`GET`, `POST`), route (`/`, `/tables`, `/menu`, `/orders`) và mã phản hồi (`200`, `404`, `500`).
- `restaurant_http_request_duration_seconds`: Biểu đồ phân bổ (Histogram) đo thời gian xử lý phản hồi của từng request (độ trễ latency).
- Các chỉ số mặc định của hệ thống: Mức tiêu thụ bộ nhớ RAM (Process resident memory), tỷ lệ chiếm dụng CPU, số lượng luồng thực thi (threads).

## 5.3. Giám sát Container (cAdvisor) và Hệ điều hành (Node Exporter)
Bên cạnh ứng dụng web, hệ thống triển khai hai exporter chuyên dụng:
* **cAdvisor (Container Advisor):** Công cụ của Google thu thập trực tiếp từ nhân Linux (`/var/run`, `/sys`, `/var/lib/docker`) các chỉ số phần cứng của từng container độc lập: CPU usage per container, Memory usage, Network I/O, Filesystem I/O.
* **Node Exporter:** Đo lường tải phần cứng tổng thể của máy chủ chủ nhà: Tải CPU đa nhân, dung lượng RAM khả dụng, tình trạng ổ đĩa, lưu lượng mạng qua card mạng ảo `ens33`/`eth0`.

Trạng thái hoạt động kiểm tra thực tế: Cả 4 targets (`cadvisor`, `node-exporter`, `prometheus`, `restaurant-web`) đều đạt trạng thái **`UP` 100%**.

## 5.4. Thiết lập Dashboard Hiển thị Trực quan trên Grafana
Grafana được liên kết tự động với Prometheus thông qua cơ chế **Datasource Provisioning** (`grafana/provisioning/datasources/datasources.yml`), không cần cấu hình thủ công qua giao diện:
- Địa chỉ truy cập: `http://localhost:3000` (hoặc `http://192.168.75.130:3000`)
- Tài khoản: `admin` / `StrongPass#2026`
- Trực quan hóa các bảng điều khiển thời gian thực:
  - Biểu đồ biến thiên Request Per Second (RPS) của nhà hàng.
  - Tỷ lệ lỗi HTTP 4xx, 5xx.
  - Tỷ lệ CPU/RAM của 10 Docker Containers.

---

# CHƯƠNG 6: HỆ THỐNG THU THẬP LOG TẬP TRUNG LOKI & PROMTAIL (1.5 ĐIỂM)

## 6.1. Kiến trúc Hệ thống Quản trị Log Tập trung Loki + Promtail
Khác với mô hình ELK Stack truyền thống nặng nề, hệ thống lựa chọn giải pháp **Grafana Loki**:
- Loki được mệnh danh là "Prometheus dành cho Logs": chỉ lập chỉ mục (index) các nhãn (metadata labels) thay vì lập chỉ mục toàn văn bản (full-text index), giúp tiết kiệm đến 80% bộ nhớ RAM và tài nguyên ổ cứng.
- **Promtail** đóng vai trò là Log Shipper: chạy nền, đọc các tệp log dạng JSON do Docker Daemon sinh ra tại `/var/lib/docker/containers/*/*-json.log`, gắn nhãn nhận dạng rồi đẩy (Push) về Loki qua cổng 3100.

## 6.2. Cấu hình Structured JSON Logging cho Ứng dụng Web
Mọi hành vi trong ứng dụng web đều được định dạng dạng cấu trúc JSON thông qua thư viện `python-json-logger`:
```json
{
  "asctime": "2026-10-11 20:53:25",
  "levelname": "INFO",
  "name": "restaurant-app",
  "message": "HTTP Access Log",
  "method": "GET",
  "path": "/",
  "status": 200,
  "duration_ms": 12.45,
  "remote_ip": "192.168.75.1",
  "student_id": "DTC245200862"
}
```
Nhờ định dạng JSON, Promtail và Loki có thể bóc tách từng trường dữ liệu (`status`, `duration_ms`, `method`) để lọc và phân tích chính xác tuyệt đối.

## 6.3. Cấu hình Promtail Tự động Thu thập Log Container Docker
Trong tệp `promtail/promtail-config.yml`, Promtail được cấu hình:
```yaml
server:
  http_listen_port: 9080
clients:
  - url: http://loki:3100/loki/api/v1/push
scrape_configs:
  - job_name: docker
    static_configs:
      - targets: [localhost]
        labels:
          job: docker-containers
          __path__: /var/lib/docker/containers/*/*-json.log
```
Container Promtail được cấp quyền đọc tệp log của Docker (`/var/lib/docker/containers:ro`) và Docker Socket (`/var/run/docker.sock:ro`).

## 6.4. Thực hành và Minh chứng 03 Câu truy vấn LogQL Thực tế
Tại giao diện Grafana > **Explore** > Chọn **Loki Datasource**, thực hiện 03 câu truy vấn LogQL tiêu biểu:

### Truy vấn 1: Xem toàn bộ luồng Log của ứng dụng Web Quản lý Nhà hàng
```logql
{job="docker-containers"} |= "restaurant-web"
```
*Ý nghĩa:* Lọc toàn bộ các dòng nhật ký được phát sinh từ dịch vụ web, giúp quản trị viên nắm bắt luồng hoạt động tổng thể.

### Truy vấn 2: Phân tích các Request thành công (HTTP 200) sử dụng bộ bóc tách JSON
```logql
{job="docker-containers"} |= "HTTP Access Log" | json | status == 200
```
*Ý nghĩa:* Sử dụng tính năng trích xuất trường `| json`, lọc ra các bản ghi truy cập có mã trạng thái HTTP 200 để tính toán lưu lượng giao dịch hợp lệ.

### Truy vấn 3: Truy vết lỗi và cảnh báo bất thường trong toàn hệ thống
```logql
{job="docker-containers"} |= "error" or "ERROR" or "failed" or "Exception"
```
*Ý nghĩa:* Giúp đội ngũ vận hành phát hiện ngay các sự cố phát sinh (ví dụ: mất kết nối cơ sở dữ liệu, lỗi cú pháp truy vấn, lỗi phân quyền).

---

# CHƯƠNG 7: TĂNG CƯỜNG BẢO MẬT HỆ THỐNG (SYSTEM HARDENING) (1.5 ĐIỂM)

Nhằm đáp ứng tiêu chí bảo mật khắt khe của học phần, nhóm đã áp dụng đồng bộ **05 biện pháp Hardening toàn diện**:

## 7.1. Chạy Container với Người dùng Đặc quyền thấp (Non-root User)
Theo mặc định, Docker chạy tiến trình bên trong container với quyền `root` (UID: 0). Nếu ứng dụng bị chiếm quyền qua lỗ hổng RCE, tin tặc có thể leo thang đặc quyền ra máy chủ vật lý.
*Giải pháp:* Trong `app/Dockerfile`, nhóm đã tạo riêng một nhóm và tài khoản người dùng không đặc quyền:
```dockerfile
RUN addgroup -g 1001 appgroup &&     adduser -u 1001 -G appgroup -s /bin/sh -D appuser
...
USER appuser
```
Tiến trình Gunicorn của ứng dụng chạy hoàn toàn dưới danh nghĩa `appuser` (UID: 1001), triệt tiêu nguy cơ chiếm quyền root máy chủ.

## 7.2. Cô lập Mạng 3 Tầng (Multi-tier Network Isolation)
Hệ thống không dùng mạng bridge phẳng mà phân chia làm 3 phân vùng mạng Docker riêng biệt:
- `frontend-net`: Vùng công cộng tiếp nhận Internet.
- `backend-net`: Vùng lưu trữ dữ liệu tuyệt mật. Container `restaurant-db` chỉ cắm vào mạng này và **không khai báo mục `ports`** để không xuất cổng 5432 ra ngoài máy chủ thật.
- `monitoring-net`: Vùng giám sát vận hành tách biệt.

## 7.3. Tước bỏ Linux Capabilities Nguy hiểm (cap_drop: ALL)
Linux Capabilities chia nhỏ quyền root thành các quyền riêng lẻ. Trong tệp `docker-compose.yml`, dịch vụ Web được cấu hình tước bỏ toàn bộ đặc quyền:
```yaml
cap_drop:
  - ALL
```
Ứng dụng web bị chặn hoàn toàn các thao tác can thiệp hệ điều hành như thay đổi cấu hình mạng (`NET_ADMIN`), tải kernel module (`SYS_MODULE`), hay thay đổi quyền sở hữu tệp (`CHOWN`).

## 7.4. Bảo mật CSDL và Kiểm soát Biến môi trường (.env)
- Toàn bộ thông tin mật khẩu của CSDL, pgAdmin, Grafana đều tuân thủ chính sách mật khẩu phức tạp (chứa chữ hoa, chữ thường, số, ký tự đặc biệt, độ dài trên 12 ký tự: `StrongPass#2026`).
- Mật khẩu được cô lập trong file `.env`, file này được thêm vào `.gitignore` để không bao giờ bị lộ lọt lên kho mã nguồn công khai.

## 7.5. Ẩn Thông tin Phiên bản Máy chủ Web (server_tokens off)
Trong cấu hình Nginx (`nginx/nginx.conf`), nhóm bật cờ:
```nginx
server_tokens off;
```
Khi người dùng hoặc công cụ quét bảo mật gửi request, header HTTP trả về chỉ hiển thị `Server: nginx` mà không kèm theo số phiên bản cụ thể (ví dụ: `nginx/1.25.4`), ngăn chặn kẻ tấn công dò tìm các lỗ hổng bảo mật đã công bố (CVE) theo phiên bản cụ thể.

---

# CHƯƠNG 8: TỔNG THỂ HỆ THỐNG, HƯỚNG DẪN DEMO VÀ KẾT LUẬN (1.0 ĐIỂM)

## 8.1. Hướng dẫn Vận hành 1 Lệnh Duy nhất bằng Docker Compose
Để khởi động toàn bộ 10 thành phần của hệ thống, người chấm chỉ cần đứng tại thư mục gốc và chạy 1 lệnh duy nhất:
```bash
docker compose up -d
```
Để kiểm tra trạng thái tất cả các container đang chạy:
```bash
docker compose ps
```
Để xem log thời gian thực:
```bash
docker compose logs -f
```
Để dừng và giải phóng toàn bộ tài nguyên:
```bash
docker compose down
```

## 8.2. Danh mục Tài khoản và Kịch bản Nghiệm thu (Demo Checklist)

### Bảng Danh mục Tài khoản Hệ thống:
| Phân hệ / Dịch vụ | Địa chỉ truy cập | Tài khoản đăng nhập | Mật khẩu | Vai trò |
| :--- | :--- | :--- | :--- | :--- |
| **Giao diện Khách hàng** | `https://192.168.75.130/customer/menu` | `sinhvien` | `123456789` | Khách xem menu, đặt món, đánh giá |
| **Giao diện Nhân viên** | `https://192.168.75.130/staff/orders` | `nhanvien` | `123456789` | Tiếp nhận đơn, cập nhật trạng thái |
| **Giao diện Quản trị viên** | `https://192.168.75.130/admin/dashboard` | `admin` | `123456789` | Quản trị tài chính, báo cáo, tài khoản |
| **Quản trị CSDL pgAdmin** | `https://192.168.75.130/pgadmin/` | `dtc245200862@ictu.edu.vn` | `StrongPass#2026` | Quản trị 8 bảng PostgreSQL |
| **Giám sát Grafana** | `http://192.168.75.130:3000` | `admin` | `StrongPass#2026` | Xem Dashboard Metrics & Loki Logs |
| **Giám sát Prometheus** | `http://192.168.75.130:9090` | *(Không cần mật khẩu)* | *(Không cần)* | Xem trạng thái 4 Targets Metrics |

### Kịch bản Nghiệm thu Chức năng (Demo Checklist):
| STT | Thành phần kiểm thử | Thao tác thực hiện | Kết quả mong đợi | Đánh giá |
| :---: | :--- | :--- | :--- | :---: |
| 1 | **Nginx Reverse Proxy & SSL** | Truy cập `http://192.168.75.130/` (Port 80) | Tự động chuyển hướng 301 sang `https://...` (Port 443), hiển thị chứng chỉ SSL an toàn | **ĐẠT** |
| 2 | **Đăng nhập & Phân quyền (RBAC)** | Đăng nhập tài khoản `admin`, `nhanvien`, `sinhvien` | Điều hướng chính xác vào từng phân hệ chuyên biệt | **ĐẠT** |
| 3 | **Khách hàng Đặt món** | Vào `/customer/menu`, chọn món, bấm "Đặt món này" | Nút bấm nhỏ gọn dạng pill, giá tiền vừa vặn, đơn gửi tức thì vào hệ thống | **ĐẠT** |
| 4 | **Nhân viên Quản lý Đơn hàng** | Vào `/staff/orders`, kiểm tra đơn mới | Cột "Món đã gọi" hiển thị đầy đủ tên món và số lượng, không bị lỗi mã hệ thống | **ĐẠT** |
| 5 | **Admin Quản trị Tài chính** | Vào `/admin/dashboard` | Hiển thị biểu đồ doanh thu, tính lợi nhuận ròng (Doanh thu - Chi phí) | **ĐẠT** |
| 6 | **Quản trị CSDL pgAdmin** | Truy cập `https://.../pgadmin/` | Quản trị trọn vẹn 8 bảng CSDL PostgreSQL 16 | **ĐẠT** |
| 7 | **Giám sát Prometheus** | Truy cập `http://192.168.75.130:9090/targets` | Cả 4 targets (`web`, `cadvisor`, `node-exporter`, `prometheus`) đều báo `UP` | **ĐẠT** |
| 8 | **Grafana Dashboard** | Truy cập `http://192.168.75.130:3000` | Tự động nhận diện Data Source Prometheus & Loki, đồ thị hiển thị realtime | **ĐẠT** |
| 9 | **Truy vấn LogQL Loki** | Vào Grafana Explore, chạy query `{job="docker-containers"}` | Toàn bộ log của web app và Nginx hiển thị theo thời gian thực | **ĐẠT** |
| 10 | **Kiểm tra Hardening** | Kiểm tra quyền bên trong container web | Chạy lệnh `id` trong container web hiển thị `uid=1001(appuser)` (Non-root) | **ĐẠT** |

## 8.3. Bảng Đối chiếu Kết quả với 7 Tiêu chí Đánh giá của Học phần

| Tiêu chí đánh giá | Điểm tối đa | Hiện trạng hoàn thành của Dự án | Tự đánh giá |
| :--- | :---: | :--- | :---: |
| **1. Quản lý mã nguồn trên GitHub** | **1.5** | Repository đầy đủ, tài khoản đặt tên theo MSV `dtc245200862-dot`, các commit mốc rõ ràng có ý nghĩa, tệp README.md hướng dẫn chi tiết. | **1.5 / 1.5** |
| **2. Triển khai ứng dụng + Database** | **1.5** | Website Quản lý Nhà hàng / Order hoàn chỉnh với 3 phân hệ, CSDL PostgreSQL 16 gồm 8 bảng kết nối ổn định, pgAdmin hoạt động hoàn hảo. | **1.5 / 1.5** |
| **3. Nginx Reverse Proxy** | **1.5** | Cấu hình proxy chuẩn xác, HTTPS tự ký mã hóa TLS 1.2/1.3, đầy đủ Security Headers (HSTS, CSP, X-Frame-Options), Rate Limiting. | **1.5 / 1.5** |
| **4. Hệ thống giám sát (Prometheus + Grafana)** | **1.5** | Prometheus cào metrics web (/metrics), cAdvisor, Node Exporter; Grafana tự nạp Datasource và trực quan hóa trực tiếp. | **1.5 / 1.5** |
| **5. Hệ thống log tập trung (Loki)** | **1.5** | Loki + Promtail hoạt động ổn định, log dạng cấu trúc JSON, thực hiện thành công 03 câu truy vấn LogQL chuyên sâu. | **1.5 / 1.5** |
| **6. Hardening hệ thống** | **1.5** | Áp dụng 05 giải pháp: Non-root container (appuser 1001), Network isolation 3 tầng, Dropping Linux capabilities, Mật khẩu mạnh qua .env, Ẩn server tokens. | **1.5 / 1.5** |
| **7. Tổng thể & Trình bày** | **1.0** | Toàn bộ hệ thống chạy bằng 1 file `docker-compose.yml`, báo cáo tổng hợp chi tiết chuẩn format ICTU, kịch bản demo rõ ràng. | **1.0 / 1.0** |
| **TỔNG ĐIỂM** | **10.0** | **Hệ thống hoàn thiện 100% các yêu cầu kỹ thuật và nghiệp vụ** | **10.0 / 10.0** |

## 8.4. Kết luận và Hướng phát triển Đề tài
Hệ thống **Quản lý Nhà hàng & Đặt món (Order) - Đề 12** đã được triển khai thành công, đáp ứng đầy đủ và vượt mức các tiêu chuẩn kỹ thuật của học phần Triển khai và Quản trị Hệ thống Phần mềm. Dự án chứng minh khả năng áp dụng linh hoạt các công nghệ container hóa hiện đại trong việc xây dựng một hạ tầng phần mềm an toàn, có khả năng tự phục hồi, giám sát chủ động và truy vết sự cố nhanh chóng.

*Hướng phát triển trong tương lai:*
- Mở rộng kiến trúc sang cụm điều phối container Kubernetes (K8s) với cơ chế tự động mở rộng (Horizontal Pod Autoscaling - HPA).
- Tích hợp pipeline CI/CD tự động bằng GitHub Actions để tự động kiểm thử và triển khai khi có commit mới.
- Bổ sung hệ thống cảnh báo tức thời qua Telegram Bot / Email thông qua Prometheus Alertmanager khi có sự cố hạ tầng.

---
*Thái Nguyên, năm 2026*  
**Sinh viên thực hiện:**  
**Hồ Quang Huy (DTC245200862)**
