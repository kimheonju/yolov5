import os

def delete_empty_txt_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            if os.path.getsize(file_path) == 0:  # 파일 크기가 0 바이트인 경우
                os.remove(file_path)  # 해당 파일 삭제

# 사용 예
folder_path = 'C:/Users/user/Desktop/thesis/yolov5/labels/test'
delete_empty_txt_files(folder_path)