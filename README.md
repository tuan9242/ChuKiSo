# Ứng dụng Chữ ký số

Ứng dụng web cho phép ký và xác thực chữ ký số trên các file, sử dụng thuật toán RSA.

## Tính năng

- **Giao diện người dùng hiện đại và thân thiện**
  - Thiết kế responsive, tương thích với mọi thiết bị
  - Hiệu ứng chuyển động mượt mà
  - Giao diện trực quan, dễ sử dụng

- **Ký số file**
  - Hỗ trợ kéo thả file
  - Hiển thị thông tin file (tên, kích thước)
  - Tạo chữ ký số sử dụng RSA
  - Hiển thị chữ ký và public key
  - Sao chép nhanh chữ ký và public key

- **Xác thực chữ ký**
  - Tải lên file cần xác thực
  - Nhập chữ ký và public key
  - Kiểm tra tính toàn vẹn của file
  - Hiển thị kết quả xác thực rõ ràng

## Cài đặt

1. Clone repository:
```bash
git clone https://github.com/yourusername/digital-signature-app.git
cd digital-signature-app
```

2. Cài đặt các thư viện Python:
```bash
pip install -r requirements.txt
```

3. Chạy ứng dụng:
```bash
python app.py
```

4. Truy cập ứng dụng tại: `http://localhost:5000`,`http://localhost:5000/receiver`

## Cấu trúc dự án

```
digital-signature-app/
├── app.py              # File chính của ứng dụng
├── requirements.txt    # Danh sách thư viện Python
├── static/
│   └── style.css      # CSS styles
└── templates/
    ├── sender.html    # Trang gửi file
    └── receiver.html  # Trang xác thực
```

## Công nghệ sử dụng

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Thư viện**: 
  - Flask: Web framework
  - PyCrypto: Xử lý mã hóa RSA
  - Font Awesome: Icons
  - AOS: Thư viện animation

## Hướng dẫn sử dụng

### Ký số file

1. Truy cập trang chủ
2. Kéo thả file vào khu vực upload hoặc click để chọn file
3. Nhấn nút "Tải lên"
4. Sau khi xử lý, chữ ký và public key sẽ được hiển thị
5. Sử dụng nút "Sao chép" để lưu thông tin

### Xác thực chữ ký

1. Truy cập trang xác thực
2. Tải lên file cần xác thực
3. Nhập chữ ký và public key
4. Nhấn nút "Xác thực"
5. Xem kết quả xác thực

## Bảo mật

- Sử dụng thuật toán RSA cho chữ ký số
- Không lưu trữ thông tin nhạy cảm
- Xử lý file an toàn
- Bảo vệ chống tấn công XSS và CSRF
