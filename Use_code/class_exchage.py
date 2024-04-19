import os

def update_labels(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        for line in lines:
            parts = line.split()
            class_num = int(parts[0])
            if class_num == 5:
                parts[0] = '4'
            #elif class_num == 6:
            #    parts[0] = '5'
            f.write(' '.join(parts) + '\n')

def update_all_labels_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):  # 텍스트 파일만 처리
            input_file = os.path.join(folder_path, filename)
            output_file = os.path.join(folder_path, "updated_" + filename)
            update_labels(input_file, output_file)
            os.remove(input_file)  # 원래 파일 삭제
            os.rename(output_file, input_file)  # 업데이트된 파일의 이름을 원래 파일의 이름으로 변경

# 사용 예
folder_path = 'D:/make_mallardduck/valid/labels'
update_all_labels_in_folder(folder_path)