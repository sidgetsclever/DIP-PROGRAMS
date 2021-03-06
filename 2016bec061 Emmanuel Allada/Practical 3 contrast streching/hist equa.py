# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:23:38 2019

@author: Admin
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'D:\Btech practicals\DIP\lena5.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(gray)
cv2.imshow("Gray_original",gray)
p=[]
for i in range(512):
    for j in range(512):
        k=gray[i][j]
        if k<64:
            gray[i][j]=0
        elif k>63 and k<128:
            gray[i][j]=80
        elif k>127 and k<194:
            gray[i][j]=160
        elif k>193 and k<256:
            gray[i][j]=255
cv2.imwrite('Quantized_image.jpg',gray)
cv2.imshow("Gray_histogram",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()