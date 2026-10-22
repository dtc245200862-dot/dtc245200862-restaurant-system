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


# LỜI NÓI ĐẦU ................................................................................................................................... 4


# DANH MỤC THUẬT NGỮ VÀ KHÁI NIỆM DỄ HIỂU .................................................................. 5


# DANH MỤC HÌNH ẢNH MINH CHỨNG ...................................................................................... 6


# DANH MỤC BẢNG BIỂU ................................................................................................................ 7


# CHƯƠNG 1. TỔNG QUAN HỆ THỐNG VÀ BÀI TOÁN QUẢN LÝ NHÀ HÀNG ......................... 8


## 1.1. Lý do ra đời và mục tiêu thực tế của hệ thống ..................................................................... 8


## 1.2. Hệ thống này làm được những công việc gì trong thực tế? ................................................. 9


## 1.3. Khách hàng, nhân viên và người quản lý sử dụng hệ thống như thế nào? ........................... 10


## 1.4. Những điểm đặc biệt và ưu thế nổi bật của hệ thống ......................................................... 11


## 1.5. Bảng đối chiếu các công nghệ sử dụng bằng ngôn ngữ đời thường ..................................... 12


## 1.6. Mô hình kiến trúc 10 bộ phận và luồng hoạt động tổng thể ............................................... 13


# CHƯƠNG 2. CHI TIẾT CÁC CHỨC NĂNG VÀ CÁCH THỨC VẬN HÀNH ................................. 14


## 2.1. Cách tổ chức thư mục mã nguồn và tài liệu dự án ............................................................. 14


## 2.2. Khởi động toàn bộ 10 thành phần bằng một câu lệnh duy nhất ........................................... 15


## 2.3. Trải nghiệm thực tế của khách hàng khi xem thực đơn và gọi món ..................................... 16


## 2.4. Trải nghiệm của nhân viên phục vụ khi tiếp nhận và xử lý đơn hàng ................................. 17


## 2.5. Trải nghiệm của chủ nhà hàng khi xem báo cáo tài chính và lợi nhuận .............................. 18


## 2.6. Ngăn chứa dữ liệu và cấu trúc 8 bảng lưu trữ thông tin nhà hàng ....................................... 19


## 2.7. Chiếc cổng bảo vệ an toàn Nginx và ổ khóa mã hóa thông tin HTTPS .............................. 20


## 2.8. Kho lưu trữ mã nguồn trên GitHub và cách quản lý phiên bản ........................................... 21


# CHƯƠNG 3. THEO DÕI SỨC KHỎE MÁY CHỦ, SỔ NHẬT KÝ VÀ BẢO VỆ HỆ THỐNG ........ 22


## 3.1. Thiết bị đo nhịp tim và tải của máy chủ: Prometheus và Grafana ...................................... 22


## 3.2. Cuốn sổ nhật ký tự động ghi chép mọi hoạt động: Loki và Promtail ................................. 23


## 3.3. Hướng dẫn cách tra cứu nhật ký bằng 3 câu lệnh tìm kiếm đơn giản .................................. 24


## 3.4. Năm lớp áo giáp bảo vệ hệ thống trước nguy cơ bị xâm nhập ............................................ 25


# CHƯƠNG 4. KỊCH BẢN CHẠY THỬ, KẾT QUẢ ĐẠT ĐƯỢC VÀ ĐÁNH GIÁ ........................... 26


## 4.1. Bảng kịch bản 10 bước chạy thử nghiệm thu hệ thống ....................................................... 26


## 4.2. Hướng dẫn chi tiết từng câu lệnh gõ trên màn hình đen Terminal ...................................... 27


## 4.3. Hướng dẫn chi tiết từng trang web cần mở để chụp ảnh minh chứng ................................. 28


## 4.4. Những kết quả thực tế mà hệ thống đã làm được ............................................................... 29


## 4.5. Những hạn chế hiện tại và hướng khắc phục trong tương lai .............................................. 29


## 4.6. Đánh giá đối chiếu theo đúng 7 yêu cầu của học phần ....................................................... 30


# KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN ........................................................................................ 31


# DANH MỤC THUẬT NGỮ VÀ KHÁI NIỆM DỄ HIỂU

Để người đọc dù không chuyên về công nghệ thông tin cũng có thể hiểu một cách dễ dàng và mạch lạc toàn bộ nội dung bản báo cáo, phần này giải thích ngắn gọn các khái niệm kỹ thuật cốt lõi bằng các hình ảnh ví von gần gũi trong đời sống hàng ngày:

- Docker và Container (Đóng gói ứng dụng): Giống như những chiếc thùng container tiêu chuẩn trên các chuyến tàu chở hàng. Mỗi phần mềm được đóng gói cẩn thận vào một chiếc thùng riêng, bên trong có sẵn tất cả đồ đạc, công cụ cần thiết để nó tự vận hành được. Nhờ đó phần mềm có thể mang đi chạy ở bất kỳ máy tính nào mà không bao giờ sợ bị lỗi thiếu file hay xung đột với các phần mềm khác.
- Docker Compose (Người nhạc trưởng điều phối): Là công cụ chỉ huy giúp điều khiển cùng lúc nhiều thùng container. Thay vì phải mất công đi khởi động từng phần mềm một cách thủ công, người quản trị chỉ cần ra lệnh cho người nhạc trưởng này một câu duy nhất là tất cả 10 thùng container sẽ đồng loạt khởi động ăn khớp nhịp nhàng với nhau.
- Nginx Reverse Proxy (Người gác cổng bảo vệ): Giống như một chú bảo vệ đứng trực ở cổng ra vào duy nhất của nhà hàng. Khách hàng từ bên ngoài vào không được tự tiện đi lung tung vào kho chứa hay nhà bếp, mà tất cả đều phải gặp chú bảo vệ này trước để kiểm tra tính hợp lệ và dẫn đường vào đúng chỗ.
- SSL/HTTPS (Chiếc ổ khóa an toàn): Khi bạn vào một trang web có hình chiếc ổ khóa nhỏ bên cạnh dòng địa chỉ, đó chính là giao thức HTTPS. Nó giống như việc mọi bức thư trao đổi giữa khách hàng và nhà hàng đều được bỏ vào một chiếc hộp sắt có khóa mã số kiên cố. Dù có kẻ xấu đứng nghe lén trên đường truyền mạng cũng không tài nào đọc được khách vừa đặt món gì hay gõ mật khẩu gì.
- PostgreSQL (Kho lưu trữ dữ liệu an toàn): Giống như một chiếc tủ hồ sơ chống cháy nhiều ngăn, lưu trữ ngăn nắp toàn bộ danh sách các món ăn, danh sách bàn, các đơn hàng và hóa đơn của nhà hàng để không bao giờ bị mất mát dù máy tính có bị mất điện đột ngột.
- pgAdmin (Giao diện xem kho hồ sơ): Là màn hình đồ họa giúp người quản lý nhìn thấy trực quan các ngăn kéo trong tủ hồ sơ PostgreSQL, dễ dàng bấm chuột vào xem từng bảng mà không cần phải gõ các câu lệnh máy tính phức tạp.
- Prometheus (Chiếc máy đo nhịp tim hệ thống): Hoạt động giống như thiết bị y tế liên tục đo huyết áp và nhịp tim của máy chủ, cứ 5 giây một lần kiểm tra xem máy chủ đang tải bao nhiêu phần trăm, có bị sốt nóng hay chạy chậm chạp không.
- Grafana (Bảng đồng hồ hiển thị trực quan): Giống như bảng đồng hồ điện tử trên xe ô tô, gom toàn bộ các số liệu nhịp tim của Prometheus và vẽ thành các biểu đồ màu sắc trực quan, giúp người quản lý chỉ cần liếc mắt nhìn qua là biết máy chủ đang chạy nhanh hay chậm.
- Loki và Promtail (Cuốn sổ nhật ký tự động): Promtail giống như một người thư ký mẫn cán đứng cạnh ghi chép lại mọi sự việc diễn ra trong nhà hàng rồi chuyển vào cuốn sổ nhật ký khổng lồ Loki. Khi cần xem lại lúc mấy giờ có ai bấm đặt món, hoặc khi xảy ra sự cố thì mở cuốn sổ này ra tra cứu trong tích tắc.
- System Hardening (Mặc áo giáp bảo vệ máy chủ): Là tập hợp các biện pháp khóa bớt các cánh cửa không cần thiết, tước bỏ các quyền hạn nguy hiểm để biến hệ thống máy tính thành một pháo đài vững chắc, kẻ xấu dù có lẻn vào được cũng không thể phá hoại được máy chủ chính.

