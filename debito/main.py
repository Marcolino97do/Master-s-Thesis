import numpy as np
import numpy.ma as ma
import random
import matplotlib
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

#DEFINE THE FIT FUNCTION
def exponential(x,a,b):
    return a*np.exp(x/b)




