import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('test.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(gray,150,250,0)
contours= cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)[0]
for c in contours:
    area = cv.contourArea(c)
    print(area)
    if 500<area < 30000:
        x,y,w,h = cv.boundingRect(c)
        # cv.rectangle(img, (x-50,y-20),(x+w+50,y+h+20),(0,255,0),2)

        img1 = img[y-30: y+h+20, x-20:x+20+w]
        break

bise_not = cv.bitwise_not(img1)

img1 = cv.resize(bise_not, (28,28))
plt.imshow(img1, cmap='gray')

plt.show()

# arr = np.array([[[5, 8, 9], [5, 8, 9]], [[5, 8, 9], [5, 8, 9]], [[5, 8, 9], [5, 8, 9]]])
# for x in arr:
#     x[x>5 ] = 1
#     # x[x<1] = 0
# print(arr)