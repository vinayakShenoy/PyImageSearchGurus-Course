# Flip image around either x or y axis

import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#flip horizontally
flipped = cv2.flip(image, 1)
cv2.imshow("Horizontal flip", flipped)

#flip vertically
flipped = cv2.flip(image, 0)
cv2.imshow("Vertical flip", flipped)

cv2.waitKey(0)

