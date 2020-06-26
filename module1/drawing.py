import cv2
import numpy as np

#drawing line, circle, and rectangle over a canvas
canvas = np.zeros((300,300,3), dtype='uint8')

#draw green line
green = (0,255,0)
cv2.line(canvas, (0,0), (300,300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

red = (0,0,255) #opencv takes bgr, not rgb
cv2.line(canvas, (0,300), (300,0), red)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


#for rectange, we pass the top-left and bottom-right corner coordinates to the function
cv2.rectangle(canvas, (10,20), (120,170), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (150, 200), (220, 250), red, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


#reset canvas and get center of canvas for drawing circle
canvas = np.zeros((300,300,3), dtype='uint8')
(centerX, centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)
white = (255,255,255)

for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


