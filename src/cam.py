# import the opencv library
import cv2
import numpy as np
import time

FPS = 30
prev_time = time.time()

# define a video capture object
camera = cv2.VideoCapture(0, cv2.CAP_V4L2)
ret, frame = camera.read()
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc("M", "J", "P", "G"))

#######################

width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('default resolution width {} height {}'.format(width, height))

# 1280x720 해상도로 변경 시도
print('set resolution width {} height {}'.format(1280, 720))
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('default resolution width {} height {}'.format(width, height))

#######################

while True:

    # Capture the video frame
    # by frame
    ret, frame = camera.read()
    
#######################
    
    current_time = time.time() - prev_time

    if current_time > 1./ FPS :
    # if True:
        prev_time = time.time()
        
#######################

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        low_r = 100
        low_g = 10
        low_b = 15
        high_r = 255
        high_g = 255
        high_b = 110

        # green
        lower_color = np.array([low_b, low_g, low_r])
        upper_color = np.array([high_b, high_g, high_r])

        mask = cv2.inRange(hsv, lower_color, upper_color)

        res = cv2.bitwise_and(frame, frame, mask=mask)

#######################

        minDist = 100 # 500
        param1 = 50
        param2 = 30
        minRad = 0
        maxRad = 100

        gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray,5)

        circle = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 0.5, minDist, param1 = param1, param2 = param2, minRadius = minRad, maxRadius = maxRad)
        if circle is None:
            continue
        else:
            circle = np.uint16(np.round(circle))
            
        for i in circle[0, :]:
            # draw the outer circle
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            print("obj{} X: {}\t Y: {}".format(i, i[0], i[1]))

#######################
    # Display the resulting frame
    cv2.imshow("frame", frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    

# After the loop release the cap object
camera.release()
# Destroy all the windows
cv2.destroyAllWindows()
