import os
import shutil

def classify_images_with_txt_name(txt_folder, image_folder, dest_folder):
    # 디렉토리가 존재하지 않는 경우 생성
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # TXT 파일 디렉토리에서 파일 목록 가져오기
    txt_files = [f for f in os.listdir(txt_folder) if f.endswith('.txt')]
    txt_names = [os.path.splitext(f)[0] for f in txt_files]  # 확장자 제거

    # 이미지 디렉토리에서 TXT 이름과 동일한 이미지 찾아서 이동
    for file in os.listdir(image_folder):
        if file.endswith(('.jpg', '.png')) and os.path.splitext(file)[0] in txt_names:
            src = os.path.join(image_folder, file)
            dest = os.path.join(dest_folder, file)
            shutil.move(src, dest)

if __name__ == "__main__":
    txt_folder = "../labels/train_txt"  # TXT 파일들이 저장된 디렉터리
    image_folder = "../동물 데이터/data"  # 모든 이미지들이 저장된 디렉터리
    dest_folder = "../6/train_img"  # 선택된 이미지들을 이동할 디렉터리

    classify_images_with_txt_name(txt_folder, image_folder, dest_folder)
