import numpy as np
import cv2 as cv

resolution = 512
thresh = 40
max_thresh = 255

if __name__ == "__main__":
    m_idx = 5;
    view_idx = 0;
    filename = '../render_output/m%d_%d_%dx%d.png'%(m_idx,view_idx,resolution,resolution)
    src_img = cv.imread(filename)

    # convert to gray image
    imgray = cv.cvtColor(src_img, cv.COLOR_BGR2GRAY)
    imgray = cv.blur(imgray,(3,3))

    # edges
    edges = cv.Canny(imgray, thresh, thresh*2)

    # threshold
    ret, thresh = cv.threshold(imgray, thresh, max_thresh, 0)

    # detect contours
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # draw contours
    blank = np.zeros(src_img.shape)
    for i in range(len(contours)):
        print(i)
        cv.drawContours(blank, contours, i, (0,255,0),1)
    
    cv.imshow('gray',imgray)
    cv.imshow('edges',edges)
    cv.imshow('c',blank)

    cv.imwrite('edges.png',edges)
    cv.imwrite('contour.png',blank)
