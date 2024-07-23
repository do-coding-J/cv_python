import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("img/tennis.jpg")

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


horizontal_paste = np.hstack((img, hsv))

cv2.imshow("", horizontal_paste)
cv2.waitKey()