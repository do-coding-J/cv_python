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
cv2.setTrackbarPos("minDist", "Trackbar Windows", 500)
cv2.createTrackbar("param1", "Trackbar Windows", 100, 1000, onChange)
cv2.setTrackbarPos("param1", "Trackbar Windows", 50)
cv2.createTrackbar("param2", "Trackbar Windows", 1, 100, onChange)
cv2.setTrackbarPos("param2", "Trackbar Windows", 30)
cv2.createTrackbar("minRad", "Trackbar Windows", 0, 1000, onChange)
cv2.setTrackbarPos("minRad", "Trackbar Windows", 0)
cv2.createTrackbar("maxRad", "Trackbar Windows", 0, 1000, onChange)
cv2.setTrackbarPos("maxRad", "Trackbar Windows", 100)

while True:

    # Capture the video frame
    # by frame
    
#######################
    
    current_time = time.time() - prev_time

    # if current_time > 1./ FPS :
    if True:
        prev_time = time.time()
        ret, frame = camera.read()
        
        
#######################

        minDist = cv2.getTrackbarPos("minDist", "Trackbar Windows")
        param1 = cv2.getTrackbarPos("param1", "Trackbar Windows")
        param2 = cv2.getTrackbarPos("param2", "Trackbar Windows")
        minRad = cv2.getTrackbarPos("minRad", "Trackbar Windows")
        maxRad = cv2.getTrackbarPos("maxRad", "Trackbar Windows")

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray,5)

        circle = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 0.5, minDist, param1 = param1, param2 = param2, minRadius = minRad, maxRadius = maxRad)
        if circle is None:
            continue
        else:
            circle = np.uint16(np.round(circle))
            
        for i in circle[0, :]:
            # draw the outer circle
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)


#######################
    # Display the resulting frame
    # cv2.imshow("frame", res)
    cv2.imshow("normal", frame)
    # cv2.imshow("gray", gray)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    

# After the loop release the cap object
camera.release()
# Destroy all the windows
cv2.destroyAllWindows()