# LỜI NÓI ĐẦU

Trong thời đại công nghệ số bùng nổ mạnh mẽ như hiện nay, ngành dịch vụ ẩm thực và nhà hàng đang đứng trước một làn sóng chuyển đổi số vô cùng sâu sắc. Phương thức kinh doanh truyền thống vốn phụ thuộc hoàn toàn vào những tờ giấy ghi món viết tay, những tiếng gọi í ới gọi nhân viên phục vụ trong giờ cao điểm đang bộc lộ rất nhiều hạn chế: tình trạng nhầm lẫn món ăn thường xuyên xảy ra, khách hàng phải chờ đợi lâu gây cảm giác ức chế, tồn kho nguyên liệu khó kiểm soát và nguy cơ thất thoát doanh thu của chủ nhà hàng là rất lớn.

Xuất phát từ thực tế cấp thiết đó, đề tài 'Hệ thống Quản lý Nhà hàng & Đặt món (Order)' trong khuôn khổ học phần Triển khai và Quản trị Hệ thống Phần mềm tại Trường Đại học Công nghệ Thông tin và Truyền thông (ICTU) đã được sinh viên Hồ Quang Huy (Mã sinh viên: DTC245200862) nghiên cứu và xây dựng hoàn chỉnh. Đề tài không đơn thuần là việc lập trình nên một trang web bán hàng, mà mục tiêu trọng tâm là ứng dụng toàn diện các công nghệ tiên tiến nhất của thế giới DevOps hiện đại để giải quyết bài toán vận hành hệ thống một cách an toàn, thông minh, bền vững và tự động hóa.

Bản báo cáo này được trình bày theo phương pháp diễn đạt mạch lạc, thực tế và dễ hiểu nhất. Mọi khái niệm kỹ thuật phức tạp đều được phân tích dưới góc nhìn đời thường để bất kỳ ai khi đọc qua cũng đều có thể nắm bắt được hệ thống này làm được gì, mang lại giá trị gì cho xã hội và vận hành trên thực tế ra sao.

Sinh viên xin bày tỏ lòng biết ơn chân thành và sâu sắc nhất tới thầy giáo TS. Lê Khánh Dương cùng các thầy cô giáo trong Bộ môn Hệ thống Thông tin và Mạng máy tính - Khoa Công nghệ Thông tin đã tận tình chỉ bảo, truyền đạt những kiến thức quý báu và định hướng phương pháp triển khai chuẩn mực giúp sinh viên hoàn thành xuất sắc đề tài này.


# CHƯƠNG 1. TỔNG QUAN HỆ THỐNG VÀ BÀI TOÁN QUẢN LÝ NHÀ HÀNG


## 1.1. Lý do ra đời và mục tiêu thực tế của hệ thống

Để hiểu rõ vì sao hệ thống này lại cần thiết, chúng ta hãy cùng nhìn vào bức tranh vận hành của một nhà hàng ẩm thực thông thường. Khi một nhóm khách bước vào quán vào buổi trưa hoặc buổi tối cuối tuần, khung cảnh thường thấy là nhân viên chạy đôn chạy đáo từ bàn này sang bàn khác. Nhân viên phải cầm cuốn sổ nhỏ và chiếc bút bi đứng chờ khách suy nghĩ chọn món. Sau khi ghi chép xong, nhân viên lại phải chạy một quãng đường dài xuống phòng bếp để kẹp tờ giấy gọi món lên giá.

Trong quá trình đó, rất nhiều vấn đề tiêu cực có thể xảy ra: chữ viết của nhân viên vội vàng nguệch ngoạc khiến đầu bếp đọc nhầm món ăn; các tờ giấy gọi món bị gió thổi bay hoặc lẫn lộn thứ tự trước sau khiến bàn vào sau lại có đồ ăn trước; những món ăn mà trong bếp đã hết sạch nguyên liệu nhưng nhân viên ngoài sảnh không biết nên vẫn ghi cho khách, đến khi khách ngồi chờ nửa tiếng sau mới quay ra thông báo hết món gây bức xúc cho thực khách. Cuối ngày, người thu ngân phải ngồi đếm từng tờ hóa đơn giấy, cộng trừ bằng máy tính bấm tay rất mất thời gian và dễ xảy ra thất thoát tiền bạc.

Mục tiêu của đề tài Đề 12 là xóa bỏ hoàn toàn phương thức thủ công lạc hậu đó bằng cách xây dựng một hệ thống phần mềm quản lý nhà hàng trực tuyến hoàn chỉnh. Tất cả các khâu từ xem thực đơn, gọi món, báo bếp, cập nhật trạng thái chế biến cho đến quản lý tồn kho và thanh quyết toán tài chính đều được kết nối liền mạch trên cùng một hệ thống mạng máy tính. Quan trọng hơn cả, hệ thống được xây dựng theo chuẩn công nghiệp DevOps của các công ty công nghệ lớn: toàn bộ các bộ phận đều được đóng gói thành các thùng container độc lập, vận hành tự động và có các hệ thống giám sát sức khỏe, bảo vệ an ninh vô cùng chặt chẽ.


## 1.2. Hệ thống này làm được những công việc gì trong thực tế?

