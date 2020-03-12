import numpy as np
from random import random, seed
import math
import sys

def intTryParse( value ):
    try:
        return int( value ), True
    except ValueError:
        return value, False

def printErrorTerminate( error ):
    print( error )
    sys.exit(1)

def randomNumber(bottom, spread):
    return bottom + (math.floor(random() * spread * 10)) % spread

def randomBool():
    return randomNumber(0, 2)

# takes ordered inputs and their respective weights
# sum of input timews its given weight
# 1 if weight is greater than threshhold, otherwise 0
#
# @params weights :: Array[int]
# @params inputs :: Array[bool as int]
# @params bias :: int
# @return bool as int
def perceptron( weights, inputs, bias ):
    return 0 if np.sum( [w*x for w,x in zip(weights, inputs)] ) + bias <= 0 else 1

def main():
    input_file = './perceptron.data.txt'

    with open( input_file ) as file:

        bias_from_file = file.readline()
        bias, res = intTryParse( bias_from_file )
        if not res:
            printErrorTerminate( "Error: The first line in the input file must be the bias" )


        num_weights_from_file = file.readline()
        num_weights, res = intTryParse( num_weights_from_file )
        if not res:
            printErrorTerminate( "Error: The second line in the weights input file must be the number of weights" )

        weights_from_file = []
        for line in file.readlines():
            x, res = intTryParse(line)
            if res:
                weights_from_file.append(x)

        weights = np.array(weights_from_file).astype(np.int)

        inputs = np.array([ randomBool() for _ in enumerate(weights) ]).astype(np.int)
        result = perceptron(weights, inputs, bias)

        print("Bias ::", bias)
        print("Weights ::", weights)
        print("Inputs ::", inputs)
        print("Result ::", result)


main()
