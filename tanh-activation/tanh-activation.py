import numpy as np
import math


def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.asarray(x)
    exp_x = np.where(x>0,np.exp(-2*x),np.exp(2*x))
    return np.where(x>0,(1-exp_x)/(1+exp_x),(exp_x-1)/(exp_x+1))