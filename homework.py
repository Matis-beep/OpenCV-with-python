import cv2

img = cv2.imread("boat.jpg", 1)
cv2.imshow("boat", img)
img1 = cv2.imread("boat.jpg", 0)
cv2.imshow("boat black n white", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()