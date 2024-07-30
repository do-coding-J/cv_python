# import the opencv library
import cv2
import numpy as np

# define a video capture object
camera = cv2.VideoCapture(0, cv2.CAP_V4L2)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc("M", "J", "P", "G"))


def onChange(pos):
    pass

cv2.namedWindow("Trackbar Windows")
cv2.createTrackbar("low r", "Trackbar Windows", 0, 255, onChange)
cv2.setTrackbarPos("low r", "Trackbar Windows", 100)
cv2.createTrackbar("low g", "Trackbar Windows", 0, 255, onChange)
cv2.setTrackbarPos("low g", "Trackbar Windows", 0)
cv2.createTrackbar("low b", "Trackbar Windows", 0, 255, onChange)
cv2.setTrackbarPos("low b", "Trackbar Windows", 20)
cv2.createTrackbar("high r", "Trackbar Windows", 0, 255, onChange)
cv2.setTrackbarPos("high r", "Trackbar Windows", 255)
cv2.createTrackbar("high g", "Trackbar Windows", 0, 255, onChange)
cv2.setTrackbarPos("high g", "Trackbar Windows", 255)
cv2.createTrackbar("high b", "Trackbar Windows", 0, 255, onChange)
cv2.setTrackbarPos("high b", "Trackbar Windows", 70)

while True:

    # Capture the video frame
    # by frame
    ret, frame = camera.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # blue
    # lower_color = np.array([110,50,50])
    # upper_color = np.array([130,255,255])
    
    # white
    lower_color = np.array([0,0,0])
    upper_color = np.array([50,255,255])
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    low_r = cv2.getTrackbarPos("low r", "Trackbar Windows") # 0
    low_g = cv2.getTrackbarPos("low g", "Trackbar Windows") # 50
    low_b = cv2.getTrackbarPos("low b", "Trackbar Windows") # 30
    high_r = cv2.getTrackbarPos("high r", "Trackbar Windows") # 255
    high_g = cv2.getTrackbarPos("high g", "Trackbar Windows") # 255
    high_b = cv2.getTrackbarPos("high b", "Trackbar Windows") # 10

    # green
    lower_color = np.array([low_b, low_g, low_r])
    upper_color = np.array([high_b, high_g, high_r])
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the resulting frame
    cv2.imshow("frame", res)
    cv2.imshow("normal", frame)
    cv2.imshow("mask", mask)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# After the loop release the cap object
camera.release()
# Destroy all the windows
cv2.destroyAllWindows()
