import cv2
import numpy as np

cap = cv2.VideoCapture('video.mp4')
# cap = cv2.VideoCapture(0)

while cap.isOpened():
	sucess, frame = cap.read()
	print(sucess)
	if sucess:
		print("Yay!!! We got the video.")
		gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('Gray Frame', gray_frame)
		cv2.imshow('Frame', frame)

		k = cv2.waitKey(50)
		if k & 0xff == ord('q'):
			break
	else:
		print("Sed Lyf :( :(")
		break

cap.release()
cv2.destroyAllWindows()
