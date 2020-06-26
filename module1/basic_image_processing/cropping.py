#removing parts of image we dont want
#Region of Interest

import cv2

image = cv2.imread("../load_display_save/florida_trip.png")
cv2.imshow("Original", image)

#crop face
face = image[85:250, 85:220]
cv2.imshow("Face", face)
cv2.waitKey(0)