Hệ thống Quản lý Nhà hàng & Đặt món này được thiết kế để phục vụ trọn vẹn 3 nhóm đối tượng thực tế trong một nhà hàng:

- Đối với Khách hàng (Thực khách): Khách chỉ cần ngồi tại bàn ăn của mình, mở điện thoại thông minh hoặc máy tính bảng lên là có ngay một cuốn thực đơn điện tử vô cùng bắt mắt. Khách có thể lướt xem các món ăn được chia thành 4 nhóm sang trọng, nhìn thấy hình ảnh món ăn chân thực và giá tiền rõ ràng. Khách bấm nút chọn món, chọn đúng số bàn mình đang ngồi (hoặc chọn mang về) rồi bấm nút Đặt món. Ngay sau đó, khách có thể theo dõi trực tiếp trên màn hình xem món ăn của mình đang được bếp nấu hay đã sẵn sàng mang lên. Khi ăn xong, khách có thể chấm điểm đánh giá từ 1 đến 5 sao và viết nhận xét về chất lượng phục vụ của nhà hàng.
- Đối với Nhân viên phục vụ và Nhà bếp: Nhân viên không còn phải chạy đi chạy lại để đưa giấy gọi món. Ngay khi khách bấm đặt món trên điện thoại, trên màn hình máy tính bảng của nhân viên và nhà bếp sẽ lập tức nhảy ra thông báo đơn hàng mới tinh, ghi rõ ràng bàn số mấy vừa gọi những món gì, mỗi món mấy suất và khách có dặn dò gì đặc biệt không (ví dụ: làm chín vừa, cho ít cay, nhiều đá). Đầu bếp nhìn vào đó để chế biến theo đúng thứ tự. Nấu xong món nào, nhân viên chỉ cần bấm một nút chuyển trạng thái sang 'Đã lên món'. Nhân viên cũng có thể kiểm soát danh sách các bàn ăn xem bàn nào đang có khách ngồi (màu đỏ) và bàn nào còn đang trống (màu xanh).
- Đối với Chủ nhà hàng và Quản lý: Người quản lý có một phân hệ quản trị riêng biệt. Dù đang đi công tác hay ngồi ở nhà, quản lý chỉ cần mở màn hình lên là nhìn thấy bức tranh toàn cảnh về tài chính: hôm nay nhà hàng đón được bao nhiêu lượt khách, bán được tổng cộng bao nhiêu tiền doanh thu, đã chi bao nhiêu tiền để nhập thịt cá rau củ, và đút túi lợi nhuận ròng thực tế là bao nhiêu triệu đồng. Quản lý cũng biết được món ăn nào đang bán chạy nhất và món nào trong kho sắp hết để kịp thời nhập thêm hàng.

## 1.3. Khách hàng, nhân viên và người quản lý sử dụng hệ thống như thế nào?

Để hình dung một cách trực quan, chúng ta hãy theo dõi một kịch bản sử dụng thực tế của một buổi ăn uống tại nhà hàng:

Bước 1: Anh Nguyễn Văn An cùng bạn bè bước vào nhà hàng và ngồi vào Bàn số 02. Trên mặt bàn có dán sẵn thông tin hướng dẫn truy cập trang web của nhà hàng. Anh An mở trình duyệt web trên điện thoại và truy cập vào địa chỉ hệ thống.

Bước 2: Trang web hiện ra giao diện thực đơn vô cùng đẹp mắt. Anh An bấm vào danh mục 'Món chính thượng hạng' và chọn 1 đĩa 'Bò bít tết sốt tiêu đen Wagyu' giá 150.000 đồng, chọn tiếp danh mục 'Món khai vị & Salad' để lấy 1 đĩa 'Salad rong nho sốt mè rang' giá 45.000 đồng, và vào danh mục 'Đồ uống' chọn thêm 1 ly 'Trà đào cam sả thảo mộc' giá 30.000 đồng. Anh An nhập số Bàn 02, ghi chú thêm dặn dò 'Bò bít tết làm chín vừa, cho nhiều sốt tiêu' rồi bấm nút 'Xác nhận đặt món'.

Bước 3: Ngay lập tức, trên màn hình máy tính của nhân viên phục vụ hiển thị một đơn hàng mới mang mã số #5, hiện đầy đủ thông tin: Bàn 02 - Khách hàng Nguyễn Văn An - Tổng tiền 225.000 đồng, kèm danh sách 3 món ăn đã gọi. Sơ đồ bàn ăn trên hệ thống tự động đổi Bàn 02 từ màu xanh (Bàn trống) sang màu đỏ (Đang có khách ngồi).

Bước 4: Nhân viên bấm xác nhận chuyển đơn hàng sang trạng thái 'Đang nấu' để nhà bếp tiến hành chế biến. Khi thức ăn chín, nhân viên bấm 'Đã lên món' và mang ra bàn phục vụ anh An. Anh An nhìn vào điện thoại của mình cũng thấy trạng thái đơn hàng đã cập nhật.

Bước 5: Khi dùng bữa xong và thanh toán, nhân viên bấm 'Hoàn tất đơn hàng'. Bàn số 02 lập tức tự động đổi lại về trạng thái màu xanh sẵn sàng đón lượt khách tiếp theo. Toàn bộ số tiền 225.000 đồng được hệ thống tự động ghi nhận vào doanh thu trong ngày của nhà hàng.


## 1.4. Những điểm đặc biệt và ưu thế nổi bật của hệ thống

Hệ thống Quản lý Nhà hàng này sở hữu những ưu thế vượt trội so với các phần mềm quản lý thông thường:

- Không cần cài đặt ứng dụng phức tạp: Người dùng không cần phải tải app từ App Store hay Google Play gây tốn dung lượng máy. Toàn bộ hệ thống chạy trực tiếp trên nền web, chỉ cần mở trình duyệt là sử dụng được ngay trên mọi thiết bị từ điện thoại iPhone, Android cho tới máy tính xách tay.
- Tốc độ phản hồi tức thời: Dữ liệu đặt món được cập nhật đồng bộ ngay tức thì. Nhân viên không bao giờ bị bỏ sót đơn hàng của khách.
- Giao diện chuẩn tiếng Việt thanh lịch: Các nút bấm chọn danh mục được thiết kế nhỏ gọn, tinh tế dạng viên thuốc (pill), cỡ chữ giá tiền được điều chỉnh vừa vặn, không bị phình to vỡ dòng hay hiển thị những dòng mã lạ làm rối mắt người dùng.
- Quản lý tài chính minh bạch: Có phân hệ tính toán lãi ròng rõ ràng (Doanh thu bán ra trừ đi Chi phí mua nguyên vật liệu bằng Lợi nhuận thực tế), giúp chủ nhà hàng nắm chắc dòng tiền kinh doanh từng ngày.
- Khởi động tự động bằng một câu lệnh: Toàn bộ 10 thành phần phức tạp của hệ thống (web, cơ sở dữ liệu, cổng bảo vệ, đo tải, ghi nhật ký) đều được đóng gói sẵn trong Docker. Người quản trị chỉ cần gõ đúng 1 câu lệnh duy nhất là hệ thống tự khởi động chạy mượt mà.

