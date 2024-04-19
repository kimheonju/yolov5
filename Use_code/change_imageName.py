import os

# 폴더 경로
folder_path = r'C:/Users/khj/Desktop/mallard duck'  # 본인의 폴더 경로로 변경

# 폴더 내 파일 목록 가져오기
file_list = os.listdir(folder_path)

# 파일 이름 변경 시작 번호
start_number = 0

# 폴더 내의 이미지 파일만 선택
for filename in file_list:
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        # 새 파일 이름 생성
        new_filename = f"mallard duck_{start_number}.jpg"  # 파일 확장자에 따라 변경
        start_number += 1

        # 파일 이름 변경
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)

print("파일 이름 변경이 완료되었습니다.")
