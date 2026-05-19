import cv2
import numpy as np




image = cv2.imread("plane.jpg")

kernel = np.ones((5, 5), np.uint8)

eroded_image = cv2.erode(image, kernel)

cv2.imshow("Errored Image", eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread("plane.jpg")

cv2.imshow("Original Image", image)
cv2.waitKey(0)

gaussian = cv2.GaussianBlur(image, (9, 9), 0)
cv2.imshow("Gaussian", gaussian)
cv2.waitKey(0)

median = cv2.medianBlur(image, 5)
cv2.imshow("median", median)
cv2.waitKey(0)

bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow("Bilateral filter", bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()