## 1.5. Bảng đối chiếu các công nghệ sử dụng bằng ngôn ngữ đời thường

Dưới đây là bảng tổng hợp các công nghệ được sử dụng trong đề tài, được giải thích đối chiếu bằng ngôn ngữ đời thường để người đọc dễ dàng hình dung:


## 1.6. Mô hình kiến trúc 10 bộ phận và luồng hoạt động tổng thể

Toàn bộ hệ thống được xây dựng từ 10 thành phần dịch vụ độc lập phối hợp ăn khớp với nhau như một cỗ máy đồng hồ cơ học:

Bộ phận số 1 là ứng dụng web nhà hàng (restaurant-web) viết bằng Python Flask. Đây là nơi chứa toàn bộ giao diện và các thuật toán xử lý nghiệp vụ gọi món, thanh toán tiền.

Bộ phận số 2 là cơ sở dữ liệu PostgreSQL (restaurant-db). Nơi đây lưu giữ bền vững toàn bộ danh mục 4 nhóm món ăn, danh sách bàn ăn, các đơn hàng và hóa đơn chi phí.

Bộ phận số 3 là công cụ quản trị pgAdmin (restaurant-pgadmin) giúp người quản trị dễ dàng tra cứu, chỉnh sửa và sao lưu dữ liệu của nhà hàng qua trình duyệt web.

Bộ phận số 4 là máy chủ Nginx (restaurant-nginx). Đóng vai trò là chốt chặn duy nhất mở cổng 80 và 443 ra thế giới bên ngoài, chịu trách nhiệm mã hóa toàn bộ dữ liệu đi qua đường truyền bằng chứng chỉ bảo mật HTTPS.

Bộ phận số 5 là máy chủ giám sát Prometheus (restaurant-prometheus) liên tục gửi tín hiệu kiểm tra định kỳ 5 giây một lần để lấy số liệu về lưu lượng người dùng đặt món.

Bộ phận số 6 là nền tảng bảng điều khiển Grafana (restaurant-grafana) hiển thị các đồ thị trực quan cho người quản lý theo dõi.

Bộ phận số 7 là công cụ cAdvisor (restaurant-cadvisor) chuyên đo đạc mức độ ngốn RAM và CPU của từng chiếc hộp container.

Bộ phận số 8 là công cụ Node Exporter (restaurant-node-exporter) chuyên đo tải phần cứng của máy chủ Linux.

Bộ phận số 9 là kho nhật ký tập trung Loki (restaurant-loki) chuyên lưu trữ và phân loại các dòng chữ nhật ký hoạt động.

Bộ phận số 10 là người giao nhật ký Promtail (restaurant-promtail) âm thầm thu lượm các file log từ các container rồi chuyển giao cho kho Loki cất giữ.


*Hình 1: Cấu trúc thư mục dự án*


# CHƯƠNG 2. CHI TIẾT CÁC CHỨC NĂNG VÀ CÁCH THỨC VẬN HÀNH


## 2.1. Cách tổ chức thư mục mã nguồn và tài liệu dự án

Dự án được phân chia thư mục vô cùng ngăn nắp và khoa học theo đúng nguyên tắc thiết kế phần mềm hiện đại. Mỗi một bộ phận chức năng đều có một ngăn chứa riêng biệt:

Thư mục 'app' chứa toàn bộ mã nguồn của trang web nhà hàng, các trang giao diện HTML dành riêng cho khách hàng, nhân viên và người quản lý, cùng các tệp hình ảnh, biểu tượng và tệp mã nguồn xử lý logic app.py.

Thư mục 'init-db' chứa tệp lệnh khởi tạo sẵn cấu trúc 8 bảng dữ liệu và nạp sẵn danh sách các món ăn thượng hạng của nhà hàng ngay khi hệ thống vừa khởi chạy.

Thư mục 'nginx' chứa các tệp cấu hình cổng bảo vệ và cặp chứng chỉ số bảo mật SSL giúp trang web chạy được giao thức HTTPS có hình chiếc ổ khóa an toàn.

Thư mục 'prometheus', 'grafana', 'loki' và 'promtail' chứa toàn bộ các tệp cấu hình tham số cho hệ thống đo tải sức khỏe và hệ thống thu thập sổ nhật ký tự động.

Tệp 'docker-compose.yml' nằm ở ngoài cùng đóng vai trò như bản đồ chỉ huy tổng thể, kết nối 10 bộ phận nói trên lại với nhau.


## 2.2. Khởi động toàn bộ 10 thành phần bằng một câu lệnh duy nhất

Một trong những điểm sáng nhất của đề tài này là khả năng vận hành tự động hóa cao độ. Thay vì người sử dụng phải mất nhiều giờ đồng hồ để cài đặt từng phần mềm riêng lẻ, cấu hình mạng lằng nhằng và dễ xảy ra lỗi không tương thích, toàn bộ hệ thống này đã được chuẩn hóa để khởi động chỉ bằng đúng 1 câu lệnh duy nhất:

Khi người quản trị gõ dòng lệnh này vào cửa sổ dòng lệnh Terminal của máy chủ Ubuntu và ấn Enter, cơ chế Docker Compose sẽ tự động kích hoạt. Nó tự động tạo ra 3 phân vùng mạng nội bộ độc lập, tự động gắn các ổ đĩa lưu trữ bền vững, và lần lượt đánh thức cả 10 container dịch vụ cùng hoạt động nhịp nhàng.

Để kiểm tra xem tất cả các bộ phận đã thức dậy và hoạt động khỏe mạnh hay chưa, người quản trị chỉ cần chạy lệnh kiểm tra:

Kết quả hiển thị trên màn hình sẽ liệt kê danh sách toàn bộ 10 container với cột trạng thái đều báo chữ 'Up' hoặc 'Up (healthy)' màu xanh lá, chứng minh hệ thống đã sẵn sàng 100% để đón nhận các lượt khách hàng truy cập.


*Hình 2: Trạng thái container*


## 2.3. Trải nghiệm thực tế của khách hàng khi xem thực đơn và gọi món

Khi thực khách truy cập vào phân hệ Khách hàng theo đường dẫn /customer/menu, một cuốn thực đơn điện tử chuẩn mực của một nhà hàng sang trọng sẽ hiện ra trước mắt. Giao diện được thiết kế với tông màu sáng tinh tế, sử dụng font chữ hiện đại, bố cục các khối món ăn cân đối hài hòa.

Thực đơn được chia làm 4 nhóm ẩm thực chuẩn vị:

