**TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN VÀ TRUYỀN THÔNG**

KHOA CÔNG NGHỆ THÔNG TIN

**Báo cáo Thực Hành**

**MÔN HỌC: TRIỂN KHAI VÀ QUẢN TRỊ HỆ THỐNG**

**ĐỀ TÀI:**

**HỆ THỐNG QUẢN LÝ NHÀ HÀNG & ĐẶT MÓN (ORDER)**

Giảng viên hướng dẫn: TS. Lê Khánh Dương

Sinh viên thực hiện:   Hồ Quang Huy - DTC245200862

Thái Nguyên, năm 2026


# CHƯƠNG 1. TỔNG QUAN ĐỀ TÀI VÀ KIẾN TRÚC HỆ THỐNG


## 1.1. Bối cảnh và mục tiêu

Đề tài 12 yêu cầu xây dựng website Quản lý Nhà hàng & Đặt món (Order), có khả năng quản lý danh mục món ăn, bàn ăn, tiếp nhận và xử lý đơn đặt món theo thời gian thực. Cơ sở dữ liệu sử dụng là PostgreSQL 16 và công cụ quản trị giao diện là pgAdmin 4. Theo yêu cầu chung của học phần Triển khai và Quản trị Hệ thống Phần mềm tại Trường Đại học Công nghệ Thông tin và Truyền thông (ICTU), hệ thống còn ứng dụng toàn diện Docker Compose, Nginx reverse proxy với chứng chỉ bảo mật SSL/HTTPS, hệ thống giám sát thời gian thực Prometheus và Grafana, hệ thống thu thập log tập trung Loki và Promtail, cùng các giải pháp hardening gia cố an ninh hạ tầng.

Mục tiêu không chỉ là làm cho website truy cập được mà còn thực hành chuyên sâu việc tổ chức dịch vụ, cấu hình mạng cô lập nhiều tầng, quản lý khối lưu trữ dữ liệu bền vững, theo dõi hiệu năng hệ thống qua metrics và truy vết sự cố qua log tập trung. Việc tách dịch vụ thành các container độc lập giúp từng thành phần có môi trường thực thi riêng biệt, giảm thiểu xung đột phần mềm và được điều phối đồng bộ, tự động hóa thông qua Docker Compose.


## 1.2. Phạm vi chức năng

Phạm vi triển khai gồm ứng dụng web Quản lý Nhà hàng (phát triển trên nền tảng Python Flask và Gunicorn), hệ quản trị CSDL PostgreSQL 16, công cụ quản trị pgAdmin 4, Nginx reverse proxy, Prometheus, Grafana, Loki và Promtail. Hệ thống cung cấp 3 phân hệ giao diện chuyên biệt phục vụ các nhóm người dùng khác nhau:

- Phân hệ Khách hàng (/customer): Xem thực đơn được phân theo 4 danh mục ẩm thực, chọn bàn ăn hoặc mang về, tạo đơn đặt món tức thời, theo dõi tiến trình chế biến và gửi đánh giá chất lượng món ăn (1-5 sao).
- Phân hệ Nhân viên Phục vụ (/staff): Bảng điều khiển tiếp nhận đơn đặt món thời gian thực, xem chi tiết tên món và số lượng đã gọi, cập nhật trạng thái chế biến (Chờ xử lý -> Đang nấu -> Đã lên món -> Hoàn tất), kiểm soát tồn kho món ăn và theo dõi sơ đồ bàn ăn.
- Phân hệ Quản trị viên (/admin): Báo cáo tài chính doanh thu, chi phí nhập nguyên vật liệu, tính toán lợi nhuận ròng, quản lý hóa đơn nhập kho và quản lý phân quyền tài khoản người dùng.
Các metrics ứng dụng được tích hợp và kiểm tra định kỳ bao gồm restaurant_http_requests_total (tổng lượt request phân loại theo route, method, status code), restaurant_http_request_duration_seconds (thời gian phản hồi request), cùng các chỉ số tài nguyên do cAdvisor và Node Exporter thu thập. Các metrics này cung cấp góc nhìn toàn diện về độ ổn định, tải hệ thống và lưu lượng nghiệp vụ thực tế.


## 1.3. Công nghệ sử dụng


## 1.4. Kiến trúc tổng thể và luồng hoạt động

