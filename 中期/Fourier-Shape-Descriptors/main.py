# python 2.7

import cv2 as cv
import numpy as np
from FourierDescriptor import getFourierDescriptor

MIN_DESCRIPTOR = 120  # surprisingly enough, 2 descriptors are already enough
TRAINING_SIZE = 1000
RESOLUTION = 512
MODEL_NUM = 20

def addNoise(descriptors):
    """this function adds gaussian noise to descriptors
    descriptors should be a [N,2] np array"""
    scale = descriptors.max() / 10
    noise = np.random.normal(0, scale, descriptors.shape[0])
    noise = noise + 1j * noise
    descriptors += noise


def sample_generater(descriptors):
    """this function generates training_set, also for testing"""
    response = np.arange(MODEL_NUM)
    response = np.tile(response, TRAINING_SIZE / MODEL_NUM)
  
    training_set = np.empty(
        [TRAINING_SIZE, MIN_DESCRIPTOR], dtype=np.float32)
    # assign descriptors with noise to our training_set
    for i in range(TRAINING_SIZE / MODEL_NUM):
        for j in range(MODEL_NUM):
            descriptors_sample = descriptors[j].copy()
            addNoise(descriptors_sample)
            training_set[i*MODEL_NUM + j] = np.absolute(descriptors_sample)
        
    return training_set, response


"""SVM START"""
def SVM(training_set, response, test_set, answer):
    svm_model = cv.ml.SVM_create()
    # set up parameters for SVM
    svm_model.setKernel(cv.ml.SVM_LINEAR)
    svm_model.setType(cv.ml.SVM_C_SVC)
    svm_model.setC(2.67)
    svm_model.setGamma(5.383)
    svm_model.train(training_set, cv.ml.ROW_SAMPLE, response)

    answer_SVM = svm_model.predict(test_set)
    answer_SVM = np.array(answer_SVM)[1]
    #print answer_SVM
    answer = answer.reshape(TRAINING_SIZE,1)
    #print answer
    success_rate_SVM = np.count_nonzero(answer_SVM==answer) *1.0/ TRAINING_SIZE
    
    return success_rate_SVM 
"""SVM END"""

"""Minimum distance classifier"""
def KNN(training_set, response, test_set, answer):
    knn = cv.ml.KNearest_create()
    knn.train(training_set, cv.ml.ROW_SAMPLE,response)
    ret, answer_KNN, neignbours, distance = knn.findNearest(test_set, 3)
    answer = answer.reshape(TRAINING_SIZE,1)

    success_rate_KNN = np.count_nonzero(answer_KNN==answer) *1.0/ TRAINING_SIZE
    return success_rate_KNN

"""Minimum distance classifier END"""


if __name__ == "__main__":
    descriptors = []
    # import images and treat
    for idx in range(MODEL_NUM):
        imgname = '../render_output/m%d_0_512x512.png'%idx
        print "processing m%d_0_512x512.png ... "%idx
        img = cv.imread(imgname)       

        """Mission 1: Calculate fourier descriptor
        and reconstruct using minimum amout of descriptors"""
        fourier_result = getFourierDescriptor(img, MIN_DESCRIPTOR, RESOLUTION, idx)
        np.save('Descriptors/%d_descriptor_%d.npy'%(idx, MIN_DESCRIPTOR), fourier_result)
        """Mission 1 END"""

        descriptors.append(fourier_result)
    
    descriptors = np.array(descriptors)

    """generate training_set"""
    training_set, response = sample_generater(descriptors)
    test_set, correct_answer = sample_generater(descriptors)    
    """generate training_set END"""

    print "Descriptor Number: %d"%MIN_DESCRIPTOR
    success_rate_SVM = SVM(training_set, response, test_set, correct_answer)
    print 'For SVM, success rate (0~1) = '+ str(success_rate_SVM)

    success_rate_KNN = KNN(training_set, response, test_set, correct_answer)
    print 'For KNN, success_rate_KNN (0~1) = ' + str(success_rate_KNN)

# """Bayers classifier"""
# bayers_model = cv.ml.NormalBayesClassifier()
# bayers_model.train(training_set, response)
# retval, answer_bayers = bayers_model.predict(test_set)
# success_rate_bayers = np.sum(
#     np.in1d(
#         correct_answer,
#         answer_bayers)) / TRAINING_SIZE
# print("For bayers_model, success_rate_bayers =  ", success_rate_bayers)
# """Bayers classifier END"""
