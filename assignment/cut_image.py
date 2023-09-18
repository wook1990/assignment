import cv2
import os
import math
import random
import glob
import sys
def cut_imgae(image_path, cols, rows) -> None:

    # image cutting
    # 이미지 로드
    img = cv2.imread(image_path)
    # 이미지 해상도 확인
    h, w = img.shape[:2]
    # print(h,w)
    # 이미지 분할 -> 입력받은 매트릭 개로 분할
    # 가로, 세로 크기 계산
    crop_h = (h / rows if (h / rows).is_integer() else math.trunc(h / rows))
    crop_w = (w / cols if (w / cols).is_integer() else math.trunc(w / cols))
    # print(crop_h, crop_w)

    # col by row 이미지 자르기
    cropped_images = []

    for i in range(rows):
        for j in range(cols):
            left = int(j * crop_w)
            top = int(i * crop_h)
            right = int((j + 1) * crop_w)
            bottom = int((i + 1) * crop_h)
            cropped_image = img[int(top):int(bottom), int(left):int(right)]

            # 분할된 이미가 각 50%의 확률로 미러링, 플립핑, 90도 변환이 되록하여 아웃풋 이미지들을 만들어 낸뒤 저장

            # mirroring (좌우)
            if random.random() > 0.5:
                cropped_image = cv2.flip(cropped_image, 1)
                # print("mirroring is done")
            # flipping (상하)
            if random.random() > 0.5:
                cropped_image = cv2.flip(cropped_image, 0)
                # print("flipping is done")
            # 90도변환
            if random.random() > 0.5:
                cropped_image = cv2.rotate(cropped_image, cv2.ROTATE_90_CLOCKWISE)
                # print("rotatind is done")

            cropped_images.append(cropped_image)

    # 이미지 저장 -> 정보를 알 수 없게
    if not os.path.exists("image/crooped_images/"):
        os.mkdir("image/crooped_images/")
    else:
        [os.remove(f) for f in glob.glob("image/crooped_images/*.jpg")]

    for img in cropped_images:
        cv2.imwrite(f"image/crooped_images/cropped_{int(round(random.random(), 7) * 10000000)}.jpg", img)


if __name__ == "__main__":


    cols, rows = int(sys.argv[1]), int(sys.argv[2])
    try:
        image_path = sys.argv[3]
    except:
        image_path = "image/origin.jpeg"
     
       
    cut_imgae(image_path, cols, rows)
