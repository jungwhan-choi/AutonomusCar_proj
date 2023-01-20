import cv2
import numpy as np
import matplotlib.pyplot as plt

cam = cv2.VideoCapture("test.mp4")
_, frame = cam.read()

lane_image = np.copy(frame)
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
canny = cv2.Canny(blur, 50, 150)
plt.imshow(canny)
plt.show()
