import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.asarray(x)
    exp_x = np.exp(2*x)
    return (exp_x-1)/(exp_x+1)