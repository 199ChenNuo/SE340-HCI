import cv2
import numpy as np
from skimage import morphology
import skimage.io as io


def blur_demo(image):            
    kernel = np.ones((8,8),np.uint8)
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    dst = cv2.blur(opening, (1, 15))  
    cv2.namedWindow("avg_blur_demo", 0)
    cv2.resizeWindow("avg_blur_demo", 640, 480)  
    cv2.imshow("avg_blur_demo", dst)

    median_blur_demo(dst)
    

    # _,binary = cv2.threshold(dst, 0.1, 0 ,cv2.THRESH_BINARY_INV)
    # cv2.namedWindow("binary", 0)
    # cv2.resizeWindow("binary", 640, 480)
    # cv2.imshow("binary", binary)

    ''' remove_small_objects()'''
    # ski=morphology.remove_small_objects(dst,min_size=10)
    # cv2.namedWindow("ski", 0)
    # cv2.resizeWindow("ski", 640, 480)
    # cv2.imshow("ski", ski)
    '''remove_small_holes()'''
    # hole=morphology.remove_small_holes(dst,min_size=1)
    # hole = hole.astype(float)
    # # print hole
    # cv2.namedWindow("hole", 0)
    # cv2.resizeWindow("hole", 640, 480)
    # cv2.imshow("hole", hole)
    '''
    when the area of a contour is smaller than threshold, remova that contour
    '''
    # image,contours,hierarch=cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    # threshold = 10
    # for i in range(len(contours)):
    #     area = cv2.contourArea(contours[i])
    #     if area < threshold:
    #         cv2.drawContours(image,[contours[i]],0,0,-1)

    # gray = cv2.cvtColor(dst, cv2.COLOR_RGB2GRAY)
    # ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)

    # cv2.namedWindow("binary", 0)
    # cv2.resizeWindow("binary", 640, 480)
    # cv2.imshow("binary", binary)

    '''
    process through pixal, convert img to binary img
    '''
    # frame = dst
    # height = frame.shape[0]
    # weight = frame.shape[1]
    # channels = frame.shape[2]
    # print("weight : %s, height : %s, channel : %s" %(weight, height, channels))
    
    # for row in range(height):
    #     for col in range(weight):
    #         for c in range(channels):
    #             pv = frame[row, col, c]
    #             if(pv != 255):
    #                 frame[row, col, c] = 0
    # cv2.imshow("fanxiang", frame)

def median_blur_demo(image):
    dst = cv2.medianBlur(image, 9)
    cv2.namedWindow("midian",0)
    cv2.resizeWindow("midian", 640, 480)
    cv2.imshow("midian", dst)

def custom_blur_demo(image):
    kernel = np.ones([5, 5], np.float32)/25   
    dst = cv2.filter2D(image, -1, kernel)
    cv2.namedWindow("custom_blur_demo", 0)
    cv2.resizeWindow("custom_blur_demo", 640, 480)
    cv2.imshow("custom_blur_demo", dst)

cv2.namedWindow("src", 0)
cv2.resizeWindow("src", 640, 480)
src = cv2.imread("./images/1.jpg")
img = cv2.resize(src,None,fx=0.8,fy=0.8,interpolation=cv2.INTER_CUBIC)
cv2.imshow('src', img)

blur_demo(img)
# custom_blur_demo(img)

cv2.waitKey(0)
cv2.destroyAllWindows()
