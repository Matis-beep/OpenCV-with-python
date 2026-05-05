import cv2

img = cv2.imread("sand.jpg", 1)
cv2.imshow("Sand Image", img)
img1 = cv2.imread("sand.jpg", 0)
cv2.imshow("Sand Black and White Image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
