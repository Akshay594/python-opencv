import cv2

image1 = cv2.imread('goku.jpg')
image2 = cv2.imread('background.jpg')
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

added_image = image1 + image2
blended_image = cv2.addWeighted(image1, 0.3, image2, 0.7, gamma=0.5)

cv2.imshow("Added Image", added_image)
cv2.imshow("Blendedage", blended_image)
cv2.waitKey(0)