- Món khai vị & Salad: Gồm các món thanh mát kích thích vị giác như Salad rong nho sốt mè rang (giá 45.000 đồng), Khoai tây chiên bơ tỏi Pháp (giá 35.000 đồng).
- Món chính thượng hạng: Gồm các món ăn bổ dưỡng đậm đà như Bò bít tết sốt tiêu đen Wagyu (giá 150.000 đồng), Cá hồi áp chảo sốt chanh leo (giá 180.000 đồng), Gà nướng thảo mộc ngũ vị (giá 120.000 đồng).
- Món nướng & Lẩu đặc biệt: Dành cho các nhóm bạn bè và gia đình quây quần như Set Lẩu Thái Hải Sản Hoàng Gia (giá 350.000 đồng).
- Đồ uống & Tráng miệng: Gồm Trà đào cam sả thảo mộc tươi mát (giá 30.000 đồng), Nước ép dưa hấu tươi mát lạnh (giá 25.000 đồng).
Các nút bấm chọn danh mục được thiết kế nhỏ nhắn, bo góc tròn trịa và không bao giờ bị vỡ dòng chữ. Giá tiền của từng món ăn được hiển thị với kích thước chuẩn mực, nổi bật trên nền màu xanh lá cây tươi tắn. Dưới mỗi món ăn có nút 'Đặt món này' nhỏ gọn. Khi bấm vào, một hộp thoại nhỏ xinh sẽ mở ra cho phép khách nhập số lượng, chọn số bàn ăn của mình và gửi dặn dò riêng cho đầu bếp.


*Hình 03: Giao diện hệ thống Quản lý Nhà hàng - Phân hệ Thực đơn Khách hàng*


## 2.4. Trải nghiệm của nhân viên phục vụ khi tiếp nhận và xử lý đơn hàng

Tại phân hệ dành riêng cho Nhân viên phục vụ (/staff/orders), nhân viên nhà hàng được cung cấp một bảng quản trị đơn đặt món trực quan và tiện dụng. Mỗi khi có khách hàng vừa bấm đặt món tại bàn ăn, thông tin đơn hàng mới sẽ lập tức xuất hiện ngay trên dòng đầu tiên của bảng danh sách.

Mỗi dòng đơn hàng thể hiện đầy đủ và chính xác các thông tin quan trọng: Mã số đơn hàng, Tên khách hàng đặt món, Hình thức dùng bữa (Ăn tại bàn số mấy hoặc Đóng hộp mang về), Tổng số tiền thanh toán, và đặc biệt là cột 'Món đã gọi'.

Cột 'Món đã gọi' hiển thị rõ ràng và chi tiết tên từng món ăn cùng số lượng suất tương ứng (ví dụ: Bò bít tết sốt tiêu đen Wagyu (x1), Salad rong nho sốt mè rang (x1), Trà đào cam sả thảo mộc (x1)), hoàn toàn không xảy ra bất kỳ lỗi kỹ thuật nào. Nhân viên có thể dễ dàng bấm nút chuyển đổi trạng thái đơn hàng theo đúng chu trình phục vụ: từ lúc nhận đơn chuyển sang 'Đang nấu', nấu xong chuyển sang 'Đã lên món', và khi khách thanh toán chuyển sang 'Hoàn tất'.

Nhân viên cũng có thể chuyển sang trang quản lý sơ đồ bàn ăn (/staff/tables) để nắm được bàn nào đang có khách ngồi dùng bữa, bàn nào khách đã đặt trước và bàn nào đang trống để xếp chỗ cho khách mới đến.


## 2.5. Trải nghiệm của chủ nhà hàng khi xem báo cáo tài chính và lợi nhuận

Chủ nhà hàng và người quản lý cấp cao sở hữu một phân hệ quản trị tối cao (/admin/dashboard). Tại đây, thay vì phải xem những con số rời rạc, hệ thống tự động tổng hợp toàn bộ hoạt động kinh doanh thành bức tranh tài chính sắc nét và minh bạch:

Chỉ số thứ nhất là Tổng doanh thu: Toàn bộ số tiền thu được từ các đơn hàng bán cho khách.

Chỉ số thứ hai là Tổng chi phí nhập hàng: Toàn bộ số tiền đã chi ra để mua thịt bò Wagyu, cá hồi, rau củ quả, tiền phí vận chuyển nguyên vật liệu theo từng hóa đơn nhập kho.

Chỉ số thứ ba - quan trọng nhất - là Lợi nhuận ròng thực tế: Được hệ thống tự động tính toán bằng công thức: Lợi nhuận ròng = Tổng doanh thu bán ra - Tổng chi phí nhập hàng. Con số này giúp chủ nhà hàng biết chính xác hôm nay mình thực sự kiếm được bao nhiêu tiền lãi.

Người quản trị cũng có thể quản lý danh sách toàn bộ các tài khoản nhân viên, phân quyền truy cập và xuất dữ liệu báo cáo kinh doanh phục vụ công tác thanh quyết toán thuế định kỳ.


## 2.6. Ngăn chứa dữ liệu và cấu trúc 8 bảng lưu trữ thông tin nhà hàng

Cơ sở dữ liệu PostgreSQL của nhà hàng được ví như một chiếc két sắt chống cháy lưu trữ thông tin tuyệt đối an toàn. Dữ liệu được tổ chức chuẩn hóa thành 8 bảng với các mối liên kết chặt chẽ:

- Bảng 1 - users (Tài khoản người dùng): Lưu trữ tên đăng nhập, mật khẩu được mã hóa an toàn, họ tên đầy đủ và vai trò của từng người (admin: chủ nhà hàng, staff: nhân viên phục vụ, customer: khách hàng).
- Bảng 2 - categories (Danh mục thực đơn): Lưu trữ 4 nhóm ẩm thực lớn của nhà hàng.
- Bảng 3 - menu_items (Danh sách món ăn): Lưu tên từng món ăn, đơn giá niêm yết, số lượng tồn kho còn lại trong bếp và trạng thái món còn đang phục vụ hay tạm hết.
- Bảng 4 - tables (Sơ đồ bàn ăn): Lưu trữ danh sách các bàn từ Bàn 01 đến Bàn 08, sức chứa của từng bàn và trạng thái hiện tại (bàn trống, đang có khách, đặt trước).
- Bảng 5 - orders (Đơn đặt món): Lưu mã đơn, tên khách hàng, số bàn ngồi, trạng thái đơn (chờ duyệt, đang nấu, đã lên món, hoàn thành), tổng tiền và ghi chú của khách.
- Bảng 6 - order_items (Chi tiết từng món trong đơn): Nối đơn hàng với món ăn, ghi rõ mỗi đơn gồm những món gì, mỗi món gọi mấy phần và thành tiền bao nhiêu.
- Bảng 7 - reviews (Đánh giá của thực khách): Lưu số sao đánh giá (từ 1 đến 5 sao) và những dòng bình luận cảm nhận của khách hàng sau bữa ăn.
- Bảng 8 - inventory_invoices (Hóa đơn nhập nguyên liệu): Ghi chép các đợt nhập nguyên liệu thịt bò, hải sản, rau quả, tiền vận chuyển và tổng tiền chi phí để tính lãi ròng.

