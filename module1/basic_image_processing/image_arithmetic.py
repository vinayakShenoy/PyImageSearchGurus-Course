'''
NumPy will perform modulus arithmetic and wrap around.
OpenCV, on the other hand, will perform clipping and ensure pixel values never fall outside the range [0, 255].
'''

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

#using cv2.add or subtract, the values get clipped if it goes beyond [0,255]
#print("Max of 255: {}".format(str(cv2.add(np.uint8(200), np.uint8(100)))))
#print("Min of 0", cv2.subtract(np.uint8(100), np.uint8(200)))

#using numpy addition and subtraction
#print("wrap around1", np.uint8(240)+np.uint8(50))
#print("wrap around2", np.uint8(40)-np.uint8(200))

M = np.ones(image.shape, dtype='uint8')*100
added = cv2.add(image, M)
cv2.imshow("added", added)

M = np.ones(image.shape, dtype='uint8')*50
subtracted = cv2.subtract(image, M)
cv2.imshow("subtracted", subtracted)
cv2.waitKey(0)
