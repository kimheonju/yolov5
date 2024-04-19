import os

def remove_unlabeled_images(labels_folder, images_folder):
    # 라벨링 파일 이름들을 가져옵니다. (확장자 제거)
    labeled_files = [os.path.splitext(filename)[0] for filename in os.listdir(labels_folder) if filename.endswith('.txt')]
    
    # 이미지 폴더를 순회하면서 라벨링이 없는 이미지를 삭제합니다.
    for filename in os.listdir(images_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):  # 다른 확장자도 필요하면 추가
            name_without_ext = os.path.splitext(filename)[0]
            if name_without_ext not in labeled_files:
                os.remove(os.path.join(images_folder, filename))

# 사용 예
labels_folder = 'C:/Users/khj/Desktop/animals/labels/val'
images_folder = 'C:/Users/khj/Desktop/animals/images/val'
remove_unlabeled_images(labels_folder, images_folder)