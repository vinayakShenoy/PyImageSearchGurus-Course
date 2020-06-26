import cv2
import numpy as np
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True, help="Image")
args = vars(ap.parse_args())

#load and display image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#get center of image
(h,w) = image.shape[:2]
(cx, cy) = (w//2, h//2)

#rotate image by 45 degrees and scale 1
M = cv2.getRotationMatrix2D((cx,cy), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Rotated by 45 degrees", rotated)

rotated = imutils.rotate(image, 80)
cv2.imshow("Rotated using 80 degrees counter-clock", rotated)
cv2.waitKey(0)



