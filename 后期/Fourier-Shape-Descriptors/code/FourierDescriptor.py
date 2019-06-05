# python 2.7

import cv2 as cv
import numpy as np

from contour import findContour

# def findContour(img):
#     # convert to gray image
#     imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)    
#     # cv.imshow("gray", imgray)
#     # cv.waitKey(-1)
    

#     # edges
#     edges = cv.Canny(imgray, 30, 40)
#     # cv.imshow("edges", edges)
#     # cv.waitKey(-1)

#     # threshold
#     ret, thresh = cv.threshold(edges, 1, 255, 0)
#     # cv.imshow("thresh", thresh)
#     # cv.waitKey(-1)

#     # dilation    
#     kernel = np.ones((9,9),np.uint8)  
#     dilation = cv.dilate(thresh,kernel,iterations = 1)
#     # cv.imshow("dila", dilation)
#     # cv.waitKey(-1)

#     # detect contours
#     contour, hierarchy = cv.findContours(
#         dilation,
#         cv.RETR_EXTERNAL,
#         cv.CHAIN_APPROX_NONE)

#     for c in contour:
#         print c.shape
#     # print contour.shape
#     return contour[0]

def findDescriptor(img):
    """ findDescriptor(img) finds and returns the
    Fourier-Descriptor of the image contour"""
    contour = findContour(img)

    x, y, w, h = cv.boundingRect(contour)
    contour_array = contour[:, 0, :]

    contour_complex = np.empty(contour_array.shape[:-1], dtype=complex)
    contour_complex.real = contour_array[:, 0] - x
    contour_complex.imag = contour_array[:, 1] - y
    fourier_result = np.fft.fft(contour_complex)

    return fourier_result


def truncate_descriptor(descriptors, degree):
    """this function truncates an unshifted fourier descriptor array
    and returns one also unshifted"""
    descriptors = np.fft.fftshift(descriptors)
    center_index = len(descriptors) / 2
    descriptors = descriptors[
        center_index - degree / 2:center_index + degree / 2]
    descriptors = np.fft.ifftshift(descriptors)

    return descriptors

# Make fourier descriptor invariant to rotaition and start point
def rotataionInvariant(fourierDesc):
    for index, value in enumerate(fourierDesc):
        fourierDesc[index] = np.absolute(value)

    return fourierDesc    

# Make fourier descriptor invariant to scale
def scaleInvariant(fourierDesc):
    firstVal = fourierDesc[0]

    for index, value in enumerate(fourierDesc):
        fourierDesc[index] = value / firstVal

    return fourierDesc

# Make fourier descriptor invariant to translation
def transInvariant(fourierDesc):
    
    return fourierDesc[1:len(fourierDesc)]

def draw_descriptors(descriptors, resolution, name):
    """ reconstruct(descriptors, degree) attempts to reconstruct the image
    using the first [degree] descriptors of descriptors"""
    # truncate the long list of descriptors to certain length
    
    contour_reconstruct = np.fft.ifft(descriptors)
    contour_reconstruct = np.array(
        [contour_reconstruct.real, contour_reconstruct.imag])
    contour_reconstruct = np.transpose(contour_reconstruct)
    contour_reconstruct = np.expand_dims(contour_reconstruct, axis=1)

    # make positive
    if contour_reconstruct.min() < 0:
        contour_reconstruct -= contour_reconstruct.min()
    # normalization
    contour_reconstruct *= resolution / contour_reconstruct.max()
    # type cast to int32
    contour_reconstruct = contour_reconstruct.astype(np.int32, copy=False)
    black = np.zeros((resolution,resolution), np.uint8)

    cv.drawContours(black, contour_reconstruct, -1, 255, thickness=-1)
    cv.imwrite(name+".png", black)


def getFourierDescriptor(img, degree, resolution, name=None):
    init_fDesc = findDescriptor(img)
    rot_fDesc = rotataionInvariant(init_fDesc.copy())
    scale_fDesc = scaleInvariant(rot_fDesc.copy())
    trans_fDesc = transInvariant(scale_fDesc.copy())
    trunc_fDesc = truncate_descriptor(trans_fDesc.copy(), degree)

    if name is not None:
        draw_descriptors(init_fDesc, resolution, "../visualization/%s_init"%name)
        draw_descriptors(rot_fDesc, resolution, "../visualization/%s_after rot"%name)
        draw_descriptors(scale_fDesc, resolution, "../visualization/%s_after scale"%name)
        draw_descriptors(trans_fDesc, resolution, "../visualization/%s_after trans"%name)
        draw_descriptors(trunc_fDesc, resolution, "../visualization/%s_after trunc"%name)

    return trunc_fDesc