Người dùng từ trình duyệt truy cập hệ thống qua cổng chuẩn 80 (HTTP) hoặc cổng 443 (HTTPS) trên máy ảo Ubuntu. Máy chủ Nginx Reverse Proxy làm chốt chặn duy nhất tại tầng biên (Edge Gateway), tiếp nhận yêu cầu, tự động chuyển hướng vĩnh viễn (301 Permanent Redirect) các truy cập HTTP sang HTTPS, kiểm tra các tiêu đề bảo mật (Security Headers) và giới hạn tần suất gửi yêu cầu (Rate Limiting).

Sau khi giải mã SSL, Nginx chuyển tiếp request vào ứng dụng web nội bộ (restaurant-web) qua mạng frontend-net. Ứng dụng web giao tiếp với cơ sở dữ liệu PostgreSQL (restaurant-db) thông qua mạng backend-net hoàn toàn cô lập, không để lộ cổng 5432 ra ngoài Internet. Giao diện pgAdmin 4 được Nginx ánh xạ an toàn qua đường dẫn /pgadmin/.

Tại phân vùng giám sát (monitoring-net), Prometheus định kỳ 5 giây cào metrics từ ứng dụng web (/metrics), cAdvisor (cổng 8080) và Node Exporter (cổng 9100). Grafana kết nối vào Prometheus và Loki thông qua Datasource Provisioning tự động tại cổng 3000. Promtail đóng vai trò Log Shipper, đọc các tệp log JSON của container từ Docker daemon rồi gửi về Loki qua cổng 3100.


*Hình 1: Cấu trúc thư mục dự án*


# CHƯƠNG 2. TRIỂN KHAI ỨNG DỤNG VÀ CÁC DỊCH VỤ


## 2.1. Tổ chức mã nguồn và Docker Compose

Dự án được tổ chức khoa học theo từng nhóm chức năng, gồm mã nguồn ứng dụng web (app/), tệp kịch bản khởi tạo CSDL (init-db/), cấu hình Nginx (nginx/), cấu hình Prometheus (prometheus/), provisioning Grafana (grafana/), cấu hình Loki (loki/), cấu hình Promtail (promtail/) và tệp điều phối trung tâm docker-compose.yml. Cách phân chia module này giúp cô lập hoàn toàn mã nguồn nghiệp vụ khỏi các cấu hình hạ tầng, tạo sự mạch lạc trong quá trình phát triển và bảo trì.

Tệp docker-compose.yml khai báo rõ ràng 10 dịch vụ, image sử dụng, cổng kết nối, volume dữ liệu bền vững (postgres_data, grafana_data, loki_data), 3 mạng cô lập (frontend-net, backend-net, monitoring-net) và quan hệ phụ thuộc điều kiện (depends_on với healthcheck). Sau khi khởi chạy, trạng thái các container được kiểm tra bằng lệnh docker compose ps. Hệ thống đảm bảo tính toàn vẹn dữ liệu, các volume lưu trữ không bị xóa khi bảo trì hoặc khởi động lại dịch vụ.


*Hình 2: Trạng thái container*


## 2.2. Ứng dụng Quản lý Nhà hàng và PostgreSQL

Ứng dụng web được lập trình bằng Python 3.12 với Flask Framework và Gunicorn WSGI server. Cơ sở dữ liệu restaurant_db trên PostgreSQL 16 được thiết kế chuẩn hóa bậc 3 (3NF) gồm 8 bảng nghiệp vụ chặt chẽ: users (người dùng và vai trò), categories (4 danh mục món ăn nhà hàng), menu_items (danh sách món ăn, giá bán và số lượng tồn kho), tables (sơ đồ bàn ăn và sức chứa), orders (đơn đặt món, khách hàng, bàn ăn và trạng thái), order_items (chi tiết số lượng và đơn giá từng món trong đơn), reviews (đánh giá sao và phản hồi của khách hàng), và inventory_invoices (hóa đơn nhập nguyên liệu phục vụ quản lý chi phí).

Giao diện phân hệ Khách hàng (/customer/menu) hiển thị thực đơn theo 4 nhóm ẩm thực chuẩn mực: Món khai vị & Salad, Món chính thượng hạng, Món nướng & Lẩu đặc biệt, Đồ uống & Tráng miệng. Các nút danh mục được thiết kế dạng pill thanh lịch, thông tin giá tiền được hiển thị rõ ràng, cân đối. Phân hệ Nhân viên (/staff/orders) hiển thị danh sách đơn hàng trực quan, tên các món ăn đã gọi cùng số lượng được tổng hợp chi tiết, không xảy ra hiện tượng xung đột mã hệ thống.


