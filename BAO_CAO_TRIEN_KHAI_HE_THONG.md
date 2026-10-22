TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN VÀ TRUYỀN THÔNG

KHOA CÔNG NGHỆ THÔNG TIN

BÁO CÁO THỰC HÀNH

MÔN HỌC: TRIỂN KHAI VÀ QUẢN TRỊ HỆ THỐNG PHẦN MỀM

ĐỀ TÀI:

HỆ THỐNG QUẢN LÝ NHÀ HÀNG & ĐẶT MÓN (ORDER)

Giảng viên hướng dẫn: TS. Lê Khánh Dương

Sinh viên thực hiện:   Hồ Quang Huy - DTC245200862

Lớp:                   CNTT K23h

Thái Nguyên, năm 2026


# MỤC LỤC


# MỤC LỤC	2


# DANH MỤC THUẬT NGỮ VÀ KHÁI NIỆM KỸ THUẬT	4


# DANH MỤC HÌNH ẢNH MINH CHỨNG	6


# DANH MỤC BẢNG BIỂU	6


# LỜI NÓI ĐẦU	7


# CHƯƠNG 1. TỔNG QUAN ĐỀ TÀI VÀ KIẾN TRÚC HỆ THỐNG	8


## 1.1. Bối cảnh và mục tiêu thực tế của hệ thống quản lý nhà hàng	8


## 1.2. Các nhóm đối tượng sử dụng và phạm vi chức năng	8


## 1.3. Quy trình vận hành thực tế một chu trình phục vụ món ăn	9


## 1.4. Ưu thế nổi bật của hệ thống	10


## 1.5. Bảng tổng hợp các công nghệ nền tảng sử dụng trong hệ thống	10


## 1.6. Mô hình kiến trúc 10 dịch vụ container và luồng giao tiếp	11


# CHƯƠNG 2. CHI TIẾT CÁC THÀNH PHẦN VÀ QUY TRÌNH VẬN HÀNH	13


## 2.1. Cấu trúc thư mục mã nguồn và các tệp cấu hình	13


## 2.2. Khởi động và điều phối toàn bộ 10 dịch vụ bằng Docker Compose	13


## 2.3. Phân hệ Khách hàng: xem thực đơn 4 nhóm ẩm thực và đặt món trực tuyến	14


## 2.4. Phân hệ Nhân viên: tiếp nhận đơn hàng, cập nhật trạng thái chế biến và sơ đồ bàn	15


## 2.5. Phân hệ Quản trị: thống kê doanh thu, chi phí và tự động tính lợi nhuận ròng	15


## 2.6. Thiết kế cơ sở dữ liệu PostgreSQL gồm 8 bảng dữ liệu quan hệ	16


## 2.7. Thiết lập Reverse Proxy Nginx, chứng chỉ SSL và giao thức HTTPS	17


## 2.8. Quản lý mã nguồn dự án trên kho lưu trữ GitHub	17


# CHƯƠNG 3. GIÁM SÁT TÀI NGUYÊN, QUẢN TRỊ NHẬT KÝ VÀ GIA CỐ BẢO MẬT	19


## 3.1. Giám sát tài nguyên máy chủ theo thời gian thực với Prometheus và Grafana	19


## 3.2. Quản trị nhật ký hoạt động tập trung với Loki và Promtail	20


## 3.3. Hướng dẫn tra cứu và phân tích nhật ký bằng ngôn ngữ truy vấn LogQL	20


## 3.4. Năm giải pháp gia cố an ninh hệ thống	21


# CHƯƠNG 4. KỊCH BẢN THỬ NGHIỆM, KẾT QUẢ ĐẠT ĐƯỢC VÀ ĐÁNH GIÁ	23


## 4.1. Kịch bản 10 bước thử nghiệm và nghiệm thu hệ thống	23


## 4.2. Hướng dẫn chi tiết các câu lệnh thực thi trên Terminal máy ảo Ubuntu	24


## 4.3. Hướng dẫn chi tiết các đường dẫn URL và tài khoản để chụp ảnh giao diện	24


## 4.4. Những kết quả thực tế mà hệ thống đã làm được	25


## 4.5. Các hạn chế tồn tại và hướng hoàn thiện trong tương lai	26


## 4.6. Bảng đối chiếu tự đánh giá theo 7 tiêu chí của học phần	26


# KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN	28


# DANH MỤC THUẬT NGỮ VÀ KHÁI NIỆM KỸ THUẬT

Nhằm giúp người đọc dễ dàng tiếp cận và hiểu rõ các công nghệ cốt lõi trong hệ thống, phần này tổng hợp định nghĩa và vai trò thực tế của các thuật ngữ kỹ thuật chính:

- Docker và Container: Công nghệ đóng gói ứng dụng cùng toàn bộ thư viện, môi trường thực thi vào một đơn vị độc lập (container). Nhờ đó, ứng dụng chạy nhất quán trên mọi máy chủ mà không bị lỗi thiếu phụ thuộc hay xung đột phiên bản.
- Docker Compose: Công cụ điều phối và quản lý vòng đời cụm container. Cho phép định nghĩa toàn bộ 10 dịch vụ, cấu hình mạng và ổ đĩa lưu trữ trong một tệp docker-compose.yml duy nhất, khởi động toàn bộ hệ thống bằng một câu lệnh.
- Nginx Reverse Proxy: Máy chủ trung gian đứng trước các dịch vụ backend, chịu trách nhiệm tiếp nhận lưu lượng truy cập từ người dùng, điều hướng yêu cầu đến đúng dịch vụ nội bộ, giải mã chứng chỉ SSL/TLS và ngăn chặn truy cập quá tải.
- SSL/TLS và HTTPS: Giao thức mã hóa đường truyền dữ liệu giữa trình duyệt của người dùng và máy chủ web. Đảm bảo toàn bộ thông tin đăng nhập, thực đơn và đơn đặt món không bị đọc lén hoặc giả mạo trên đường truyền mạng.
- PostgreSQL: Hệ quản trị cơ sở dữ liệu quan hệ mã nguồn mở mạnh mẽ, đảm bảo tính toàn vẹn dữ liệu (chuẩn ACID), lưu trữ an toàn toàn bộ dữ liệu thực đơn, sơ đồ bàn, đơn hàng và hóa đơn tài chính của nhà hàng.
- pgAdmin 4: Giao diện web trực quan phục vụ công tác quản trị cơ sở dữ liệu PostgreSQL, giúp quản trị viên xem cấu trúc bảng, truy vấn dữ liệu và sao lưu mà không cần dùng lệnh dòng lệnh phức tạp.
- Prometheus: Hệ thống giám sát và lưu trữ số liệu (metrics) theo chuỗi thời gian. Định kỳ 5 giây một lần, Prometheus thu thập số liệu tải CPU, bộ nhớ RAM, lưu lượng truy cập từ các dịch vụ trong hệ thống.
- Grafana: Nền tảng trực quan hóa dữ liệu giám sát thành các bảng biểu đồ đồ họa (Dashboards), giúp quản trị viên theo dõi trạng thái sức khỏe máy chủ và hiệu năng ứng dụng theo thời gian thực.
- Loki và Promtail: Bộ đôi giải pháp quản trị nhật ký (log) tập trung. Promtail thu thập log phát sinh từ các container và chuyển về kho lưu trữ Loki để đánh chỉ mục nhãn, hỗ trợ tra cứu nhanh chóng bằng ngôn ngữ LogQL.
- Security Hardening: Tập hợp các giải pháp kỹ thuật nhằm gia cố an ninh cho hệ thống máy chủ và container, bao gồm chạy quyền người dùng thông thường (non-root), cách ly phân vùng mạng, tước bỏ đặc quyền Linux nguy hiểm và ẩn thông tin phiên bản phần mềm.

