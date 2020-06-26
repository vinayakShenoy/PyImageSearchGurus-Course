#translation is shifting of image along the x and y axis.
import argparse
import cv2
import numpy as np
import imutils

#construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original",image)

#Translating image is given by a Numpy Matrix
#M = [[1,0,shiftX], [0,1,shiftY]]

M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted down and right", shifted)

M = np.float32([[1, 0, -25], [0, 1, -50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and left", shifted)


shifted = imutils.translate(image, 40, 100)
cv2.imshow("Using imutils", shifted)

cv2.waitKey(0)



