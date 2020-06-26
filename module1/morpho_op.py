

'''
KERNELS
we think of an image as a big matrix,
then we can think of a kernel or convolutional matrix as a tiny matrix that is used for
blurring, sharpening, edge detection, and other image processing functions.
'''


'''
Morphological operations are simple transformations applied to binary or grayscale images.
More specifically, we apply morphological operations to shapes and structures inside of images.
Morphological operations “probe” an image with a structuring element.
This structuring element defines the neighborhood to be examined around each pixel.
And based on the given operation and the size of the structuring element we are able to adjust our output image.

Structuring element is a type of kernel or mask.
However, instead of applying a convolution, we are only going to perform simple tests on the pixels.

'''

import cv2
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-c", "--cimage", required=True, help="Path to car")
args = vars(ap.parse_args())
# load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

'''
1) Erosion: A foreground pixel in the input image will be kept only if ALL pixels inside the structuring element are > 0. Otherwise, the pixels are set to 0 (i.e. background).
 Useful for removing small blobs in an image or disconnecting two connected objects.
'''

for i in range(0,3):
    eroded = cv2.erode(gray.copy(), None, iterations=i+1)
    cv2.imshow("Eroded {} times".format(i+1), eroded)
    cv2.waitKey(0)


'''
2) Dilation: Opposite of erosion. Utilizes structuring elements - a center pixel p of the structuring element is set to white if ANY pixel in the structuring element is > 0.
useful for joining broken parts of an image together.
'''

cv2.destroyAllWindows()
cv2.imshow("Original", image)
for i in range(0,3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i+1)
    cv2.imshow("Dilated {} times".format(i+1), dilated)
    cv2.waitKey(0)


'''
3) Opening: Eroson followed by dilation.
allows us to remove small blobs from an image:
first an erosion is applied to remove the small blobs, then a dilation is applied to regrow the size of the original object.
'''

cv2.destroyAllWindows()
cv2.imshow("Original", image)
kernels = [(3,3), (5,5), (7,7)]

for kernelSize in kernels:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({},{})".format(kernelSize[0],kernelSize[1]), opening)
    cv2.waitKey(0)


'''
4) Closing: Dilation folowed by erosion
closing is used to close holes inside of objects or for connecting components together.

'''


cv2.destroyAllWindows()
cv2.imshow("Original", image)

for kernelSize in kernels:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing: ({},{})".format(kernelSize[0],kernelSize[1]), closing)
    cv2.waitKey(0)


'''
5) Morphological gradient: Difference between erosion and dilation
useful for determining the outline of a particular object of an image:
'''


cv2.destroyAllWindows()
cv2.imshow("Original", image)

for kernelSize in kernels:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    grad = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Gradient: ({},{})".format(kernelSize[0],kernelSize[1]), grad)
    cv2.waitKey(0)


'''
6) Top Hat/white hat: difference between original(grayscale) image and opening
used to reveal bright regions of an image on dark backgrounds.
'''

carImage = cv2.imread(args["cimage"])
carGray = cv2.cvtColor(carImage, cv2.COLOR_BGR2GRAY)
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13,5))
blackhat = cv2.morphologyEx(carGray, cv2.MORPH_BLACKHAT, rectKernel)
tophat = cv2.morphologyEx(carGray, cv2.MORPH_TOPHAT, rectKernel)

cv2.imshow("Original", carImage)
cv2.imshow("Tophat", tophat)
cv2.imshow("Blackhat", blackhat)
cv2.waitKey(0)





