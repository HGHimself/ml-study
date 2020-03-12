import math

def sigmoid( weights, inputs, bias ):
    return 1 / (1 + math.exp(-1 * np.sum( [w*x for w,x in zip(weights, inputs)] ) + bias))
