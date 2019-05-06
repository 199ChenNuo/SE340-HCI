# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 14:56:27 2019

@author: jwjiang
"""

import cv2
import numpy as np

inputImgPath = 'D:\\github\\SE340-HCI\\m5_0_512x512.png' 
outputImgPath = 'D:\\github\\SE340-HCI\\m5_0_512x512.txt' 


# featureSun:计算特征点个数
featureSum = 0
img = cv2.imread(inputImgPath)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

detector = cv2.xfeatures2d.SIFT_create()
# 找到关键点
kps , des = detector.detectAndCompute(gray,None)
# 绘制关键点
img=cv2.drawKeypoints(gray,kps,img)

# 将特征点保存
np.savetxt(outputImgPath ,des ,  fmt='%.2f')
featureSum += len(kps)
cv2.imshow('result',img)
cv2.waitKey(0)
print('kps:' + str(featureSum))
