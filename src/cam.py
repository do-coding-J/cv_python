# import the opencv library
import cv2
import numpy as np
import time

# define a video capture object
camera = cv2.VideoCapture(0, cv2.CAP_V4L2)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc("M", "J", "P", "G"))

FPS = 30
prev_time = time.time()


def onChange(pos):
    pass

cv2.namedWindow("Trackbar Windows")
cv2.createTrackbar("minDist", "Trackbar Windows", 1, 1000, onChange)
cv2.setTrackbarPos("minDist", "Trackbar Windows", 100)
cv2.createTrackbar("param1", "Trackbar Windows", 100, 1000, onChange)
cv2.setTrackbarPos("param1", "Trackbar Windows", 250)
cv2.createTrackbar("param2", "Trackbar Windows", 1, 100, onChange)
cv2.setTrackbarPos("param2", "Trackbar Windows", 10)
cv2.createTrackbar("minRad", "Trackbar Windows", 0, 1000, onChange)
cv2.setTrackbarPos("minRad", "Trackbar Windows", 80)
cv2.createTrackbar("maxRad", "Trackbar Windows", 0, 1000, onChange)
cv2.setTrackbarPos("maxRad", "Trackbar Windows", 120)

while True:

    # Capture the video frame
    # by frame
    ret, frame = camera.read()
    
#######################
    
    current_time = time.time() - prev_time

    if (ret is True) and (current_time > 1./ FPS) :
        prev_time = time.time()
        
#######################

        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # # green
        # lower_color = np.array([30, 50, 0])
        # upper_color = np.array([100, 255, 255])

        # mask = cv2.inRange(hsv, lower_color, upper_color)

        # res = cv2.bitwise_and(frame, frame, mask=mask)

#######################

        minDist = cv2.getTrackbarPos("minDist", "Trackbar Windows")
        param1 = cv2.getTrackbarPos("param1", "Trackbar Windows")
        param2 = cv2.getTrackbarPos("param2", "Trackbar Windows")
        minRad = cv2.getTrackbarPos("minRad", "Trackbar Windows")
        maxRad = cv2.getTrackbarPos("maxRad", "Trackbar Windows")

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        circle = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, minDist, param1 = param1, param2 = param2, minRadius = minRad, maxRadius = maxRad)
        circle = np.uint16(np.round(circle))
        for i in circle[0, :]:
            # draw the outer circle
            cv2.circle(gray, (i[0], i[1]), i[2], (0, 255, 0), 2)


#######################
        # Display the resulting frame
        # cv2.imshow("frame", res)
        # cv2.imshow("normal", frame)
        cv2.imshow("gray", gray)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    

# After the loop release the cap object
camera.release()
# Destroy all the windows
cv2.destroyAllWindows()
