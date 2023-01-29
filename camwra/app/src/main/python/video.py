import cv2
import numpy as np
import meshio as ms
def canny(img):
    #pic=Image.open(io.BytesIO(bytes(img)))
    #image=np.array(pic)

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # RGB값을 조정해 회색으로 만듦
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # 5x5 커널을 활용해 가우시안 블러처리
    canny = cv2.Canny(blur, 50, 150)  # canny함수로 변형, RGB 값의 변화가 급격하게 생기는 부분만 나타냄
    ret_canny=ms.read("canny.Mat")
    return canny