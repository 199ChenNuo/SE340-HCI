import cv2 as cv
import numpy as np

def findContour(img, verbose=False):
    # convert to gray image
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
    if verbose:   
        cv.imshow("gray", imgray)
        cv.waitKey(-1)    

    # edges
    edges = cv.Canny(imgray, 30, 40)
    if verbose:  
        cv.imshow("edges", edges)
        cv.waitKey(-1)

    # threshold
    ret, thresh = cv.threshold(edges, 1, 255, 0)

    # dilation    
    kernel = np.ones((9,9),np.uint8)  
    dilation = cv.dilate(thresh,kernel,iterations = 1)
    if verbose:  
        cv.imshow("dila", dilation)
        cv.waitKey(-1)

    # detect contours
    contour, hierarchy = cv.findContours(
        dilation,
        cv.RETR_EXTERNAL,
        cv.CHAIN_APPROX_NONE)

    def func(x,y):
        a = x.shape[0]
        b = y.shape[0]
        if a<b:
            return 1
        if a==b:
            return 0
        else:
            return -1
            
    contour.sort(cmp=func)

    # for c in contour:
    #     print c.shape

    return contour[0]