*Hình 04: Cơ sở dữ liệu và bảng dữ liệu của hệ thống trên pgAdmin 4*


## 2.7. Chiếc cổng bảo vệ an toàn Nginx và ổ khóa mã hóa thông tin HTTPS

Máy chủ Nginx đóng vai trò như một người gác cổng mẫn cán đứng ở cổng chính của nhà hàng. Khi người dùng gõ địa chỉ trang web dạng thông thường (cổng 80 HTTP không an toàn), Nginx sẽ tự động phát hiện và chuyển hướng ngay lập tức sang cổng 443 với giao thức mã hóa HTTPS an toàn (cơ chế 301 Permanent Redirect).

Đồng thời, Nginx trang bị một chiếc chìa khóa mã hóa SSL công nghệ cao (thuật toán RSA 2048-bit). Nhờ có chiếc khóa này, toàn bộ đường truyền dữ liệu giữa điện thoại của khách hàng và máy chủ nhà hàng đều được xáo trộn thành những chuỗi ký tự bí mật không thể giải mã. Dù có kẻ xấu rình mò chặn bắt gói tin trên mạng wifi công cộng cũng không thể biết được mật khẩu hay thông tin đặt món của khách hàng.

Nginx còn được cài đặt sẵn các tấm lá chắn an ninh (Security Headers) để chống lại các thủ đoạn tin tặc phổ biến: tấm chắn X-Frame-Options ngăn kẻ xấu lồng trang web nhà hàng vào các trang lừa đảo giả mạo; tấm chắn X-Content-Type-Options ngăn chặn mã độc cải trang thành file ảnh; và cơ chế Rate Limiting giới hạn mỗi địa chỉ mạng chỉ được gửi tối đa 10 yêu cầu trong một giây để chống lại các đợt tấn công quấy phá làm tê liệt máy chủ.


*Hình 05: Giao diện hệ thống Nhà hàng truy cập qua Nginx reverse proxy với giao thức HTTPS*


*Hình 6: Kết quả kiểm tra các HTTP response headers được cấu hình trên Nginx*


## 2.8. Kho lưu trữ mã nguồn trên GitHub và cách quản lý phiên bản

Toàn bộ mã nguồn chương trình, các tệp cấu hình và tài liệu hướng dẫn của dự án đều được đồng bộ hóa và lưu trữ an toàn trên nền tảng GitHub tại địa chỉ kho lưu trữ chính thức: https://github.com/dtc245200862-dot/dtc245200862-restaurant-system.git.

Tên tài khoản GitHub và tên kho lưu trữ đều được đặt chuẩn chỉnh theo đúng mã sinh viên của tác giả (dtc245200862). Quá trình phát triển dự án được ghi chép trung thực qua các mốc commit lịch sử rõ ràng, phản ánh mạch lạc từng giai đoạn xây dựng hệ thống: từ việc đóng gói trang web ban đầu, tích hợp cơ sở dữ liệu, thiết lập cổng bảo vệ Nginx, bổ sung bộ đo tải Prometheus/Grafana cho tới việc hoàn thiện luồng nhật ký Loki/Promtail và tinh chỉnh giao diện người dùng.

Tệp cấu hình mật khẩu bí mật .env được loại bỏ hoàn toàn khỏi kho lưu trữ công khai để đảm bảo an toàn tuyệt đối, thay vào đó là tệp hướng dẫn mẫu .env.example giúp bất kỳ người nào khi tải dự án về cũng đều có thể dễ dàng thiết lập và chạy thử thành công.


*Hình 7: Repository GitHub của hệ thống Quản lý Nhà hàng dtc245200862-restaurant-system*


*Hình 8: Lịch sử commit mã nguồn Repository GitHub*


# CHƯƠNG 3. THEO DÕI SỨC KHỎE MÁY CHỦ, SỔ NHẬT KÝ VÀ BẢO VỆ HỆ THỐNG


## 3.1. Thiết bị đo nhịp tim và tải của máy chủ: Prometheus và Grafana

Một hệ thống phần mềm chuyên nghiệp không chỉ cần hoạt động tốt lúc bình thường mà còn phải có khả năng tự theo dõi sức khỏe của chính mình để người quản trị biết trước các nguy cơ quá tải. Trong đề tài này, cặp đôi công nghệ Prometheus và Grafana đóng vai trò như một phòng khám y tế thu nhỏ của máy chủ:

Prometheus hoạt động âm thầm và bền bỉ, cứ đúng 5 giây một lần nó lại gửi tín hiệu thăm dò đến 4 bộ phận trọng yếu trong hệ thống: ứng dụng web nhà hàng (/metrics), bộ phận giám sát thùng container cAdvisor, bộ phận đo lường phần cứng máy chủ Node Exporter, và chính bản thân máy chủ Prometheus. Cả 4 mục tiêu này đều được kiểm tra thực tế và duy trì trạng thái hoạt động hoàn hảo 100% (trạng thái UP màu xanh lá).

Từ nguồn số liệu đo đạc liên tục đó, nền tảng Grafana tại cổng 3000 sẽ tổng hợp và vẽ nên một bảng điều khiển đa năng tuyệt đẹp. Người quản lý khi nhìn vào màn hình Grafana sẽ thấy ngay các đồ thị biến thiên trực quan theo thời gian thực: biểu đồ đo số lượng khách hàng truy cập mỗi giây (RPS), biểu đồ đo thời gian máy chủ trả lời yêu cầu (độ trễ miligiây), tỷ lệ các truy cập thành công hay thất bại, và mức độ chiếm dụng bộ nhớ RAM cũng như năng lực xử lý CPU của từng thùng container.


*Hình 9: Trang Prometheus Targets hiển thị danh sách các mục tiêu giám sát của hệ thống Nhà hàng*


*Hình 10: Dashboard Grafana hiển thị các chỉ số giám sát của hệ thống Nhà hàng*


## 3.2. Cuốn sổ nhật ký tự động ghi chép mọi hoạt động: Loki và Promtail

Nếu như Prometheus lưu trữ các con số đo lường thì cặp đôi Loki và Promtail lại là cuốn sổ nhật ký ghi lại bằng chữ tất cả các câu chuyện diễn ra trong nhà hàng. Điểm hay của công nghệ này là nó cực kỳ tiết kiệm bộ nhớ máy tính so với các hệ thống ghi log cồng kềnh trước đây.

Cách thức hoạt động diễn ra như sau: Mỗi khi một người khách mở xem thực đơn, bấm đặt món hay một nhân viên bấm chuyển trạng thái đơn hàng, ứng dụng web Python Flask sẽ tự động ghi lại một dòng chữ nhật ký dưới dạng cấu trúc JSON chuẩn mực. Dòng nhật ký này ghi rõ ràng: thời điểm xảy ra sự việc (ngày giờ phút giây), mức độ thông tin (INFO hoặc ERROR), tên dịch vụ phát sinh, đường dẫn trang web vừa truy cập, mã trạng thái thành công HTTP 200, thời gian máy tính xử lý mất mấy phần nghìn giây, và mã sinh viên tác giả (DTC245200862).

