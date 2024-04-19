import os
import shutil

def classify_txt_files_matching_images(image_folder, txt_folder, dest_folder):
    # 디렉토리가 존재하지 않는 경우 생성
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # 이미지 파일 디렉토리에서 파일 목록 가져오기
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png'))]
    image_names = [os.path.splitext(f)[0] for f in image_files]  # 확장자 제거

    # TXT 파일 디렉토리에서 이미지 이름과 동일한 TXT 파일 찾아서 이동
    for file in os.listdir(txt_folder):
        if file.endswith('.txt') and os.path.splitext(file)[0] in image_names:
            src = os.path.join(txt_folder, file)
            dest = os.path.join(dest_folder, file)
            shutil.move(src, dest)

if __name__ == "__main__":
    image_folder = "6/val_img"
    txt_folder = "label"
    dest_folder = "6/val_txt"

    classify_txt_files_matching_images(image_folder, txt_folder, dest_folder)