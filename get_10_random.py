import os
import random
import shutil

def collect_random_images_from_each_subdir(source_dir, target_dir, num_images_per_subdir=10):
    # Tạo thư mục đích nếu chưa tồn tại
    os.makedirs(target_dir, exist_ok=True)

    # Duyệt qua các thư mục con trong thư mục gốc
    for subdir in os.listdir(source_dir):
        subdir_path = os.path.join(source_dir, subdir)
        if os.path.isdir(subdir_path):
            all_images = []
            
            # Thu thập tất cả các ảnh trong thư mục con
            for file in os.listdir(subdir_path):
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                    all_images.append(os.path.join(subdir_path, file))

            # Nếu số lượng ảnh ít hơn số yêu cầu, điều chỉnh lại số lượng ảnh cần lấy
            num_images_to_select = min(num_images_per_subdir, len(all_images))
            
            # Lấy ngẫu nhiên các ảnh từ danh sách
            selected_images = random.sample(all_images, num_images_to_select)
            
            # Sao chép các ảnh đã chọn sang thư mục đích
            for image in selected_images:
                shutil.copy(image, target_dir)
                print(f'Đã sao chép: {image} đến {target_dir}')

# Ví dụ sử dụng
source_directory = '105_classes_pins_dataset'  # Thư mục gốc
target_directory = 'B'  # Thư mục đích
collect_random_images_from_each_subdir(source_directory, target_directory)
