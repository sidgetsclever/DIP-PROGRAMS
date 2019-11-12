# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:52:35 2019

@author: Neha Kala
"""



import cv2
from matplotlib import pyplot as plt
img=cv2.imread("lenagray.jpg")

for r in range(0,255):
    for c in range(0,255):
        if img[:,:,1][r][c]>=0 and img[:,:,1][r][c]<64:
            img[:,:,1][r][c]=0
        elif img[:,:,1][r][c]>=64 and img[:,:,1][r][c]<125:
            img[:,:,1][r][c]=80
        elif img[:,:,1][r][c]>=125 and img[:,:,1][r][c]<191:
            img[:,:,1][r][c]=160
        elif img[:,:,1][r][c]>=191 and img[:,:,1][r][c]<255:
            img[:,:,1][r][c]=255

img[:,:,0]=img[:,:,1]
img[:,:,2]=img[:,:,1]
plt.imshow(img)





