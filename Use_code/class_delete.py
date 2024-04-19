import os

def remove_class_4_lines(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        for line in lines:
            parts = line.split()
            if not parts:  # 빈 라인이거나 예상치 못한 형식의 라인을 스킵
                continue
            class_num = int(parts[0])
            if class_num != 4:  # 클래스 넘버가 4가 아닌 라인만 저장
                f.write(line)

def remove_class_4_lines_from_all_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):  # 텍스트 파일만 처리
            input_file = os.path.join(folder_path, filename)
            output_file = os.path.join(folder_path, "temp_" + filename)
            remove_class_4_lines(input_file, output_file)
            os.remove(input_file)  # 원래 파일 삭제
            os.rename(output_file, input_file)  # 임시 파일의 이름을 원래 파일의 이름으로 변경

# 사용 예
folder_path = 'C:/Users/user/Desktop/thesis/yolov5/labels/val'
remove_class_4_lines_from_all_files_in_folder(folder_path)