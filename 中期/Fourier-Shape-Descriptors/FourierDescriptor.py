# python 2.7

import cv2 as cv
import numpy as np

def findDescriptor(img, resolution):
    """ findDescriptor(img) finds and returns the
    Fourier-Descriptor of the image contour"""
    # convert to gray image
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    # threshold
    ret, thresh = cv.threshold(imgray, 1, 255, 0)

    # detect contours
    contour, hierarchy = cv.findContours(
        thresh,
        cv.RETR_EXTERNAL,
        cv.CHAIN_APPROX_NONE)

    print contour[0].shape
    contour_array = contour[0][:, 0, :]
    # print contour_array.shape
    # contour_array = reconstruct_contour(contour_array, resolution)
    # print contour_array.shape

    contour_complex = np.empty(contour_array.shape[:-1], dtype=complex)
    contour_complex.real = contour_array[:, 0]
    contour_complex.imag = contour_array[:, 1]
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


def getFourierDescriptor(img, degree, resolution, idx=None):
    init_f = findDescriptor(img, resolution)
    recons_f = truncate_descriptor(init_f, degree)

    if idx is not None:
        draw_descriptors(init_f, resolution, "visualization/%d_before truc"%idx)
        draw_descriptors(recons_f, resolution, "visualization/%d_after truc"%idx)
       
    return recons_f

