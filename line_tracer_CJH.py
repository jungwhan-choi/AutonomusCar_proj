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
    polygons = np.array(  # polygon:3D 객체를 이루는 여러개의 삼각형 입자를 말하는 것
        [[(600, height), (1300, height), (850, 300)]]
    )  # 삼각형의 공간을 x,y좌표계를 polygon 중 하나로 임의로 지정한 뒤 가져온다.
    mask = np.zeros_like(
        image
    )  # image의 픽셀 갯수만큼의 zero matrix를 만든다. 이제 이 zero matrix의 공간에 triangle 만큼의 영역을 채운다
    cv2.fillPoly(
        mask, polygons, 255
    )  # fillpoly 함수는 여러개의 polygon에 대해 작동하기 때문에 polygons 변수에 하나의 polygon을 가진 배열이라고 정해놓은 것.
    return mask  # mask는 그림에서 따오고 싶은 부분만의 영역을 rgb값을 밝게 처리하고 나머지는 0으로 처리한 프레임


while 1:

    # _, frame = cam.read()
    image = cv2.imread("road_test.jpg")  # 이미지를 가져옴
    lane_image = np.copy(image)  # 원본 이미지에 영향을 주지 않기 위해 copy 사용
    canny = canny(lane_image)

    cv2.imshow("result", region_of_interest(canny))  # 이미지 보여줌
    cv2.waitKey(0)
    if cv2.waitKey(1) == ord("q"):
        break  # q키 누르기 전까지 이미지 imshow
