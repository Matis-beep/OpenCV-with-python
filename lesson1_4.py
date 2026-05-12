import cv2

img1 = cv2.imread("room.png")
img2 = cv2.imread("man.png")
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
weightedSum = cv2.addWeighted(img1, 0.5, img2, 0.4, 0)

cv2.imshow("Weighted Image", weightedSum)
cv2.waitKey(0)
cv2.destroyAllWindows()