*Hình 03: Giao diện hệ thống Quản lý Nhà hàng - Phân hệ Thực đơn Khách hàng*


*Hình 04: Cơ sở dữ liệu và bảng dữ liệu của hệ thống trên pgAdmin 4*


## 2.3. pgAdmin và Nginx reverse proxy

pgAdmin 4 được container hóa trong dịch vụ restaurant-pgadmin, kết nối trực tiếp với PostgreSQL qua mạng nội bộ backend-net. Công cụ này cung cấp giao diện quản trị cơ sở dữ liệu mạnh mẽ, cho phép theo dõi cấu trúc bảng, thực thi truy vấn SQL, quản lý chỉ mục và sao lưu dữ liệu mà không cần xuất cổng cơ sở dữ liệu ra ngoài Internet.

Máy chủ Nginx đóng vai trò Reverse Proxy làm việc tại cổng 80 và 443. Khi người dùng gửi yêu cầu HTTP thông thường, Nginx tự động chuyển tiếp sang HTTPS thông qua chỉ thị chuyển hướng 301. Toàn bộ phiên truyền thông được mã hóa bằng chứng chỉ SSL tự ký chuẩn TLSv1.2/TLSv1.3. Nginx được thiết lập các tiêu đề HTTP bảo mật nâng cao nhằm ngăn chặn các lỗ hổng web phổ biến: X-Content-Type-Options: nosniff, X-Frame-Options: SAMEORIGIN, X-XSS-Protection: 1; mode=block, Strict-Transport-Security và Content-Security-Policy.


*Hình 05: Giao diện hệ thống Nhà hàng truy cập thông qua Nginx reverse proxy với giao thức HTTPS*


*Hình 6: Kết quả kiểm tra các HTTP response headers được cấu hình trên Nginx*


## 2.4. Quản lý mã nguồn trên GitHub

Toàn bộ mã nguồn ứng dụng và tệp cấu hình hạ tầng DevOps được đồng bộ hóa và lưu trữ tại repository GitHub theo đúng quy chuẩn định danh mã sinh viên: https://github.com/dtc245200862-dot/dtc245200862-restaurant-system.git trên nhánh chính (main). Lịch sử commit được ghi nhận rõ ràng, mạch lạc theo từng mốc phát triển chức năng của học phần.

Tệp .env chứa các biến môi trường nhạy cảm (mật khẩu CSDL, khóa bí mật) được đưa vào .gitignore để tuyệt đối không đưa lên kho lưu trữ công khai. Dự án cung cấp tệp .env.example mẫu với các giá trị định danh minh họa, giúp việc triển khai trên môi trường mới diễn ra an toàn, chính xác và không làm rò rỉ bí mật hệ thống.


*Hình 7: Repository GitHub của hệ thống Quản lý Nhà hàng dtc245200862-restaurant-system*


*Hình 8: Lịch sử commit mã nguồn Repository GitHub*


# CHƯƠNG 3. GIÁM SÁT, TẬP TRUNG LOG VÀ BẢO MẬT


## 3.1. Prometheus và Grafana

Hệ thống áp dụng mô hình giám sát chủ động (Pull-based) của Prometheus. Máy chủ Prometheus được cấu hình định kỳ 5 giây cào chỉ số hoạt động từ 4 đích giám sát (targets) chuyên biệt: ứng dụng web nhà hàng (/metrics), cAdvisor (chỉ số phần cứng của từng Docker container), Node Exporter (chỉ số phần cứng máy chủ Linux) và chính máy chủ Prometheus. Toàn bộ 4 targets đều duy trì trạng thái hoạt động UP 100%.

Grafana được tích hợp làm nền tảng trực quan hóa số liệu thông qua cơ chế nạp tự động Data Source (Provisioning) tại cổng 3000. Dashboard giám sát của hệ thống cung cấp các biểu đồ thời gian thực: tần suất yêu cầu trên giây (RPS), độ trễ phản hồi (latency), tỷ lệ mã trạng thái HTTP 2xx/4xx/5xx, mức tiêu thụ CPU và dung lượng RAM của 10 container.


