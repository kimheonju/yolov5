import os

def rename_files_in_directory(directory_path):
    # 지정된 디렉토리 내의 모든 파일을 가져옴
    files = os.listdir(directory_path)

    # 이미지 파일만 필터링 (확장자 기준: jpg, png, jpeg)
    image_files = [f for f in files if f.endswith(('.jpg', '.png', '.jpeg'))]

    # 각 이미지 파일에 대해 이름 변경
    for idx, image_file in enumerate(image_files):
        # 새 파일 이름 생성
        new_name = f"sparrow_{idx}.jpg"
        old_path = os.path.join(directory_path, image_file)
        new_path = os.path.join(directory_path, new_name)
        
        os.rename(old_path, new_path)
        print(f"{image_file} -> {new_name}")

# 예시로 사용할 경우:
directory_path = "D:/sparrow"  # 변경하고자 하는 디렉토리 경로 지정
rename_files_in_directory(directory_path)