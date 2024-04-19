import os

# 폴더 경로 설정
folder_path = 'C:/Users/khj/Desktop/animals/labels/train'  # 실제 폴더 경로로 변경해주세요.

# 클래스 아이디 설정
target_class_id = 1  # 찾고자 하는 클래스 아이디

# 해당 폴더 내의 모든 txt 파일 찾기
txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

# 해당 클래스 아이디를 가진 파일의 수를 저장할 변수 초기화
class_count = 0

# 각 txt 파일을 순회하며 클래스 아이디 확인
for txt_file in txt_files:
    file_path = os.path.join(folder_path, txt_file)
    with open(file_path, 'r') as file:
        first_line = file.readline()
        first_line = first_line.split()  # 공백으로 분리하여 첫 번째 숫자 추출
        if len(first_line) > 0 and int(first_line[0]) == target_class_id:
            class_count += 1

# 찾은 클래스 아이디를 가진 파일의 수 출력
print(f"클래스 아이디 {target_class_id}를 가진 파일의 수: {class_count}")