# DANH MỤC HÌNH ẢNH MINH CHỨNG


*Hình 1: Cấu trúc thư mục dự án	12*


*Hình 2: Trạng thái container hoạt động Up/healthy	14*


*Hình 3: Giao diện hệ thống Quản lý Nhà hàng - Phân hệ Thực đơn Khách hàng	15*


*Hình 4: Cơ sở dữ liệu và bảng dữ liệu của hệ thống trên pgAdmin 4	16*


*Hình 5: Giao diện hệ thống truy cập qua Nginx reverse proxy với HTTPS	17*


*Hình 6: Kết quả kiểm tra các HTTP response headers được cấu hình trên Nginx	17*


*Hình 7: Repository GitHub của hệ thống Quản lý Nhà hàng dtc245200862-restaurant-system	18*


*Hình 8: Lịch sử commit mã nguồn Repository GitHub	18*


*Hình 9: Trang Prometheus Targets hiển thị danh sách 4 mục tiêu giám sát	19*


*Hình 10: Dashboard Grafana hiển thị các chỉ số giám sát của hệ thống	20*


*Hình 11: Kiểm tra và giám sát nhật ký hoạt động của hệ thống bằng Grafana và Loki	21*


*Hình 12: Truy vấn lọc từ khóa nhật ký hoạt động ứng dụng bằng LogQL trên Grafana	21*


*Hình 13: Cấu hình mạng Docker, Non-root và các cổng truy cập của hệ thống	22*


# DANH MỤC BẢNG BIỂU

Bảng 1: Bảng tổng hợp các công nghệ nền tảng sử dụng trong hệ thống	10

Bảng 2: Kịch bản 10 bước thử nghiệm và nghiệm thu hệ thống	23

Bảng 3: Hướng dẫn chi tiết địa chỉ URL và tài khoản để chụp ảnh minh chứng	24

Bảng 4: Bảng đối chiếu tự đánh giá theo 7 tiêu chí đánh giá của học phần	26


# LỜI NÓI ĐẦU

Trong xu thế chuyển đổi số mạnh mẽ hiện nay, việc áp dụng công nghệ thông tin vào quản lý và vận hành hoạt động kinh doanh ẩm thực đã trở thành yêu cầu tất yếu. Mô hình phục vụ truyền thống với các công đoạn ghi phiếu món ăn bằng giấy, trao đổi thủ công giữa nhân viên phục vụ và bếp thường bộc lộ nhiều điểm nghẽn: dễ nhầm lẫn thông tin đơn hàng, thời gian chờ đợi của khách kéo dài trong giờ cao điểm, khó kiểm soát nguyên vật liệu và số liệu tài chính thiếu sự chuẩn xác tức thời.

Đề tài 'Hệ thống Quản lý Nhà hàng & Đặt món (Order) - Đề 12' trong khuôn khổ học phần Triển khai và Quản trị Hệ thống Phần mềm tại Trường Đại học Công nghệ Thông tin và Truyền thông (ICTU) được xây dựng nhằm giải quyết triệt để các bài toán thực tế nêu trên. Đề tài tập trung áp dụng các nguyên lý và kỹ thuật hiện đại của DevOps, bao gồm đóng gói container bằng Docker, điều phối dịch vụ với Docker Compose, bảo mật hạ tầng mạng bằng Nginx Reverse Proxy và SSL/TLS, giám sát tài nguyên máy chủ theo thời gian thực với Prometheus/Grafana, quản trị nhật ký tập trung với Loki/Promtail và áp dụng các biện pháp gia cố an toàn thông tin theo chuẩn công nghiệp.

Bản báo cáo này được biên soạn với cấu trúc chặt chẽ, văn phong kỹ thuật chuẩn mực, diễn giải rõ ràng nguyên lý hoạt động và giá trị thực tế của từng thành phần trong hệ thống. Mọi nội dung phân tích đều gắn liền với cấu hình thực tế và kết quả kiểm thử trên môi trường máy ảo Ubuntu.

Sinh viên xin trân trọng gửi lời cảm ơn sâu sắc nhất tới thầy giáo TS. Lê Khánh Dương cùng toàn thể quý thầy cô Bộ môn Hệ thống Thông tin và Mạng máy tính - Khoa Công nghệ Thông tin đã tận tình hướng dẫn, truyền thụ tri thức chuyên môn và định hướng phương pháp triển khai chuẩn mực giúp sinh viên hoàn thành đề tài này một cách toàn diện.


# CHƯƠNG 1. TỔNG QUAN ĐỀ TÀI VÀ KIẾN TRÚC HỆ THỐNG


## 1.1. Bối cảnh và mục tiêu thực tế của hệ thống quản lý nhà hàng

Trong mô hình nhà hàng ẩm thực truyền thống, quy trình phục vụ trải qua nhiều bước thủ công: khách hàng xem thực đơn trên quyển menu in sẵn, nhân viên phục vụ ghi chép các món ăn vào sổ tay, sau đó chuyển giấy gọi món xuống khu vực bếp. Quy trình này tồn tại nhiều rủi ro: nhân viên ghi nhầm số bàn hoặc tên món, đầu bếp đọc sai số lượng suất ăn, giấy gọi món bị thất lạc trong giờ cao điểm, hoặc món ăn trong bếp đã hết nguyên liệu nhưng nhân viên vẫn ghi cho khách khiến khách phải chờ đợi lâu.

Mục tiêu trọng tâm của đề tài Đề 12 là xây dựng và triển khai một hệ thống phần mềm toàn diện giúp số hóa toàn bộ chu trình vận hành của nhà hàng. Hệ thống liên kết chặt chẽ ba khâu cốt lõi: khách hàng tự xem thực đơn điện tử và đặt món trực tuyến; nhân viên tiếp nhận đơn tức thời và theo dõi chế biến; người quản lý nắm bắt tình hình kinh doanh, doanh thu, chi phí và lợi nhuận ròng tự động theo thời gian thực.

