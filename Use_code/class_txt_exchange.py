import os

def change_label_in_files(target_directory='.'):
    # 지정된 디렉토리 내의 모든 파일을 탐색합니다.
    for filename in os.listdir(target_directory):
        filepath = os.path.join(target_directory, filename)
        # 파일 이름에 'sparrow'가 포함되어 있고, 텍스트 파일이면
        if 'sparrow' in filename and filename.endswith('.txt'):
            with open(filepath, 'r') as f:
                lines = f.readlines()
            
            # 각 라인에 대해 클래스 아이디 2를 5로 변경합니다.
            new_lines = [line.replace('1 ', '5 ', 1) if line.startswith('1 ') else line for line in lines]
            
            with open(filepath, 'w') as f:
                f.writelines(new_lines)

# 폴더 경로를 지정합니다.
directory = "C:/Users/khj/Desktop/Hard Hat Sample.v7i.yolov5pytorch/test/labels"
change_label_in_files(directory)