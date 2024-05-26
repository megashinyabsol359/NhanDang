import cv2
from deepface import DeepFace
import os
import time

def count_faces_with_timer(directory):
 

    # Khởi tạo bộ đếm ảnh và thời gian bắt đầu
    count_detected = 0
    start_time = time.time()

    # Đếm số lượng tệp trong thư mục
    num_files = len(os.listdir(directory))

    # Tạo tên thư mục output dựa trên tên thư mục gốc
    output_dir = f"{directory}_output"

    # Tự động tạo thư mục output nếu chưa tồn tại
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Duyệt qua tất cả tệp tin trong thư mục
    for filename in os.listdir(directory):
        img_path = os.path.join(directory, filename)

        # Đọc ảnh
        img = cv2.imread(img_path)
        print(f"Xử lý ảnh: {img_path}")

        # Bắt đầu tính thời gian xử lý ảnh
        start_image_time = time.time()

        try:
            # Sử dụng DeepFace để phát hiện khuôn mặt
            faces = DeepFace.extract_faces(img_path)

            # Cập nhật bộ đếm ảnh có khuôn mặt
            count_detected += 1

            # Vẽ bounding box cho mỗi khuôn mặt
            # Vẽ bounding box cho mỗi khuôn mặt
            for face in faces:
                # Lấy thông tin bounding box
                x = face['facial_area']['x']
                y = face['facial_area']['y']
                w = face['facial_area']['w']
                h = face['facial_area']['h']

                # Vẽ bounding box trên ảnh (tùy chọn)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Tạo tên tệp output với tên gốc và tiền tố "face_"
            output_filename = f"face_{filename}"

            # Lưu ảnh có bounding box vào thư mục output
            cv2.imwrite(os.path.join(output_dir, output_filename), img)

            # Tính toán thời gian xử lý ảnh
            image_processing_time = time.time() - start_image_time
            print(f"Thời gian xử lý ảnh: {image_processing_time:.2f} giây")
        except ValueError as error:
            print(f"Lỗi: {error}")
            # Bỏ qua ảnh này và không tính vào bộ đếm
            pass

    # Tính toán tổng thời gian thực thi
    total_time = time.time() - start_time

    # In thông tin
    print(f"\nĐã xử lý {num_files} ảnh trong thư mục '{directory}'.")
    print(f"Tổng số hình đếm được: {count_detected}")
    print(f"Tổng thời gian thực thi: {total_time:.2f} giây")
    print(f"Ảnh có bounding box được lưu trong thư mục '{output_dir}'.")

    return count_detected

# Ví dụ sử dụng cho pos
directory = "pos"  # Thay đổi thư mục này theo ý bạn
count_detected = count_faces_with_timer(directory)

# In số lượng ảnh có khuôn mặt được phát hiện
print(f"Số lượng ảnh có khuôn mặt: {count_detected}")

print(f"")
 
# Ví dụ sử dụng cho neg
#directory = "neg"  # Thay đổi thư mục này theo ý bạn
#count_detected = count_faces_with_timer(directory)

# In số lượng ảnh có khuôn mặt được phát hiện
#print(f"Số lượng ảnh có khuôn mặt: {count_detected}")
