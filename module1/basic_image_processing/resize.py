import cv2
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True, help="Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

r = 150.0/image.shape[1]
dim = (150, int(image.shape[0]*r))

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("resized", resized)

resized = imutils.resize(image, width=100)
cv2.imshow("resized using imutils", resized)

cv2.waitKey(0)


#interpolation methods
## cv2.INTER_AREA
## cv2.INTER_NEAREST
## cv2.INTER_LINEAR
## cv2.INTER_CUBIC
## cv2.INTER_LANCZOS4

