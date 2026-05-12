import cv2
image = cv2.imread("mountain.jpg", cv2.IMREAD_COLOR)

if image is None:
    print("Image not found.")
else:
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("Original Image: ", image)
    cv2.waitKey(0)
    cv2.imshow("HSV Image", hsv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()