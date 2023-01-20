# import  OpenCV
import cv2

# Access WebCam
cam = cv2.VideoCapture(0)

while(True):
	# Access frames
	ret, frame = cam.read()

	# Display the resulting frame
	cv2.imshow('Frame', frame)
	
	# Press 'q' to close
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# Realease WebCam
cam.release()

# CLose All Windows
cv2.destroyAllWindows()