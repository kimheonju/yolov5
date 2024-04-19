import os

def list_unmatched_files(labels_folder, images_folder):
    # 라벨링 파일 이름들을 가져옵니다. (확장자 제거)
    labeled_files = [os.path.splitext(filename)[0] for filename in os.listdir(labels_folder) if filename.endswith('.txt')]
    
    # 이미지 폴더의 파일 이름들을 가져옵니다. (확장자 제거)
    image_files = [os.path.splitext(filename)[0] for filename in os.listdir(images_folder) if filename.endswith('.jpg') or filename.endswith('.png')]
    
    # 라벨링이 없는 이미지 파일 이름들을 출력합니다.
    for image_file in image_files:
        if image_file not in labeled_files:
            print(f"Missing label for image: {image_file}.jpg")
    
    # 이미지가 없는 라벨링 파일 이름들을 출력합니다.
    for label_file in labeled_files:
        if label_file not in image_files:
            print(f"Missing image for label: {label_file}.txt")

# 사용 예
labels_folder = 'C:/Users/user/Desktop/thesis/yolov5/labels/val'
images_folder = 'C:/Users/user/Desktop/thesis/yolov5/images/val'
list_unmatched_files(labels_folder, images_folder)