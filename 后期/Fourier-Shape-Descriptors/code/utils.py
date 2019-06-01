# python 2.7

import cv2 as cv
import numpy as np

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

    answer_size = answer.shape[0]
    answer = answer.reshape(answer_size,1)

    print answer_SVM
    success_rate_SVM = np.count_nonzero(answer_SVM==answer) *1.0/ answer_size
    
    return success_rate_SVM 
"""SVM END"""

"""Minimum distance classifier"""
def KNN(training_set, response, test_set, answer):
    knn = cv.ml.KNearest_create()
    knn.train(training_set, cv.ml.ROW_SAMPLE,response)
    ret, answer_KNN, neignbours, distance = knn.findNearest(test_set, 3)

    answer_size = answer.shape[0]
    answer = answer.reshape(answer_size,1)

    print answer_KNN
    success_rate_KNN = np.count_nonzero(answer_KNN==answer) *1.0/ answer_size
    return success_rate_KNN

"""Minimum distance classifier END"""




def processImg(im):
    imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    img = 255 - imgray
    
    return img