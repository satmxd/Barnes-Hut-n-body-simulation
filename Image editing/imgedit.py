import cv2
import numpy as np
import os

from matplotlib import pyplot as plt

dir = "D:\\Users\\Satvik\\Documents\\Data\\Entertainment\\Coding\\GIT\\Barnes-Hut-n-body-simulation\\src\\frames"
i = 0
for filename in os.scandir(dir):
    if filename.is_file():
        img = cv2.imread(filename.path)
        bimg = cv2.GaussianBlur(img, (7,7),0)
        simg = cv2.resize(img, (300,300))

        # gauss_noise=np.array((0,),dtype=np.uint8)
        # cv2.randn(gauss_noise,10,100)
        # gauss_noise=(gauss_noise*0.5).astype(np.uint8)
        # nimg=cv2.add(simg,gauss_noise)
        cv2.imwrite(f'updated-frames\\{filename.name}', simg)
        i+= 1

cv2.waitKey(0)
cv2.destroyAllWindows()