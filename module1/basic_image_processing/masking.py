'''
we can use a combination of both bitwise operations and masks to construct ROIs that are non-rectangular. 
This allows us to extract regions from images that are of completely arbitrary shape.
'''

import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and display it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

mask = np.zeros(image.shape[:2], dtype='uint8')
cv2.rectangle(mask, (0,90), (290,450), 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked", masked)

cv2.waitKey(0)
