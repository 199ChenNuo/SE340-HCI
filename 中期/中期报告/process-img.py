import cv2 as cv
 
 
def access_pixels(image):
    height, width, channels = image.shape
    print("width:%s,height:%s,channels:%s" % (width, height, channels))
 
    for row in range(height):
        for list in range(width):
            for c in range(channels):
                pv = image[row, list, c]
                image[row, list, c] = 255 - pv

    # cv.namedWindow('after', 0)
    # cv.resizeWindow('after', 4480, 640)
    cv.imshow('after', image)
 
 
src = cv.imread('t_5__before truc.png')
# cv.namedWindow("src",0);
# cv.resizeWindow("src", 480, 640);
cv.imshow("src",src)
 
t1 = cv.getTickCount()
access_pixels(src)
t2 = cv.getTickCount()
print("time cost:%s s" % ((t2 - t1) / cv.getTickFrequency()))
cv.waitKey()
