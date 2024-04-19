import os

def count_files_with_class_id(target_directory='.', class_id='5'):
    file_count = 0
    # 지정된 디렉토리 내의 모든 파일을 탐색합니다.
    for filename in os.listdir(target_directory):
        filepath = os.path.join(target_directory, filename)
        # 파일 이름에 'goose'가 포함되어 있고, 텍스트 파일이면
        if 'sparrow' in filename and filename.endswith('.txt'):
            with open(filepath, 'r') as f:
                content = f.read()

            # 클래스 아이디가 1인 라벨이 파일에 포함되어 있으면 카운트를 증가시킵니다.
            if f"{class_id} " in content:
                file_count += 1
            
    return file_count

# 폴더 경로를 지정합니다.
directory = "C:/Users/khj/Desktop/animals/labels/val"
result = count_files_with_class_id(directory)
print(f"클래스 아이디 1이 포함된 텍스트 파일 수: {result}")