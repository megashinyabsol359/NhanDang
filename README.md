# Hướng dẫn sử dụng
## Môi trường và thư viện: 
+ Ngôn ngữ: python 3.12 (nhớ chọn cài pip)
+ Thư viện deepface (pip install deepface)
+ Công cụ sử dụng khi test thử: visual studio code

## Cách sử dụng
- Mở file main.py trên một editor/IDE, thay đổi biến directory tới đường dẫn thư mục có ảnh cần nhận dạng có khuôn mặt con người
- Sử dụng hàm count_faces_with_timer(directory)
  + Biến directory là đường dẫn tới thư mục chứa các file ảnh (VD: d:\data\images)
- Sau khi hàm chạy xong sẽ thông báo kết quả trên console & sẽ tạo một thư mục có thêm hậu tố "_output" để lưu hình đã được khoanh đỏ phần khuôn mặt (VD: d:\data\images_output)

## Mẫu để test thử nhận dạng
- Ở đây có kèm theo 2 thư mục chứa ảnh để test thử phần nhận dạng
  + Thư mục pos: chứa ảnh có khuôn mặt người
  + Thự mục neg: chứa ảnh không có khuôn mặt người

## Kết quả test thử nhận dạng
