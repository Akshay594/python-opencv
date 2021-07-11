import cv2
import numpy as np

canvas = np.zeros((512,512, 3), np.uint8)
cv2.line(canvas, (0, 0), (511, 511), (255, 0, 0), 3)
cv2.rectangle(canvas, (0, 0), (400, 400), (0, 255, 0), 11)
cv2.putText(canvas, "Over 9000", 
	(200, 200),
	cv2.FONT_HERSHEY_SIMPLEX,
	1, 
	(0, 0, 255), 2)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)