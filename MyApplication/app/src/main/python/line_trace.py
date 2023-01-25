import cv2
import numpy as np
import matplotlib.pyplot as plt


def main():
    def canny(image):
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # RGB값을 조정해 회색으로 만듦
        blur = cv2.GaussianBlur(gray, (5, 5), 0)  # 5x5 커널을 활용해 가우시안 블러처리
        canny = cv2.Canny(blur, 50, 150)  # canny함수로 변형, RGB 값의 변화가 급격하게 생기는 부분만 나타냄
        return canny

    def region_of_interest(image):
        height = image.shape[0]  # y축 높이가 0이됨을 뜻함
        polygons = np.array(  # polygon:3D 객체를 이루는 여러개의 삼각형 입자를 말하는 것
            [[(0, height), (950, height), (480, 350)]]
        )  # 삼각형의 공간을 x,y좌표계를 polygon 중 하나로 임의로 지정한 뒤 가져온다.
        mask = np.zeros_like(
            image
        )  # image의 픽셀 갯수만큼의 zero matrix를 만든다. 이제 이 zero matrix의 공간에 triangle 만큼의 영역을 채운다
        cv2.fillPoly(
            mask, polygons, 255
        )  # fillpoly 함수는 여러개의 polygon에 대해 작동하기 때문에 polygons 변수에 하나의 polygon을 가진 배열이라고 정해놓은 것. polygons 변수가 나타내는 영역만 채운다.
        masked_image = cv2.bitwise_and(
            image, mask
        )  # mask 프레임과 image 프레임을 이진파일 상에서 AND연산을 시키면 polygon 영역의 값만 추출해낼 수 있음
        return masked_image

    def make_coordinates(image, line_parameters):
        try:
            slope, intercept = line_parameters
        except TypeError:
            slope, intercept = 0.001, 0
        y1 = image.shape[0]  # y축 맨 밑에서 시작
        y2 = int(y1 * (3 / 5))  # 바닦지점으로 부터 전체의 3/5지점까지가 경계
        x1 = int((y1 - intercept) / slope)
        x2 = int((y2 - intercept) / slope)
        return np.array([x1, y1, x2, y2])


    def average_slope_intercept(image, lines):
        left_fit = []
        right_fit = []
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            parameters = np.polyfit((x1, x2), (y1, y2), 1)
            slope = parameters[0]
            intercept = parameters[1]
            if slope < 0:
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))
        left_fit_average = np.average(left_fit, axis=0)
        right_fit_average = np.average(right_fit, axis=0)
        left_line = make_coordinates(image, left_fit_average)
        right_line = make_coordinates(image, right_fit_average)
        return np.array([left_line, right_line])

    def display_lines(image, lines):
        line_image = np.zeros_like(image)
        if lines is not None:
            for x1, y1, x2, y2 in lines:
                cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
        return line_image

    frame1 = cv2.imread("road_test.jpg")


    while 1:

        #frame1 = cam.read()
        # image = cv2.imread("road_test.jpg")  # 이미지를 가져옴
        frame = np.copy(frame1)  # 원본 이미지에 영향을 주지 않기 위해 copy 사용
        canny_image = canny(frame)
        cropped_image = region_of_interest(canny_image)
        lines = cv2.HoughLinesP(cropped_image,2,np.pi / 180,100,np.array([]),minLineLength=40,maxLineGap=5,)
        averaged_lines = average_slope_intercept(frame, lines)
        line_image = display_lines(frame, averaged_lines)
        combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
        cv2.imshow("result", combo_image)  # 이미지 보여줌
        cv2.waitKey(0)
    cam.release()
    cv2.destroyAllWindows