*Hình 9: Trang Prometheus Targets hiển thị danh sách các mục tiêu giám sát và trạng thái kết nối của hệ thống Nhà hàng*


*Hình 10: Dashboard Grafana hiển thị các chỉ số giám sát của hệ thống Nhà hàng*


## 3.2. Loki, Promtail và truy vấn LogQL

Hệ thống quản trị log tập trung sử dụng giải pháp Grafana Loki và Promtail. Khác với ELK Stack tiêu tốn tài nguyên, Loki áp dụng cơ chế chỉ đánh chỉ mục theo nhãn (metadata labels) và lưu trữ log chunks nén, giúp tối ưu hóa hiệu năng máy chủ. Promtail chạy nền dưới quyền hệ thống, đọc trực tiếp các tệp nhật ký JSON do Docker Daemon sinh ra tại /var/lib/docker/containers/*/*-json.log, gắn nhãn nhận diện rồi đẩy dữ liệu về Loki qua giao thức HTTP tại cổng 3100.

Ứng dụng Python Flask được tích hợp thư viện python-json-logger để sinh log dạng cấu trúc (Structured JSON Logging), ghi nhận đầy đủ thời gian (asctime), mức độ (INFO/ERROR), tên dịch vụ, HTTP method, route, status code, thời gian xử lý và mã sinh viên (DTC245200862). Toàn bộ pipeline thu thập log vận hành ổn định, không có lỗi ingestion. Quản trị viên sử dụng ngôn ngữ LogQL trong Grafana Explore để phân tích log với 3 truy vấn tiêu biểu:


*Hình 11: Kiểm tra và giám sát nhật ký hoạt động của hệ thống bằng Grafana và Loki*


*Hình 12: Truy vấn lọc từ khóa nhật ký hoạt động ứng dụng bằng LogQL trên Grafana*


## 3.3. Các biện pháp hardening

Nhằm bảo vệ hạ tầng máy chủ và giảm thiểu tối đa bề mặt tấn công, hệ thống đã triển khai đồng bộ 05 biện pháp gia cố an ninh (Hardening) thực tế:


### 1. Network Isolation: Hệ thống được phân tách thành 03 mạng bridge riêng biệt (frontend-net, backend-net, monitoring-net). Container cơ sở dữ liệu PostgreSQL chỉ nằm trong mạng backend-net và không khai báo cổng kết nối (ports) ra ngoài, triệt tiêu nguy cơ bị quét cổng hoặc tấn công khai thác CSDL từ Internet.


### 2. Non-root Container: Trong Dockerfile của ứng dụng web, nhóm người dùng appgroup và tài khoản appuser (UID: 1001) được tạo riêng biệt. Tiến trình Gunicorn thực thi hoàn toàn dưới danh nghĩa appuser, ngăn ngừa nguy cơ leo thang đặc quyền root máy chủ nếu ứng dụng bị xâm nhập.


### 3. Tước bỏ Linux Capabilities: Trong docker-compose.yml, dịch vụ web được cấu hình chỉ thị cap_drop: - ALL, tước bỏ toàn bộ đặc quyền hệ điều hành không cần thiết của Linux (thay đổi mạng, chown, nạp module kernel).


### 4. Quản lý Secrets an toàn: Mật khẩu của CSDL, pgAdmin và Grafana đều áp dụng chính sách mật khẩu phức tạp (StrongPass#2026), được lưu trữ trong tệp .env cục bộ và loại trừ khỏi Git qua .gitignore.

5. Ẩn thông tin phiên bản máy chủ: Cấu hình Nginx bật cờ server_tokens off, ngăn chặn việc hiển thị phiên bản phần mềm trong các tiêu đề phản hồi HTTP, làm thất bại các kỹ thuật dò quét lỗ hổng đã công bố (CVE).


*Hình 13: Cấu hình mạng Docker, Non-root và các cổng truy cập của hệ thống Nhà hàng*


# CHƯƠNG 4. KIỂM THỬ, KẾT QUẢ VÀ ĐÁNH GIÁ


## 4.1. Kịch bản kiểm thử

Quá trình kiểm thử được tiến hành toàn diện qua 8 kịch bản (Test Cases) nhằm xác minh tính sẵn sàng của hạ tầng container, tính chính xác của nghiệp vụ ứng dụng, cơ chế mã hóa Nginx SSL, các targets giám sát Prometheus, dashboard Grafana, pipeline log Loki và an toàn mã nguồn trên GitHub.


## 4.2. Kết quả đạt được

Hệ thống Quản lý Nhà hàng & Đặt món (Order) - Đề 12 đã được triển khai hoàn chỉnh 100% trên môi trường máy chủ Ubuntu ảo hóa. Ứng dụng web hoạt động ổn định với 3 phân hệ giao diện chuyên biệt, hỗ trợ đầy đủ quy trình đặt món, quản lý bàn ăn, kiểm soát tồn kho và báo cáo tài chính. Cơ sở dữ liệu PostgreSQL gồm 8 bảng lưu trữ dữ liệu an toàn và bền vững qua Docker Named Volume.

Hạ tầng DevOps được thiết lập bài bản theo chuẩn công nghiệp: Nginx Reverse Proxy bảo vệ an toàn với giao thức HTTPS tự ký và các tiêu đề an ninh; Prometheus cào metrics ổn định với 4 targets UP tuyệt đối; Grafana hiển thị trực quan các biểu đồ hiệu năng; pipeline Loki và Promtail thu thập log tập trung dạng JSON trơn tru; và 05 kỹ thuật Hardening được áp dụng nghiêm ngặt bảo vệ hệ thống khỏi các nguy cơ tấn công leo thang đặc quyền.


## 4.3. Hạn chế và hướng khắc phục

Bên cạnh các kết quả xuất sắc đã đạt được, hệ thống vẫn tồn tại một số điểm có thể tối ưu hóa hơn nữa trong giai đoạn tiếp theo:

- Chứng chỉ SSL hiện tại là chứng chỉ tự ký (Self-signed Certificate), khi truy cập trên trình duyệt ngoài môi trường thực hành sẽ hiển thị cảnh báo bảo mật. Hướng khắc phục: Trong môi trường sản xuất thực tế với tên miền Internet công khai, hệ thống sẽ tích hợp Certbot tự động cấp phát chứng chỉ số miễn phí Let's Encrypt.
- Cơ chế cảnh báo sự cố hạ tầng hiện mới dừng lại ở việc quan sát trên Dashboard Grafana. Hướng khắc phục: Cấu hình thêm Prometheus Alertmanager để gửi thông báo tức thời qua ứng dụng Telegram Bot hoặc Email của đội ngũ quản trị viên khi phát sinh sự cố quá tải CPU, cạn kiệt bộ nhớ hoặc dịch vụ dừng đột ngột.

## 4.4. Đánh giá theo yêu cầu đề tài


# KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

Đề tài 'Hệ thống Quản lý Nhà hàng & Đặt món (Order) - Đề 12' đã giúp sinh viên vận dụng sâu sắc các kiến thức nền tảng và nâng cao của học phần Triển khai và Quản trị Hệ thống Phần mềm. Dự án đã chứng minh khả năng làm chủ các công nghệ container hóa hiện đại thông qua việc đóng gói ứng dụng web đa tầng, chuẩn hóa cơ sở dữ liệu quan hệ PostgreSQL, tích hợp công cụ quản trị trực quan pgAdmin, thiết lập chốt chặn an ninh Nginx Reverse Proxy mã hóa SSL/HTTPS, cấu hình hệ thống giám sát thời gian thực Prometheus/Grafana và xây dựng luồng thu thập log tập trung Loki/Promtail.

Kết quả triển khai thực tế khẳng định rằng việc tách biệt các dịch vụ thành từng container độc lập, phân chia mạng cô lập và loại bỏ các đặc quyền hệ thống không cần thiết đã tạo nên một kiến trúc phần mềm an toàn, có khả năng mở rộng linh hoạt, dễ dàng bảo trì và tự phục hồi khi có sự cố. Kho mã nguồn trên GitHub lưu trữ đầy đủ lịch sử phát triển mạch lạc, minh chứng cho phương pháp làm việc chuẩn chỉ theo quy trình DevOps hiện đại.

Trong tương lai, hệ thống có thể tiếp tục được mở rộng sang mô hình cụm điều phối container Kubernetes (K8s) với cơ chế tự động co giãn tải (Autoscaling), xây dựng pipeline CI/CD tự động bằng GitHub Actions và hoàn thiện hệ thống cảnh báo tức thời qua Alertmanager.
