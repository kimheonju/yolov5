import os
from PIL import Image
import subprocess

# 필요한 설정 파일 경로 설정
yaml_path = "C:/Users/khj/Desktop/animals/yolov5/models/yolov5.yaml"
test_yaml = "C:/Users/khj/Desktop/animals/yolov5/data.yaml"

# YOLOv5 레포지토리 폴더로 이동
yolov5_repo_path = "C:/Users/khj/Desktop/animals/yolov5"
os.chdir(yolov5_repo_path)

# 이미지 크기 조정 함수 정의
def resize_images(image_folder, output_folder, new_size):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg"):
            img = Image.open(os.path.join(image_folder, filename))
            img = img.resize(new_size, Image.BILINEAR)  # 이미지 크기 조정 (BILINEAR 알고리즘 사용)
            img.save(os.path.join(output_folder, filename))

# 이미지 크기 조정
input_images_folder = "C:/Users/khj/Desktop/animals/images"  # 이미지가 있는 폴더 경로 입력
output_images_folder = "C:/Users/khj/Desktop/animals/result"  # 크기 조정된 이미지를 저장할 폴더 경로 입력
new_image_size = (640, 640)  # 새로운 이미지 크기 (너비, 높이) 입력

resize_images(input_images_folder, output_images_folder, new_image_size)

# YOLOv5 모델 학습 명령어 실행 (GPU 0을 사용)
command = f"python train.py --img 640 --batch 16 --epochs 50 --data {test_yaml} --weights yolov5m.pt --project=C:/Users/khj/Desktop/animals/result --name new_data_yolov5m_results --exist-ok"
os.system(command)

def evaluate_model():
    # YOLOv5 레포지토리 폴더로 이동
    yolov5_repo_path = "C:/Users/khj/Desktop/animals/yolov5"
    os.chdir(yolov5_repo_path)

    # YOLOv5 모델 평가 명령어 실행
    evaluate_command = f"python test.py --data {test_yaml} --weights C:/Users/khj/Desktop/animals/result/new_yolov5m_results/weights/best.pt" \
        " --batch-size 16"
    subprocess.run(evaluate_command, shell=True)

# 모델 평가 함수 호출
mAP50 = evaluate_model()