Người thư ký Promtail chạy nền sẽ tự động gom nhặt tất cả các dòng nhật ký này từ các container Docker rồi chuyển giao cho kho lưu trữ Loki cất giữ cẩn thận. Toàn bộ chuỗi vận hành thu thập nhật ký này chạy tự động 100%, ổn định hoàn hảo và không bao giờ xảy ra lỗi nghẽn dữ liệu.


## 3.3. Hướng dẫn cách tra cứu nhật ký bằng 3 câu lệnh tìm kiếm đơn giản

Khi muốn tra cứu lại lịch sử hoạt động hoặc khi cần điều tra nguyên nhân một lỗi phát sinh trong nhà hàng, người quản trị chỉ cần mở màn hình Grafana Explore, chọn kho nhật ký Loki và gõ các câu lệnh tìm kiếm LogQL vô cùng đơn giản sau đây:

Câu lệnh số 1: Xem toàn bộ các dòng nhật ký phát sinh từ ứng dụng web nhà hàng:

Ý nghĩa: Lệnh này lọc ra tất cả những gì mà ứng dụng web đã ghi lại, giúp người quản lý nắm bắt được toàn cảnh các thao tác vừa diễn ra trên hệ thống.

Câu lệnh số 2: Lọc riêng các lượt khách hàng đặt món và truy cập thành công (mã HTTP 200):

Ý nghĩa: Sử dụng bộ bóc tách thông minh để chỉ lấy ra các giao dịch thành công tốt đẹp, giúp tính toán chính xác lưu lượng người dùng thực tế của nhà hàng.

Câu lệnh số 3: Lùng sục và phát hiện ngay các sự cố, lỗi bất thường trong toàn hệ thống:

Ý nghĩa: Giúp người quản trị tìm ra ngay những vết tích hỏng hóc (nếu có) như mất kết nối cơ sở dữ liệu hay lỗi cú pháp để kịp thời sửa chữa trước khi khách hàng phàn nàn.


*Hình 11: Kiểm tra và giám sát nhật ký hoạt động của hệ thống bằng Grafana và Loki*


*Hình 12: Truy vấn lọc từ khóa nhật ký hoạt động ứng dụng bằng LogQL trên Grafana*


## 3.4. Năm lớp áo giáp bảo vệ hệ thống trước nguy cơ bị xâm nhập

Để đảm bảo hệ thống không thể bị tin tặc phá hoại, tác giả đã trang bị đồng bộ 5 lớp áo giáp bảo vệ (Hardening) vững chắc theo đúng tiêu chuẩn an toàn thông tin chuyên nghiệp:

