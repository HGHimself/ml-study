import numpy as np
import math
from random import random

def randomNumber( bottom, spread ):
    return bottom + (math.floor(random() * spread * 10)) % spread

def nTo4bit( n ):
    return np.array([ [int(n&b==b)] for b in [8,4,2,1] ])

def vectorized_result(j):
    """Return a 10-dimensional unit vector with a 1.0 in the jth
    position and zeroes elsewhere.  This is used to convert a digit
    (0...9) into a corresponding desired output from the neural
    network."""
    e = np.zeros((16, 1))
    e[j] = 1.0
    return e


def load_binary_numbers():
    training_inputs = []
    training_results = []


    for i in range(50000):
        number = randomNumber(0, 16)
        training_inputs.append(vectorized_result(number))
        training_results.append(nTo4bit(number))


    # training_results = np.array(training_results)
    # print(training_results.shape)
    # (100, 4, 1)

    # training_inputs = np.array(training_inputs)
    # print(training_inputs.shape)
    # (100, 16, 1)

    training_data = zip(training_inputs, training_results)
    # training_data = np.array(list(training_data))
    # print(training_data.shape)
    # (100, 2)


    test_inputs = []
    test_results = []

    for i in range(10000):
        number = randomNumber(0, 16)
        test_inputs.append(vectorized_result(number))
        test_results.append(number)

    # test_results = np.array(test_results)
    # print(test_results.shape)
    # (20, 4, 1)

    # test_inputs = np.array(test_inputs)
    # print(test_inputs.shape)
    # (20, 16, 1)


    test_data = zip(test_inputs, test_results)
    # test_data = np.array(list(test_data))
    # print(test_data.shape)
    # (20, 2)

    return (training_data, test_data)
