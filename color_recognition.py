import cv2

img = cv2.imread("img/oranges.jpg")

print(img)



cv2.imshow("Original", img)
cv2.waitKey(0)
