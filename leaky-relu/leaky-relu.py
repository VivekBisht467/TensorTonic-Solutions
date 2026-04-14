import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    x = np.asarray(x)
    # result = [i if i>=0 else alpha*i for i in x]
    result = np.where(x>=0,x,alpha*x)
    return result