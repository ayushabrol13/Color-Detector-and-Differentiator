import cv2

img = cv2.imread("img/orange.png")

print(img)

cv2.imshow("Original", img)
cv2.waitKey(0)