Về mặt hạ tầng kỹ thuật, hệ thống hướng tới mục tiêu tự động hóa tối đa: toàn bộ 10 thành phần dịch vụ được đóng gói độc lập trong các container, khởi động đồng bộ chỉ bằng một câu lệnh, có cơ chế tự phục hồi khi xảy ra sự cố, phân tách mạng nội bộ an toàn và có hệ thống đo lường hiệu năng máy chủ liên tục.


## 1.2. Các nhóm đối tượng sử dụng và phạm vi chức năng

Hệ thống được thiết kế phân quyền chuyên biệt cho ba nhóm đối tượng người dùng chính trong quy trình phục vụ nhà hàng:

- Khách hàng (Thực khách): Truy cập trực tiếp vào hệ thống bằng thiết bị cá nhân (điện thoại thông minh, máy tính bảng) qua trình duyệt web mà không cần cài đặt ứng dụng. Khách hàng xem danh mục thực đơn 4 nhóm ẩm thực chuẩn vị, tra cứu thông tin chi tiết từng món ăn (tên món, hình ảnh, đơn giá, tình trạng còn món), chọn số lượng và số bàn ngồi (hoặc chọn mang về), gửi ghi chú chế biến và bấm xác nhận đặt món. Sau bữa ăn, khách hàng có thể chấm điểm đánh giá từ 1 đến 5 sao và gửi phản hồi chất lượng phục vụ.
- Nhân viên phục vụ và Nhà bếp: Sử dụng phân hệ quản lý đơn đặt món chuyên dụng để tiếp nhận tức thời các đơn hàng mới từ bàn ăn mà không cần di chuyển thủ công. Bảng quản trị hiển thị rõ ràng mã đơn, tên khách, số bàn, tổng tiền và danh sách các món đã gọi. Nhân viên thao tác chuyển đổi trạng thái đơn hàng theo chu trình chế biến: từ 'Chờ xử lý' sang 'Đang nấu', 'Đã lên món' và 'Hoàn tất'. Đồng thời, nhân viên quản lý sơ đồ bàn ăn trực quan để nắm bắt bàn nào đang có khách ngồi và bàn nào còn trống để tiếp đón khách mới.
- Người quản lý và Chủ nhà hàng: Sử dụng phân hệ bảng điều khiển quản trị (Dashboard) để theo dõi tổng thể hoạt động kinh doanh: tổng số lượt khách, tổng doanh thu theo ngày, tổng chi phí nhập nguyên vật liệu từ các hóa đơn lưu trữ, và lợi nhuận ròng thực tế. Quản lý có thể cấu hình danh mục thực đơn, cập nhật giá món ăn, quản lý tài khoản người dùng và xuất dữ liệu báo cáo kinh doanh phục vụ quyết toán định kỳ.

## 1.3. Quy trình vận hành thực tế một chu trình phục vụ món ăn

Một chu trình phục vụ khách hàng tiêu chuẩn trên hệ thống diễn ra mạch lạc qua 5 bước liên hoàn sau:

- Bước 1 - Khách truy cập và chọn món: Khách hàng ngồi tại Bàn 02, mở trình duyệt web trên điện thoại truy cập vào địa chỉ https://192.168.75.130/customer/menu. Hệ thống hiển thị thực đơn 4 danh mục ẩm thực. Khách hàng lựa chọn: 1 suất Bò bít tết sốt tiêu đen Wagyu (150.000 VNĐ), 1 suất Salad rong nho sốt mè rang (45.000 VNĐ) và 1 ly Trà đào cam sả thảo mộc (30.000 VNĐ). Khách nhập số Bàn 02, điền ghi chú 'Bít tết chín vừa, ít đá cho đồ uống' và bấm nút 'Xác nhận đặt món'.
- Bước 2 - Hệ thống ghi nhận và thông báo: Đơn hàng mới được tạo lập trong cơ sở dữ liệu với trạng thái 'pending'. Sơ đồ bàn ăn tự động chuyển trạng thái Bàn 02 từ màu xanh (Bàn trống) sang màu đỏ (Đang phục vụ). Trên màn hình nhân viên phục vụ tại quầy, đơn hàng lập tức xuất hiện ở vị trí đầu tiên của danh sách.
- Bước 3 - Bếp chế biến và cập nhật tiến độ: Nhân viên xác nhận đơn và bấm chuyển trạng thái sang 'preparing' (Đang nấu). Đầu bếp nhìn thông tin hiển thị trên màn hình bếp để tiến hành chế biến đúng món, đúng định lượng và đúng yêu cầu ghi chú của thực khách.
- Bước 4 - Phục vụ món ăn lên bàn: Khi món ăn hoàn thành, nhân viên phục vụ bấm chuyển trạng thái đơn sang 'served' (Đã lên món) và mang thức ăn tới phục vụ khách tại Bàn 02. Trạng thái trên giao diện khách hàng cũng được cập nhật đồng bộ để khách an tâm theo dõi.
- Bước 5 - Thanh toán và giải phóng bàn: Sau khi khách dùng bữa xong và tiến hành thanh toán, nhân viên bấm 'completed' (Hoàn tất đơn hàng). Hệ thống tự động ghi nhận doanh thu 225.000 VNĐ vào báo cáo tài chính trong ngày và đổi trạng thái Bàn 02 trở lại màu xanh, sẵn sàng phục vụ lượt khách tiếp theo.

## 1.4. Ưu thế nổi bật của hệ thống

So với các giải pháp quản lý bán hàng truyền thống hoặc các ứng dụng đóng gói đơn lẻ, hệ thống sở hữu các ưu thế kỹ thuật vượt trội:

- Khả năng tiếp cận linh hoạt: Ứng dụng xây dựng trên nền tảng web responsive tương thích hoàn hảo với mọi thiết bị từ điện thoại iOS, Android đến máy tính bảng và máy tính để bàn mà không yêu cầu cài đặt phần mềm phụ trợ.
- Đóng gói độc lập và di động (Containerization): Toàn bộ mã nguồn backend, cơ sở dữ liệu và các công cụ quản trị được đóng gói thành các image Docker chuẩn mực, đảm bảo khả năng triển khai tức thì trên bất kỳ hệ điều hành Linux hoặc môi trường đám mây nào.
- Tự động hóa vận hành 100%: Quy trình khởi động, gắn ổ đĩa dữ liệu bền vững và thiết lập phân vùng mạng nội bộ được tự động hóa hoàn toàn thông qua Docker Compose chỉ với một câu lệnh duy nhất.
- An toàn thông tin nhiều lớp: Triển khai Reverse Proxy Nginx đóng vai trò điểm tiếp nhận duy nhất, mã hóa toàn diện dữ liệu đường truyền bằng giao thức HTTPS với chứng chỉ SSL, cấu hình đầy đủ các tiêu đề an ninh HTTP và kiểm soát tần suất truy cập chống tấn công từ chối dịch vụ.
- Khả năng quan sát toàn diện (Full Observability): Tích hợp hoàn chỉnh hệ thống thu thập số liệu giám sát phần cứng theo thời gian thực (Prometheus/Grafana) kết hợp hệ thống quản trị nhật ký hoạt động có cấu trúc tập trung (Loki/Promtail).