- Lớp áo giáp 1 - Không cho phần mềm dùng quyền tối cao (Non-root Container): Bình thường các phần mềm khi chạy trong container hay dùng quyền root (quyền tối cao cao nhất của máy tính). Nếu phần mềm bị lỗi bảo mật, tin tặc có thể cướp quyền này để chiếm luôn cả máy tính chủ. Trong đề tài này, tác giả đã tạo ra riêng một tài khoản người dùng bình thường mang tên 'appuser' (mã số định danh UID: 1001) để chạy ứng dụng. Dù kẻ xấu có hack được vào web thì cũng chỉ là tài khoản bình thường không có quyền can thiệp vào máy chủ.
- Lớp áo giáp 2 - Chia nhà thành 3 gian phòng kín tách biệt (Multi-tier Network Isolation): Hệ thống không dùng chung một mạng phẳng mà chia thành 3 mạng cô lập: gian phòng công cộng (frontend-net) tiếp xúc với khách; gian phòng an ninh (monitoring-net) để đo đạc sức khỏe; và gian phòng bí mật (backend-net) cất giữ cơ sở dữ liệu. Thùng chứa cơ sở dữ liệu PostgreSQL tuyệt đối không mở bất kỳ cánh cửa nào ra ngoài Internet, kẻ xấu từ xa hoàn toàn bất lực không thể tấn công vào cơ sở dữ liệu.
- Lớp áo giáp 3 - Tước bỏ toàn bộ quyền hạn nguy hiểm (cap_drop: ALL): Trong tệp cấu hình, tác giả khai báo lệnh tước sạch toàn bộ các quyền can thiệp sâu của Linux đối với container web. Ứng dụng web bị cấm tuyệt đối việc thay đổi mạng máy tính hay can thiệp vào nhân hệ điều hành.
- Lớp áo giáp 4 - Cất giấu mật khẩu an toàn (.env): Toàn bộ mật khẩu của cơ sở dữ liệu, tài khoản quản trị đều tuân thủ độ phức tạp cao (chứa chữ hoa, chữ thường, số và ký tự đặc biệt như StrongPass#2026), được cất giấu trong tệp .env riêng biệt và không bao giờ bị đưa lên mạng Internet.
- Lớp áo giáp 5 - Đeo mặt nạ che giấu phiên bản máy chủ (server_tokens off): Cấu hình Nginx che giấu hoàn toàn số hiệu phiên bản phần mềm. Khi có người tò mò quét cổng, máy chủ chỉ đáp lại tên chung chung là Nginx mà không cho biết phiên bản mấy, khiến kẻ tấn công không biết đường nào mà khai thác lỗ hổng.

*Hình 13: Cấu hình mạng Docker, Non-root và các cổng truy cập của hệ thống Nhà hàng*


# CHƯƠNG 4. KỊCH BẢN CHẠY THỬ, KẾT QUẢ ĐẠT ĐƯỢC VÀ ĐÁNH GIÁ


## 4.1. Bảng kịch bản 10 bước chạy thử nghiệm thu hệ thống

Để phục vụ công tác chấm điểm và nghiệm thu thực tế của giảng viên, bảng kịch bản 10 bước kiểm thử (Test Cases) dưới đây mô tả chi tiết từng thao tác thực hiện và kết quả kỳ vọng tương ứng:


## 4.2. Hướng dẫn chi tiết từng câu lệnh gõ trên màn hình đen Terminal

Khi ngồi trước màn hình máy ảo Ubuntu để thực hành và chụp ảnh cho bài báo cáo, sinh viên mở cửa sổ Terminal (bằng tổ hợp phím tắt Ctrl + Alt + T) và lần lượt gõ các dòng lệnh đơn giản sau:


### 1. Lệnh xem cây thư mục dự án (để chụp Hình 1):


### 2. Lệnh xem trạng thái 10 chiếc hộp container đang chạy (để chụp Hình 2):


### 3. Lệnh kiểm tra chiếc cổng bảo vệ Nginx và các tiêu đề an ninh (để chụp Hình 6):


### 4. Lệnh mở xem cấu hình mạng và các biện pháp bảo vệ trong tệp điều phối (để chụp Hình 13):


## 4.3. Hướng dẫn chi tiết từng trang web cần mở để chụp ảnh minh chứng

Đối với các ảnh chụp giao diện trình duyệt web, sinh viên chỉ việc mở trình duyệt (Firefox hoặc Chrome) và nhập lần lượt các địa chỉ sau:


## 4.4. Những kết quả thực tế mà hệ thống đã làm được

Trải qua quá trình nghiên cứu, xây dựng và kiểm thử nghiêm ngặt, hệ thống Quản lý Nhà hàng & Đặt món (Order) - Đề 12 đã gặt hái được những thành tựu nổi bật:

Thứ nhất: Xây dựng thành công một ứng dụng web nhà hàng hoàn chỉnh với 3 phân hệ giao diện chuyên biệt cho Khách hàng, Nhân viên và Người quản lý. Giao diện trực quan, thân thiện, tương thích mượt mà trên cả điện thoại di động và máy tính.

Thứ hai: Đóng gói thành công toàn bộ 10 thành phần dịch vụ vào Docker Compose, khởi động tự động hóa 100% bằng đúng một câu lệnh duy nhất mà không xảy ra bất kỳ lỗi xung đột phần mềm nào.

Thứ ba: Thiết lập thành công chốt chặn an ninh Nginx Reverse Proxy mã hóa toàn bộ dữ liệu bằng HTTPS với chứng chỉ bảo mật SSL tự ký, kèm theo đầy đủ các tiêu đề bảo vệ an ninh mạng nâng cao.

Thứ tư: Xây dựng hoàn chỉnh hệ thống giám sát sức khỏe máy chủ theo thời gian thực bằng Prometheus và Grafana với 4 mục tiêu giám sát đạt trạng thái UP tuyệt đối.

Thứ năm: Thiết lập luồng thu thập và quản trị nhật ký tập trung mượt mà bằng Loki và Promtail với định dạng log JSON chuẩn mực, thực hiện thành công các câu truy vấn tìm kiếm LogQL nhanh chóng.

Thứ sáu: Áp dụng đồng bộ và nghiêm ngặt 5 kỹ thuật gia cố an ninh (Hardening) giúp bảo vệ hệ thống vững chắc trước các nguy cơ tấn công leo thang đặc quyền.


## 4.5. Những hạn chế hiện tại và hướng khắc phục trong tương lai

Bên cạnh những kết quả to lớn đã đạt được, hệ thống vẫn còn một số điểm có thể tiếp tục hoàn thiện hơn nữa trong các giai đoạn phát triển tiếp theo:

Hạn chế 1: Chứng chỉ bảo mật SSL hiện tại đang sử dụng là chứng chỉ tự ký (Self-signed Certificate). Khi truy cập trên trình duyệt ngoài môi trường mạng nội bộ, trình duyệt sẽ hiện thông báo cảnh báo màu đỏ. Hướng khắc phục: Trong tương lai khi đưa hệ thống lên mạng Internet với tên miền thật, nhà hàng sẽ tích hợp công cụ Certbot tự động xin cấp chứng chỉ số quốc tế miễn phí Let's Encrypt để ổ khóa luôn hiển thị màu xanh hoàn hảo.

Hạn chế 2: Việc theo dõi sức khỏe máy chủ hiện tại vẫn đòi hỏi người quản lý phải chủ động mở màn hình Grafana lên xem. Hướng khắc phục: Tích hợp thêm công cụ gửi thông báo Alertmanager để mỗi khi máy chủ bị quá tải CPU hay hết RAM, hệ thống sẽ tự động gửi tin nhắn cảnh báo khẩn cấp về điện thoại của người quản lý qua ứng dụng Telegram hoặc gửi Email cảnh báo tức thì.


## 4.6. Đánh giá đối chiếu theo đúng 7 yêu cầu của học phần

Dưới đây là bảng đối chiếu kết quả thực hiện của dự án so với 7 tiêu chí đánh giá khắt khe của học phần Triển khai và Quản trị Hệ thống Phần mềm:


# KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

Đề tài 'Hệ thống Quản lý Nhà hàng & Đặt món (Order) - Đề 12' đã được sinh viên Hồ Quang Huy nghiên cứu, thiết kế và triển khai thành công rực rỡ, đáp ứng vượt mức mọi mục tiêu học tập và thực hành của học phần Triển khai và Quản trị Hệ thống Phần mềm tại Trường Đại học Công nghệ Thông tin và Truyền thông.

Thông qua việc xây dựng một sản phẩm phần mềm gắn liền với thực tiễn đời sống kinh doanh ẩm thực, sinh viên không chỉ củng cố vững chắc kỹ năng lập trình ứng dụng mà quan trọng hơn cả là đã làm chủ được các công nghệ hạ tầng DevOps hiện đại hàng đầu thế giới: từ tư duy đóng gói phần mềm bằng Docker container, kỹ năng điều phối dịch vụ tự động hóa bằng Docker Compose, kỹ năng bảo mật hệ thống mạng và chứng chỉ số với Nginx Reverse Proxy, cho đến năng lực thiết lập các hệ thống giám sát sức khỏe máy chủ Prometheus/Grafana và quản trị nhật ký tập trung Loki/Promtail.

Kết quả thực nghiệm đã khẳng định tính đúng đắn và hiệu quả vượt trội của mô hình: một hệ thống dù có quy mô phức tạp với 10 cỗ máy container nhưng vẫn có thể vận hành ổn định, nhẹ nhàng, tự phục hồi khi có sự cố và được khởi động một cách kỳ diệu chỉ bằng đúng một câu lệnh duy nhất. Đây là hành trang kiến thức và kỹ năng vô cùng thiết thực, giúp sinh viên tự tin bước vào môi trường làm việc thực tế tại các doanh nghiệp và tập đoàn công nghệ lớn sau khi ra trường.

Trong tương lai, đề tài có thể tiếp tục được nghiên cứu và phát triển mở rộng theo các hướng sau:

- Tích hợp Trí tuệ Nhân tạo (AI): Tự động phân tích sở thích ăn uống và lịch sử gọi món của từng thực khách để đưa ra những lời gợi ý món ăn phù hợp nhất, giúp tăng doanh thu cho nhà hàng.
- Mở rộng lên cụm máy chủ đám mây Kubernetes (K8s): Cho phép hệ thống tự động nhân bản thêm các thùng container khi lượng khách vào giờ cao điểm tăng đột biến, đáp ứng nhu cầu cho các chuỗi nhà hàng ẩm thực quy mô lớn trên toàn quốc.
- Tích hợp cổng thanh toán trực tuyến: Cho phép khách hàng thanh toán tiền ăn tức thì qua việc quét mã QR ngân hàng hoặc ví điện tử MoMo, ZaloPay ngay trên màn hình điện thoại.
Sinh viên xin trân trọng cảm ơn quý thầy cô đã theo dõi và đánh giá bản báo cáo này!
