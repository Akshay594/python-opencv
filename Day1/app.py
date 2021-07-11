import cv2

cap = cv2.VideoCapture(0)

while True:
	flag, frame = cap.read()
	if not flag:
		print('Could not access the camera')
		break
	cv2.imshow('frame', frame)
	k = cv2.waitkey(1)
	if k == ord('q'):
		break


cap.release()
cv2.destroyAllWindows()