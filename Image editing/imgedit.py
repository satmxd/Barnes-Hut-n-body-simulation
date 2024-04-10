import cv2
import numpy as np
import os

from matplotlib import pyplot as plt

dir = "D:\\Users\\Satvik\\Documents\\Data\\Entertainment\\Coding\\GIT\\Barnes-Hut-n-body-simulation\\Pygame\\frames"
i = 0
for filename in os.scandir(dir):
    if filename.is_file():
        img = cv2.imread(filename.path,0)
        bimg = cv2.GaussianBlur(img, (5,5),0)
        simg = cv2.resize(bimg, (300,300))
        gauss_noise=np.zeros((300,300),dtype=np.uint8)
        cv2.randn(gauss_noise,10,40)
        gauss_noise=(gauss_noise*0.5).astype(np.uint8)
        nimg=cv2.add(simg,gauss_noise)
        cv2.imwrite(f'updated-frames\\{filename.name}', nimg)
        i+= 1

cv2.waitKey(0)
cv2.destroyAllWindows()