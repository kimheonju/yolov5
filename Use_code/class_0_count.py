import os

def count_empty_txt_files(folder_path):
    empty_file_count = 0
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            if os.path.getsize(file_path) == 0:  # 파일 크기가 0 바이트인 경우
                empty_file_count += 1

    return empty_file_count

# 사용 예
folder_path = 'D:/make_mallardduck/test/labels'
empty_count = count_empty_txt_files(folder_path)
print(f"0 바이트인 txt 파일 개수: {empty_count}")