## 1.5. Bảng tổng hợp các công nghệ nền tảng sử dụng trong hệ thống

Dưới đây là bảng tổng hợp các công nghệ chính được tích hợp trong kiến trúc hệ thống, kèm theo vai trò kỹ thuật và ý nghĩa triển khai thực tế:


## 1.6. Mô hình kiến trúc 10 dịch vụ container và luồng giao tiếp

Hệ thống được thiết kế theo kiến trúc Microservices phân rã thành 10 dịch vụ container độc lập, phối hợp đồng bộ thông qua 3 phân vùng mạng nội bộ chuyên biệt:

- 1. Dịch vụ ứng dụng web (restaurant-web): Ứng dụng backend viết bằng Python Flask, chạy trên cổng nội bộ 5000, đảm nhận toàn bộ logic hiển thị giao diện, tiếp nhận đơn đặt món, kết nối cơ sở dữ liệu và ghi nhật ký có cấu trúc JSON.
- 2. Dịch vụ cơ sở dữ liệu (restaurant-db): Chạy PostgreSQL phiên bản 16 trên cổng 5432 nội bộ, lưu trữ bền vững toàn bộ dữ liệu của 8 bảng thực thể thông qua volume gắn ngoài postgres_data.
- 3. Dịch vụ quản trị CSDL (restaurant-pgadmin): Công cụ quản trị giao diện web pgAdmin 4, cung cấp giao diện quản lý cơ sở dữ liệu trực quan qua đường dẫn bảo mật /pgadmin/.
- 4. Dịch vụ cổng bảo vệ mạng (restaurant-nginx): Đóng vai trò là Edge Reverse Proxy duy nhất mở cổng công khai (80 và 443), tiếp nhận toàn bộ lưu lượng của người dùng và điều hướng an toàn vào các dịch vụ backend nội bộ.
- 5. Dịch vụ giám sát số liệu (restaurant-prometheus): Máy chủ thu thập dữ liệu chuỗi thời gian, định kỳ gửi yêu cầu scrape 5 giây/lần tới các endpoint giám sát để đo lường tài nguyên hệ thống.
- 6. Dịch vụ bảng điều khiển trực quan (restaurant-grafana): Nền tảng hiển thị đồ thị và biểu đồ phân tích thời gian thực trên cổng 3000, tích hợp sẵn nguồn dữ liệu Prometheus và Loki.
- 7. Dịch vụ giám sát container (restaurant-cadvisor): Thu thập chi tiết số liệu tiêu thụ CPU, dung lượng RAM và băng thông mạng của từng container đang hoạt động trong Docker.
- 8. Dịch vụ giám sát phần cứng máy chủ (restaurant-node-exporter): Thu thập các thông số tài nguyên phần cứng tổng quát của hệ điều hành Linux máy chủ.
- 9. Dịch vụ lưu trữ nhật ký tập trung (restaurant-loki): Kho lưu trữ và quản lý nhật ký hoạt động có cấu trúc, tối ưu hóa dung lượng lưu trữ nhờ cơ chế chỉ đánh chỉ mục theo nhãn (labels).
- 10. Dịch vụ thu thập nhật ký (restaurant-promtail): Agent chạy nền gắn kết trực tiếp với thư mục log của Docker daemon, liên tục đọc và đẩy dữ liệu log mới nhất về kho lưu trữ Loki.

*Hình 1: Cấu trúc thư mục dự án*


# CHƯƠNG 2. CHI TIẾT CÁC THÀNH PHẦN VÀ QUY TRÌNH VẬN HÀNH


## 2.1. Cấu trúc thư mục mã nguồn và các tệp cấu hình

Dự án được tổ chức cấu trúc thư mục theo đúng chuẩn mực phát triển phần mềm và DevOps công nghiệp. Mỗi dịch vụ đều có thư mục riêng biệt chứa các tệp mã nguồn và cấu hình tương ứng:

- Thư mục 'app': Chứa toàn bộ mã nguồn của ứng dụng web Python Flask, bao gồm tệp xử lý chính app.py, thư mục templates chứa các trang giao diện HTML dành cho từng đối tượng người dùng, thư mục static chứa các tệp định dạng CSS, mã JavaScript và biểu tượng giao diện.
- Thư mục 'init-db': Chứa tệp kịch bản SQL khởi tạo sẵn cấu trúc 8 bảng dữ liệu quan hệ và nạp dữ liệu mẫu ban đầu cho danh mục thực đơn và sơ đồ bàn ăn.
- Thư mục 'nginx': Chứa tệp cấu hình nginx.conf định nghĩa quy tắc reverse proxy, cấu hình chuyển hướng cổng 80 sang cổng 443 và cặp khóa chứng chỉ số bảo mật SSL (cert.pem và key.pem).
- Thư mục 'prometheus', 'grafana', 'loki', 'promtail': Chứa các tệp cấu hình tham số hoạt động, quy tắc thu thập số liệu và cấu hình nguồn dữ liệu tự động (provisioning datasources).
- Tệp 'docker-compose.yml': Bản thiết kế tổng thể định nghĩa tham số khởi chạy của 10 dịch vụ, bao gồm ánh xạ cổng, gắn volume lưu trữ bền vững, thiết lập biến môi trường và cô lập phân vùng mạng.

## 2.2. Khởi động và điều phối toàn bộ 10 dịch vụ bằng Docker Compose

Một trong những ưu thế nổi trội của hệ thống là khả năng triển khai tự động hóa cao độ. Thay vì cài đặt thủ công từng dịch vụ và cấu hình mạng phức tạp, người quản trị chỉ cần thực thi một câu lệnh duy nhất trên Terminal:

Quá trình thực thi sẽ tự động khởi tạo 3 mạng nội bộ (frontend-net, backend-net, monitoring-net), tạo các volume lưu trữ bền vững và khởi chạy tuần tự các container theo đúng thứ tự phụ thuộc (depends_on). Cơ chế kiểm tra sức khỏe tự động (Healthcheck) được áp dụng cho container cơ sở dữ liệu PostgreSQL để đảm bảo cơ sở dữ liệu hoàn toàn sẵn sàng trước khi ứng dụng web kết nối.

Để kiểm tra trạng thái hoạt động thực tế của toàn bộ cụm dịch vụ, quản trị viên sử dụng câu lệnh:

Kết quả trả về danh sách đầy đủ 10 container đều đạt trạng thái hoạt động 'Up' hoặc 'Up (healthy)', chứng minh toàn bộ các thành phần trong hệ thống đã vận hành ổn định.


*Hình 2: Trạng thái container hoạt động Up/healthy*


## 2.3. Phân hệ Khách hàng: xem thực đơn 4 nhóm ẩm thực và đặt món trực tuyến

Khi khách hàng truy cập vào đường dẫn /customer/menu, giao diện thực đơn điện tử của nhà hàng được hiển thị tối ưu và trực quan. Danh mục món ăn được phân chia khoa học thành 4 nhóm ẩm thực tiêu chuẩn:

- Nhóm 1 - Món khai vị & Salad: Gồm các món thanh đạm kích thích vị giác như Salad rong nho sốt mè rang (45.000 VNĐ), Khoai tây chiên bơ tỏi Pháp (35.000 VNĐ).
- Nhóm 2 - Món chính thượng hạng: Gồm các món ăn dinh dưỡng cao cấp như Bò bít tết sốt tiêu đen Wagyu (150.000 VNĐ), Cá hồi áp chảo sốt chanh leo (180.000 VNĐ), Gà nướng thảo mộc ngũ vị (120.000 VNĐ).
- Nhóm 3 - Món nướng & Lẩu đặc biệt: Phục vụ các nhóm khách đông người như Set Lẩu Thái Hải Sản Hoàng Gia (350.000 VNĐ).
- Nhóm 4 - Đồ uống & Tráng miệng: Gồm Trà đào cam sả thảo mộc (30.000 VNĐ), Nước ép dưa hấu tươi mát lạnh (25.000 VNĐ).
Các nút bấm chọn danh mục được thiết kế nhỏ gọn dạng viên thuốc (pill badge), kích thước giá tiền được định dạng cân đối, hiển thị rõ ràng bằng tiếng Việt. Khi khách bấm nút 'Đặt món', hộp thoại xác nhận mở ra cho phép chọn số lượng, chọn số bàn ăn và nhập ghi chú gửi tới bếp một cách nhanh chóng.


*Hình 3: Giao diện hệ thống Quản lý Nhà hàng - Phân hệ Thực đơn Khách hàng*


## 2.4. Phân hệ Nhân viên: tiếp nhận đơn hàng, cập nhật trạng thái chế biến và sơ đồ bàn

Tại phân hệ dành riêng cho Nhân viên phục vụ (/staff/orders), hệ thống cung cấp bảng quản trị danh sách đơn hàng được cập nhật tức thì. Mỗi khi có khách hàng đặt món, thông tin đơn hàng mới sẽ xuất hiện ở dòng đầu tiên của bảng điều khiển.

