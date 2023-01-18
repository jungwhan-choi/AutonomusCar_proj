import cv2
import numpy as np

cam = cv2.VideoCapture("http://192.168.219.105:8080/video")

while 1:
    _, frame = cam.read()
    image = cv2.imread("road_test.jpg")  # 이미지를 가져옴
    lane_image = np.copy(image)  # 원본 이미지에 영향을 주지 않기 위해 copy 사용
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)  # RGB값을 조정해 회색으로 만듦
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # 5x5 커널을 활용해 가우시안 블러처리
    canny = cv2.Canny(blur, 50, 150)
    cv2.imshow("result", canny)  # 이미지 보여줌
    cv2.waitKey(0)  # 키 누르기 전까지 이미지 imshow 유지
