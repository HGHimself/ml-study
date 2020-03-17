import math
import numpy as np
from matplotlib import pyplot as plt

def perceptron( weights, inputs, bias ):
    return 0 if np.sum( [w*x for w,x in zip(weights, inputs)] ) + bias <= 0 else 1

# regular exponential function, tiny with negative numbers, huge as z grows
# range = {0, inf}
def exp( z ):
    return math.exp( z )

# flipped exponential, huge with negative numbers, tiny as z grows
# range = {-inf, 0}
def neg_exp( z ):
    return exp( -z )

# this is equal to above
# to remove a negative exponent, x^-z = 1/x^z
# range = {-inf, 0}
def inverse_exp( z ):
    return 1 / exp( z )

# this just moves the entire graph up by 1
# makes sure the output is always > 0
# range = {1, inf}
def bumped_exp( z ):
    return 1 + exp( z )

# if z is big, denominator is big. makes fraction tiny(1/10000) aka close to 0
# if z is tiny, denominator is close to 1, makes fraction close to 1 / 1
# range = {1, 0}
def bumped_inverse_exp( z ):
    return 1 / ( 1 + exp( z ) )

# looking above, we have a function that goes from 1 to 0 as the input grows
# we want to flip so it goes from 0 to 1, so we use negative exponent
# range = {0, 1}
def sigmoid( z ):
    return 1 / ( 1 + math.exp( -z ))

top = 10
bottom = -10

functions = [exp, neg_exp, inverse_exp, bumped_exp, bumped_inverse_exp, sigmoid]
names = ['exp', 'neg_exp', 'inverse_exp', 'bumped_exp', 'bumped_inverse_exp', 'sigmoid']

for func, name in zip(functions, names):
    data = [ func(z) for z in range( bottom, top )]
    plt.plot(range( bottom, top ), data)
    plt.savefig(name+'.png')
    plt.clf()
