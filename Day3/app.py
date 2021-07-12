import cv2
import numpy as np

image = cv2.imread('goku.jpg')
print(image)
height, width, channels = image.shape
# Matrix
M = np.float32([[1, 0, 50], [0, 1, 50]])

#
rotation_matrix = cv2.getRotationMatrix2D((height/2, width/2), -40, 2)
translated_image = cv2.warpAffine(image, M, (height, width))
rotated_image = cv2.warpAffine(image, rotation_matrix, (height, width))
scaled_image = cv2.resize(image, None, fx=5, fy=2)

# cv2.imshow("Image", image)
# cv2.imshow("translated image", translated_image)
cv2.imshow("rotated image", rotated_image)
# cv2.imwrite("Rotated.jpg", rotated_image)
print("I am a print statement.")
# cv2.imshow("scaled image", scaled_image)

cv2.waitKey(0)
