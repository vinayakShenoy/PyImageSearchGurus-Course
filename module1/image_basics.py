import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="Path to image")
args = vars(ap.parse_args())

#display image
image = cv2.imread(args["image"])
(h,w) = image.shape[:2]
cv2.imshow("Original", image)

#access pixel
(b, g, r) = image[0, 0]
print("Pixel at (0,0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

#slicing image
(cX, cY) = (w//2, h//2)
tl = image[0:cY, 0:cX]
cv2.imshow("Top-left corner", tl)

tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)
cv2.waitKey(0)



