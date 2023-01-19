import cv2
import numpy as np
import matplotlib.pyplot as plt

# cam = cv2.VideoCapture("http://192.168.219.105:8080/video")
def canny(image):
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)  # RGB값을 조정해 회색으로 만듦
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # 5x5 커널을 활용해 가우시안 블러처리
    canny = cv2.Canny(blur, 50, 150)  # canny함수로 변형
    return canny


def region_of_interest(image):
    height = image.shape[0]  # y축 높이가 0이됨을 뜻함
    triangle = np.array(
        [(600, height), (1300, height), (850, 300)]
    )  # 삼각형의 공간을 x,y좌표계를 활용하여 가져온다
    mask = np.zeros_like(image)


while 1:

    # _, frame = cam.read()
    image = cv2.imread("road_test.jpg")  # 이미지를 가져옴
    lane_image = cv2.copy(image)  # 원본 이미지에 영향을 주지 않기 위해 copy 사용
    canny = canny(lane_image)

    cv2.imshow("result", canny)  # 이미지 보여줌

    if cv2.waitKey(1) == ord("q"):
        break  # q키 누르기 전까지 이미지 imshow
