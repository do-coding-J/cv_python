# import the opencv library
import cv2


# define a video capture object
camera = cv2.VideoCapture(0, cv2.CAP_V4L2)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

while(True):
	
	# Capture the video frame
	# by frame
	ret, frame = camera.read()

	# Display the resulting frame
	cv2.imshow('frame', frame)
	
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object
camera.release()
# Destroy all the windows
cv2.destroyAllWindows()