Mỗi bản ghi đơn hàng hiển thị đầy đủ các thông tin then chốt: Mã đơn hàng (#ID), Tên khách hàng, Hình thức phục vụ (Tại bàn số mấy hoặc Mang về), Tổng số tiền thanh toán và chi tiết cột 'Món đã gọi'. Cột 'Món đã gọi' liệt kê chính xác tên món ăn kèm số lượng phần tương ứng (ví dụ: Bò bít tết sốt tiêu đen Wagyu (x1), Salad rong nho sốt mè rang (x1), Trà đào cam sả thảo mộc (x1)), hoàn toàn không bị hiển thị chuỗi mã kỹ thuật khó hiểu.

Nhân viên có thể thao tác bấm nút chuyển trạng thái đơn hàng theo đúng quy trình phục vụ: Chờ xử lý -> Đang nấu -> Đã lên món -> Hoàn tất. Đồng thời, nhân viên có thể chuyển qua phân hệ sơ đồ bàn ăn (/staff/tables) để theo dõi trạng thái các bàn: bàn màu đỏ thể hiện đang có khách ngồi dùng bữa, bàn màu xanh thể hiện bàn trống sẵn sàng đón tiếp khách mới.


## 2.5. Phân hệ Quản trị: thống kê doanh thu, chi phí và tự động tính lợi nhuận ròng

Chủ nhà hàng và cán bộ quản lý được cấp quyền truy cập vào phân hệ Quản trị cấp cao (/admin/dashboard). Tại đây, hệ thống tự động tổng hợp toàn bộ số liệu vận hành thành các chỉ số tài chính rõ ràng:

- Tổng doanh thu: Tổng hợp toàn bộ số tiền thanh toán từ tất cả các đơn hàng đã phục vụ thành công trong ngày.
- Tổng chi phí nhập hàng: Tổng hợp chi phí phát sinh từ các hóa đơn nhập nguyên vật liệu (thịt bò Wagyu, cá hồi, rau củ quả, chi phí vận chuyển) được lưu trữ trong bảng inventory_invoices.
- Lợi nhuận ròng thực tế: Được hệ thống tính toán tự động bằng công thức: Lợi nhuận ròng = Tổng doanh thu bán ra - Tổng chi phí nguyên vật liệu. Chỉ số này cung cấp bức tranh tài chính chính xác cho chủ nhà hàng.
Bên cạnh đó, phân hệ quản trị còn cung cấp các công cụ quản lý danh mục món ăn, cập nhật đơn giá, quản lý tài khoản người dùng và xuất báo cáo tài chính định kỳ.


## 2.6. Thiết kế cơ sở dữ liệu PostgreSQL gồm 8 bảng dữ liệu quan hệ

Cơ sở dữ liệu của hệ thống được xây dựng trên hệ quản trị cơ sở dữ liệu PostgreSQL 16, tuân thủ nghiêm ngặt các quy tắc chuẩn hóa dữ liệu với 8 bảng quan hệ liên kết chặt chẽ:

- 1. Bảng users: Lưu trữ thông tin tài khoản người dùng, mật khẩu đã được mã hóa an toàn, họ tên đầy đủ và vai trò phân quyền (admin: quản trị viên, staff: nhân viên phục vụ, customer: khách hàng).
- 2. Bảng categories: Lưu trữ 4 danh mục ẩm thực chính của thực đơn nhà hàng.
- 3. Bảng menu_items: Lưu trữ danh mục các món ăn, khóa ngoại tham chiếu đến bảng danh mục, đơn giá niêm yết, số lượng tồn kho và trạng thái phục vụ của món.
- 4. Bảng tables: Lưu trữ danh sách các bàn ăn trong nhà hàng từ Bàn 01 đến Bàn 08, sức chứa số người và trạng thái hiện tại (bàn trống, đang có khách, đã đặt trước).
- 5. Bảng orders: Lưu trữ thông tin tổng quát của đơn hàng: mã đơn, mã khách hàng, số bàn ngồi, tổng số tiền, trạng thái đơn và ghi chú của khách.
- 6. Bảng order_items: Lưu trữ thông tin chi tiết từng món ăn trong một đơn hàng, liên kết khóa ngoại với bảng orders và menu_items, ghi rõ số lượng suất và đơn giá tại thời điểm đặt.
- 7. Bảng reviews: Lưu trữ phản hồi đánh giá của khách hàng sau khi dùng bữa, bao gồm số sao đánh giá (từ 1 đến 5 sao) và nội dung bình luận chi tiết.
- 8. Bảng inventory_invoices: Lưu trữ các hóa đơn nhập nguyên vật liệu đầu vào của bếp (nhà cung cấp, ngày nhập, chủng loại nguyên liệu, số lượng và tổng chi phí) phục vụ việc tính toán lợi nhuận ròng.

*Hình 4: Cơ sở dữ liệu và bảng dữ liệu của hệ thống trên pgAdmin 4*


## 2.7. Thiết lập Reverse Proxy Nginx, chứng chỉ SSL và giao thức HTTPS

Máy chủ Nginx được triển khai làm Edge Reverse Proxy tiếp nhận lưu lượng mạng ở lớp ngoài cùng của hệ thống. Nginx được cấu hình mở cổng 80 (HTTP) và cổng 443 (HTTPS), áp dụng cơ chế tự động chuyển hướng toàn bộ lưu lượng HTTP chưa mã hóa sang giao thức HTTPS an toàn thông qua mã phản hồi HTTP 301 Moved Permanently.

Đường truyền dữ liệu được bảo vệ an toàn bằng chứng chỉ số SSL/TLS với thuật toán mã hóa RSA 2048-bit. Quá trình trao đổi dữ liệu giữa trình duyệt của khách hàng và máy chủ được mã hóa toàn diện, ngăn chặn hoàn toàn nguy cơ nghe lén gói tin hoặc đánh cắp thông tin xác thực trên mạng nội bộ.

Ngoài ra, Nginx được tích hợp các tiêu đề phản hồi an ninh nâng cao (Security Response Headers): X-Frame-Options: SAMEORIGIN (chống tấn công Clickjacking), X-Content-Type-Options: nosniff (chống tấn công MIME-sniffing), Content-Security-Policy (kiểm soát nguồn nạp tài nguyên) và cơ chế giới hạn tần suất truy cập Rate Limiting (10 requests/giây) giúp bảo vệ hệ thống trước nguy cơ tấn công từ chối dịch vụ.


*Hình 5: Giao diện hệ thống truy cập qua Nginx reverse proxy với HTTPS*


*Hình 6: Kết quả kiểm tra các HTTP response headers được cấu hình trên Nginx*


## 2.8. Quản lý mã nguồn dự án trên kho lưu trữ GitHub

Toàn bộ mã nguồn, tệp cấu hình và tài liệu hướng dẫn triển khai của dự án được đồng bộ và lưu trữ chính thức trên nền tảng GitHub tại địa chỉ kho lưu trữ: https://github.com/dtc245200862-dot/dtc245200862-restaurant-system.git.

Tên tài khoản GitHub và tên kho lưu trữ đều tuân thủ chính xác theo mã sinh viên của tác giả (dtc245200862). Quá trình xây dựng hệ thống được ghi nhận minh bạch qua các mốc commit lịch sử rõ ràng, phản ánh trung thực từng giai đoạn phát triển: khởi tạo ứng dụng web, cấu hình cơ sở dữ liệu PostgreSQL, thiết lập Nginx SSL, tích hợp hệ thống giám sát Prometheus/Grafana, thiết lập thu thập log Loki/Promtail và gia cố an toàn hệ thống.

Các thông tin bảo mật nhạy cảm (mật khẩu CSDL, khóa bí mật) được tách biệt hoàn toàn vào tệp biến môi trường .env cục bộ và được đưa vào tệp .gitignore để không bao giờ bị đưa lên kho lưu trữ công khai. Dự án cung cấp sẵn tệp mẫu .env.example chuẩn mực giúp người khác dễ dàng cấu hình và chạy thử hệ thống.


*Hình 7: Repository GitHub của hệ thống Quản lý Nhà hàng dtc245200862-restaurant-system*


*Hình 8: Lịch sử commit mã nguồn Repository GitHub*


# CHƯƠNG 3. GIÁM SÁT TÀI NGUYÊN, QUẢN TRỊ NHẬT KÝ VÀ GIA CỐ BẢO MẬT


## 3.1. Giám sát tài nguyên máy chủ theo thời gian thực với Prometheus và Grafana

Trong công tác quản trị hệ thống phần mềm chuyên nghiệp, việc chủ động theo dõi tình trạng tài nguyên phần cứng và hiệu năng dịch vụ đóng vai trò then chốt nhằm phát hiện sớm các nguy cơ quá tải. Đề tài triển khai tích hợp giải pháp giám sát toàn diện dựa trên Prometheus và Grafana:

Prometheus hoạt động theo mô hình kéo (pull-based metrics collection), định kỳ 5 giây một lần gửi yêu cầu thu thập số liệu tới 4 mục tiêu giám sát (Targets) chính: ứng dụng web nhà hàng (cổng 5000/metrics), bộ giám sát container cAdvisor (cổng 8080/metrics), bộ giám sát phần cứng Node Exporter (cổng 9100/metrics) và bản thân máy chủ Prometheus (cổng 9090/metrics). Cả 4 mục tiêu giám sát đều được thiết lập hoạt động ổn định và duy trì trạng thái UP màu xanh lá.

Nền tảng Grafana hoạt động tại cổng 3000 kết nối với nguồn dữ liệu Prometheus để trực quan hóa các số liệu thu thập được thành các đồ thị biến thiên theo thời gian thực. Bảng điều khiển Grafana cung cấp các thông số then chốt: tỷ lệ chiếm dụng CPU của hệ điều hành và từng container, dung lượng bộ nhớ RAM tiêu thụ, lưu lượng yêu cầu đặt món mỗi giây (RPS) và thời gian phản hồi yêu cầu (độ trễ đo bằng miligiây).


*Hình 9: Trang Prometheus Targets hiển thị danh sách 4 mục tiêu giám sát*


*Hình 10: Dashboard Grafana hiển thị các chỉ số giám sát của hệ thống*


## 3.2. Quản trị nhật ký hoạt động tập trung với Loki và Promtail

Bên cạnh việc theo dõi số liệu hiệu năng bằng Prometheus, hệ thống tích hợp giải pháp quản trị nhật ký hoạt động tập trung sử dụng Loki và Promtail. Kiến trúc này giải quyết nhược điểm phân tán của log khi vận hành nhiều container độc lập:

Ứng dụng web Python Flask được cấu hình để xuất toàn bộ thông tin truy cập và thao tác nghiệp vụ dưới dạng log có cấu trúc chuẩn JSON. Mỗi bản ghi nhật ký ghi lại đầy đủ các trường thông tin: thời điểm ghi nhận (timestamp), mức độ thông tin (level: INFO/ERROR), tên dịch vụ phát sinh (service: restaurant-web), đường dẫn endpoint được truy cập (path), phương thức HTTP (method), mã trạng thái phản hồi (status), thời gian xử lý yêu cầu (duration) và mã sinh viên tác giả (student_id: DTC245200862).

Agent Promtail chạy nền tự động đọc các luồng log từ Docker daemon, gắn thêm các nhãn định danh (labels) và chuyển tiếp liên tục về kho lưu trữ Loki. Nhờ cơ chế chỉ đánh chỉ mục theo nhãn và nén dữ liệu khối log, Loki tiết kiệm đáng kể tài nguyên lưu trữ và cho phép quản trị viên tra cứu lịch sử hoạt động một cách nhanh chóng.


## 3.3. Hướng dẫn tra cứu và phân tích nhật ký bằng ngôn ngữ truy vấn LogQL

Để phục vụ công tác điều tra nguyên nhân sự cố hoặc kiểm toán các giao dịch gọi món của nhà hàng, quản trị viên mở giao diện Grafana Explore, chọn nguồn dữ liệu Loki và thực thi các câu truy vấn LogQL tiêu biểu sau:

Truy vấn 1: Lọc toàn bộ các bản ghi nhật ký phát sinh từ container ứng dụng web nhà hàng:

Ý nghĩa: Lệnh này giúp quản trị viên theo dõi toàn bộ các luồng thao tác nghiệp vụ mà ứng dụng web vừa thực hiện.

Truy vấn 2: Trích xuất trường dữ liệu JSON và lọc riêng các yêu cầu truy cập thành công (mã trạng thái HTTP 200):

Ý nghĩa: Bóc tách các trường trong chuỗi log JSON để thống kê chính xác số lượng yêu cầu đặt món và xem thực đơn hoàn tất thành công.

Truy vấn 3: Tra cứu và phát hiện các thông báo lỗi phát sinh trong hệ thống:

Ý nghĩa: Cho phép phát hiện ngay các sự cố bất thường như mất kết nối cơ sở dữ liệu hay lỗi thực thi truy vấn để kịp thời xử lý.


*Hình 11: Kiểm tra và giám sát nhật ký hoạt động của hệ thống bằng Grafana và Loki*


*Hình 12: Truy vấn lọc từ khóa nhật ký hoạt động ứng dụng bằng LogQL trên Grafana*


## 3.4. Năm giải pháp gia cố an ninh hệ thống

Nhằm đảm bảo an toàn vận hành và giảm thiểu nguy cơ bị tấn công khai thác lỗ hổng máy chủ, hệ thống được áp dụng đồng bộ 5 giải pháp gia cố an ninh (Security Hardening) theo chuẩn công nghiệp:

- 1. Chạy container với tài khoản người dùng thông thường (Non-root Container): Thay vì để tiến trình trong container chạy với đặc quyền root mặc định, tác giả cấu hình Dockerfile và tệp điều phối tạo riêng tài khoản appuser với mã định danh UID: 1001. Trong trường hợp ứng dụng web bị tin tặc khai thác lỗ hổng, kẻ tấn công cũng chỉ bị giới hạn trong phạm vi người dùng thường và không thể leo thang đặc quyền để kiểm soát máy chủ Linux.
- 2. Cô lập phân vùng mạng nội bộ ba lớp (Multi-tier Network Isolation): Hệ thống phân tách thành 3 mạng Docker riêng biệt: mạng frontend-net kết nối Nginx với ứng dụng web; mạng monitoring-net kết nối các công cụ giám sát; và mạng backend-net cô lập cơ sở dữ liệu PostgreSQL. Container cơ sở dữ liệu hoàn toàn không có cổng mở trực tiếp ra bên ngoài, ngăn chặn triệt để các đợt tấn công dò quét cổng từ Internet.
- 3. Tước bỏ đặc quyền Linux nguy hiểm (cap_drop: ALL): Trong tệp cấu hình docker-compose.yml, container web được áp dụng chỉ thị tước bỏ toàn bộ các quyền can thiệp nhân hệ điều hành của Linux (Capabilities). Ứng dụng web bị cấm tuyệt đối việc can thiệp cấu hình mạng hoặc ghi đè tập tin hệ thống.
- 4. Bảo mật biến môi trường và thông tin xác thực (.env): Toàn bộ thông tin nhạy cảm bao gồm mật khẩu cơ sở dữ liệu, tài khoản quản trị viên và khóa bí mật của ứng dụng được lưu trữ trong tệp .env nội bộ, áp dụng độ phức tạp cao (chứa ký tự hoa, thường, số và ký tự đặc biệt như StrongPass#2026) và được bảo vệ nghiêm ngặt không đưa lên kho mã nguồn công khai.
- 5. Ẩn thông tin phiên bản máy chủ (server_tokens off): Cấu hình Nginx được thiết lập ẩn hoàn toàn chuỗi số hiệu phiên bản phần mềm trong các tiêu đề phản hồi HTTP. Kẻ tấn công khi quét cổng sẽ không thể xác định được phiên bản chính xác để tìm kiếm các lỗ hổng bảo mật đã biết.

*Hình 13: Cấu hình mạng Docker, Non-root và các cổng truy cập của hệ thống*


# CHƯƠNG 4. KỊCH BẢN THỬ NGHIỆM, KẾT QUẢ ĐẠT ĐƯỢC VÀ ĐÁNH GIÁ


## 4.1. Kịch bản 10 bước thử nghiệm và nghiệm thu hệ thống

Để phục vụ công tác kiểm thử chất lượng và nghiệm thu thực tế, kịch bản 10 trường hợp kiểm thử (Test Cases) dưới đây mô tả chi tiết từng thao tác thực hiện, tiêu chí kỳ vọng và kết quả ghi nhận thực tế trên hệ thống:


## 4.2. Hướng dẫn chi tiết các câu lệnh thực thi trên Terminal máy ảo Ubuntu

Khi thao tác trên máy ảo Ubuntu để kiểm thử và chụp ảnh minh chứng cho bài báo cáo, sinh viên mở cửa sổ Terminal (tổ hợp phím tắt Ctrl + Alt + T) và lần lượt thực thi các lệnh sau:


### 1. Lệnh kiểm tra cấu trúc cây thư mục dự án (dùng để chụp Hình 1):


### 2. Lệnh kiểm tra trạng thái hoạt động của 10 container (dùng để chụp Hình 2):


### 3. Lệnh kiểm tra phản hồi Nginx và các tiêu đề bảo mật HTTP (dùng để chụp Hình 6):


### 4. Lệnh xem cấu hình phân vùng mạng và gia cố an ninh trong docker-compose.yml (dùng để chụp Hình 13):


## 4.3. Hướng dẫn chi tiết các đường dẫn URL và tài khoản để chụp ảnh giao diện

Đối với các minh chứng giao diện người dùng trên trình duyệt web (Firefox hoặc Chrome), sinh viên truy cập lần lượt theo các địa chỉ và thông tin xác thực sau:


## 4.4. Những kết quả thực tế mà hệ thống đã làm được

Sau quá trình triển khai, kiểm thử và tối ưu hóa toàn diện, hệ thống Quản lý Nhà hàng & Đặt món (Order) - Đề 12 đã hoàn thành xuất sắc các mục tiêu đề ra:

- Xây dựng thành công ứng dụng web nhà hàng hoàn chỉnh với 3 phân hệ giao diện chuyên biệt cho Khách hàng, Nhân viên và Quản trị viên, hỗ trợ đầy đủ các thao tác nghiệp vụ đặt món, chế biến và quyết toán tài chính.
- Đóng gói và điều phối tự động hóa 10 dịch vụ độc lập bằng Docker Compose, khởi động ổn định bằng một câu lệnh duy nhất mà không xảy ra xung đột cổng hoặc lỗi thiếu thư viện phụ thuộc.
- Thiết lập thành công chốt chặn an ninh Nginx Reverse Proxy mã hóa toàn bộ dữ liệu qua giao thức HTTPS với chứng chỉ số SSL, cấu hình đầy đủ các tiêu đề bảo vệ an ninh mạng nâng cao.
- Xây dựng hệ thống giám sát sức khỏe máy chủ theo thời gian thực bằng Prometheus và Grafana với 4 mục tiêu giám sát đạt trạng thái UP 100%.
- Thiết lập luồng thu thập và quản trị nhật ký hoạt động tập trung sử dụng Loki và Promtail với định dạng log JSON chuẩn mực, thực hiện thành công các truy vấn phân tích LogQL nhanh chóng.
- Áp dụng đồng bộ và nghiêm ngặt 5 giải pháp gia cố an ninh (Security Hardening), bảo vệ hệ thống vững chắc trước các nguy cơ tấn công leo thang đặc quyền.

## 4.5. Các hạn chế tồn tại và hướng hoàn thiện trong tương lai

Bên cạnh các kết quả nổi bật đã đạt được, hệ thống vẫn còn một số điểm có thể tiếp tục nâng cấp trong các giai đoạn phát triển tiếp theo:

- Chứng chỉ bảo mật SSL hiện tại: Đang sử dụng chứng chỉ tự ký (Self-signed Certificate) phục vụ môi trường thử nghiệm cục bộ, do đó trình duyệt web ngoài môi trường mạng nội bộ sẽ hiển thị cảnh báo tin cậy. Hướng khắc phục: Khi triển khai hệ thống lên tên miền Internet chính thức, hệ thống sẽ tích hợp công cụ Certbot tự động cấp phát và làm mới chứng chỉ số quốc tế Let's Encrypt hoàn toàn miễn phí.
- Cơ chế cảnh báo sự cố máy chủ: Việc theo dõi trạng thái tài nguyên hiện tại vẫn dựa trên việc quản trị viên chủ động quan sát bảng điều khiển Grafana. Hướng khắc phục: Tích hợp công cụ Alertmanager để tự động gửi tin nhắn cảnh báo khẩn cấp qua ứng dụng Telegram hoặc gửi Email cảnh báo tức thì khi tải CPU vượt ngưỡng 80% hoặc dung lượng RAM bị cạn kiệt.

## 4.6. Bảng đối chiếu tự đánh giá theo 7 tiêu chí của học phần

Dưới đây là bảng đối chiếu kết quả thực hiện của đề tài so với 7 tiêu chí đánh giá của học phần Triển khai và Quản trị Hệ thống Phần mềm:


# KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

Đề tài 'Hệ thống Quản lý Nhà hàng & Đặt món (Order) - Đề 12' đã được sinh viên Hồ Quang Huy nghiên cứu, thiết kế và triển khai thành công, đáp ứng toàn diện mọi yêu cầu thực hành và quản trị của học phần Triển khai và Quản trị Hệ thống Phần mềm tại Trường Đại học Công nghệ Thông tin và Truyền thông.

Thông qua việc xây dựng một sản phẩm phần mềm gắn liền với thực tiễn quản lý kinh doanh dịch vụ ẩm thực, sinh viên không chỉ củng cố kỹ năng lập trình web backend và cơ sở dữ liệu quan hệ, mà quan trọng hơn cả là đã làm chủ được các công nghệ hạ tầng DevOps hiện đại: từ tư duy đóng gói phần mềm bằng Docker container, kỹ năng điều phối dịch vụ tự động hóa bằng Docker Compose, kỹ năng bảo mật hệ thống mạng và chứng chỉ số với Nginx Reverse Proxy, cho đến năng lực thiết lập hệ thống giám sát sức khỏe máy chủ Prometheus/Grafana và quản trị nhật ký tập trung Loki/Promtail.

Kết quả thực nghiệm đã khẳng định tính đúng đắn và hiệu quả vượt trội của mô hình: hệ thống gồm 10 dịch vụ container độc lập nhưng vẫn vận hành nhịp nhàng, ổn định, tự phục hồi khi gặp lỗi và khởi động tự động hóa hoàn toàn chỉ bằng một câu lệnh duy nhất. Đây là nền tảng kiến thức và kỹ năng thực tiễn giá trị, giúp sinh viên tự tin tiếp cận môi trường làm việc thực tế tại các doanh nghiệp công nghệ trong tương lai.

Trong giai đoạn tiếp theo, hệ thống có thể được tiếp tục nghiên cứu và mở rộng theo 3 định hướng sau:

- Tích hợp Trí tuệ Nhân tạo (AI): Xây dựng mô hình học máy phân tích thói quen ăn uống và lịch sử gọi món của từng thực khách để đưa ra các gợi ý món ăn phù hợp, gia tăng doanh số và nâng cao trải nghiệm khách hàng.
- Triển khai trên cụm máy chủ đám mây Kubernetes (K8s): Ứng dụng công nghệ Kubernetes để tự động co giãn số lượng container (Auto-scaling) theo lưu lượng truy cập thực tế trong các khung giờ cao điểm, đáp ứng nhu cầu cho chuỗi nhà hàng quy mô lớn.
- Tích hợp cổng thanh toán trực tuyến: Kết nối trực tiếp với các cổng thanh toán điện tử như VNPay, MoMo, ZaloPay và mã VietQR động để khách hàng thực hiện thanh toán trực tuyến tức thì ngay tại bàn ăn.
Sinh viên xin trân trọng cảm ơn quý thầy cô giáo đã theo dõi, đóng góp ý kiến và đánh giá đề tài này!
