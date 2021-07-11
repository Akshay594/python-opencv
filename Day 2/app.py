import cv2
import numpy as np

image = cv2.imread('../images/goku.jpg')


zeros = np.zeros((image.shape[0], image.shape[1]), np.uint8)

b,g,r = cv2.split(image)
print("Blue channel: ", b)
print("Green channel: ", g)
print("Red channel: ", r)

# gray_image = cv2.imread('../images/goku.jpg', 0)

# gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# cv2.imshow("Frame Goku", image)
# cv2.imshow("Frame Goku Gray", gray_image)
blue = cv2.merge([b, zeros, zeros])
green = cv2.merge([zeros, g, zeros])
red = cv2.merge([zeros, zeros, r])

custom_image = cv2.merge([b, g+100, r])

# cv2.imshow('Blue', blue)
cv2.imwrite('BlueImage.png', blue)
# cv2.imshow('Red', red)
# cv2.imshow('Green', green)

# print(custom_image)
cv2.imshow('custom_image', custom_image)
cv2.waitKey(0)