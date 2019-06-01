# python 2.7

import cv2 as cv
import numpy as np
import argparse
from FourierDescriptor import getFourierDescriptor

MIN_DESCRIPTOR = 100  # surprisingly enough, 2 descriptors are already enough
RESOLUTION = 512
MODEL_NUM = 20
MODEL_DIR = '../render_output/'
DATA_DIR= '../data/'
CAND_NUM = 5


# Core match function
def match(tpFD, spFDs):
    # dist store the distance, same order as spContours
    dist = []
    
    n = len(spFDs)
    print "sample descriptor size: ", n

    for i in range(n):
        spFD = spFDs[i][0]
        classID = spFDs[i][1]
        # Calculate Euclidean distance between templete and testee
        dist.append( (classID, np.linalg.norm(np.array(spFD)-np.array(tpFD))) )
    
    def takeSecond(elem):
        return elem[1]

    dist.sort(key=takeSecond)
    return dist

def initDescriptor():
    # load model view img
    descriptors = []
    for idx in range(MODEL_NUM):
        imgname = MODEL_DIR + 'm%d_0_512x512.png'%idx
        print "processing m%d_0_512x512.png ... "%idx
        img = cv.imread(imgname)       

        """Mission 1: Calculate fourier descriptor
        and reconstruct using minimum amout of descriptors"""
        fourier_result = getFourierDescriptor(img, MIN_DESCRIPTOR, RESOLUTION, "m_%d_"%idx)
        """Mission 1 END"""

        descriptors.append([fourier_result,idx])    

    descriptors = np.array(descriptors)
    np.save(DATA_DIR+'descriptors.npy', descriptors)

def main(figureName, init=False):
    if init:
        initDescriptor()
     
    # load model descriptors
    descriptors = np.load(DATA_DIR+'descriptors.npy',allow_pickle=True)

    # load and test Stick figure
    img = cv.imread(figureName)   
    if img is None:
        print "invalid figure: %s"%(figureName)
        return

    print "test figure [%s] ... "%(figureName) 
    fourier_result = getFourierDescriptor(img, MIN_DESCRIPTOR, RESOLUTION, None)
    np.save(DATA_DIR+'%s.npy'%figureName.split('/')[-1].split('.')[0], fourier_result)

    dist = match(fourier_result, descriptors);
    
    for i in range(CAND_NUM):
        print dist[i]

    # test_set = []
    # answer = []
    # for idx in range(MODEL_NUM):
    #     img = cv.imread('../pics/m%d.jpg'%idx)   
    #     if img is None:
    #         continue  
    #     print "test m%d.jpg ... "%idx
    #     answer.append(idx)
    #     """Mission 1: Calculate fourier descriptor
    #     and reconstruct using minimum amout of descriptors"""
    #     fourier_result = getFourierDescriptor(img, MIN_DESCRIPTOR, RESOLUTION, "t_%d_"%idx)
    #     """Mission 1 END"""

    #     dist = match(fourier_result, descriptors);
    #     #print dist
    #     print dist[0:5]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', action='store', dest='figure_name',
            help='Stick figure name')

    parser.add_argument('-n', action='store', dest='cand_num', 
            default=5, type=int,
            help='Candidate model number')

    parser.add_argument('-I', action='store_true', default=False,
            dest='init_model',
            help='Whether to initiate model descriptor')

    results = parser.parse_args()

    CAND_NUM = results.cand_num
    main(results.figure_name, results.init_model)
        



