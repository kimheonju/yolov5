import cv2
import os

def improve_image_quality(input_path, output_path):
    # 이미지를 불러옵니다.
    img = cv2.imread(input_path)
    
    # 이미지의 크기를 가져옵니다.
    height, width = img.shape[:2]
    
    # 이미지 화질 개선을 위해 이미지를 업스케일링합니다.
    upscaled = cv2.resize(img, (width, height), interpolation=cv2.INTER_LANCZOS4)
    
    # 결과를 저장합니다.
    cv2.imwrite(output_path, upscaled)

# 폴더 경로
folder_path = r'C:/Users/khj/Desktop/sparrow'  # 본인의 폴더 경로로 변경

# 폴더 내의 이미지 파일만 선택
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        # 파일 경로 설정
        input_file_path = os.path.join(folder_path, filename)
        output_file_path = input_file_path  # 출력 파일 경로를 입력 파일 경로로 설정

        # 이미지 화질 개선만 수행
        improve_image_quality(input_file_path, output_file_path)

print("이미지 화질 개선이 완료되었습니다.")
