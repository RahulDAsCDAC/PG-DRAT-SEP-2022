import cv2

video = cv2.VideoCapture(0)

if (video.isOpened() == False):
	print("Error reading video file")

frame_width = int(video.get(3))
frame_height = int(video.get(4))

size = (frame_width, frame_height)

result = cv2.VideoWriter('filename.mp4',
						cv2.VideoWriter_fourcc(*'mp4v'),
						30, size)
	
while(True):
	ret, frame = video.read()
	if ret == True:
		result.write(frame)
		cv2.imshow('Frame', frame)
		# Press 'q' to close app
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

video.release()
result.release()
cv2.destroyAllWindows()
print("The video was successfully saved")