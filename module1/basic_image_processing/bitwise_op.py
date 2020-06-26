#part of process of extracting ROI in images
#AND, OR, XOR, NOT

import cv2
import numpy as np

canvas1 = np.zeros((300,300), dtype='uint8')
cv2.rectangle(canvas1, (25, 25), (275,275), 255, -1)
cv2.imshow("Rect", canvas1)

canvas2 = np.zeros((300,300), dtype='uint8')
cv2.circle(canvas2, (150,150), 150, 255, -1)
cv2.imshow("Circle", canvas2)

bitwiseAnd = cv2.bitwise_and(canvas1, canvas2)
cv2.imshow("AND",bitwiseAnd)

bitwiseOR = cv2.bitwise_or(canvas1, canvas2)
cv2.imshow("OR", bitwiseOR)

bitwiseXOR = cv2.bitwise_xor(canvas1, canvas2)
cv2.imshow("XOR", bitwiseXOR)

bitwiseNOT = cv2.bitwise_not(canvas1)
cv2.imshow("NOT", bitwiseNOT)
cv2.waitKey(0)
