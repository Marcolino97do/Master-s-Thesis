from scipy.optimize import curve_fit
from matplotlib import pyplot as plt


import numpy as np
# Function to calculate the exponential with constants a and b
def exponential(x, a, b):
    return a*np.exp(b*x)

# Generate dummy dataset
x_dummy = np.linspace(start=5, stop=15, num=50)

# Calculate y-values based on dummy x-values
y_dummy = exponential(x_dummy, 0.5, 0.5)

# Add noise from a Gaussian distribution
noise = 5*np.random.normal(size=y_dummy.size)
y_dummy = y_dummy + noise

# Plot the noisy exponential data
plt.plot(x_dummy,y_dummy, label='guardame')
plt.xlabel('x')
plt.ylabel('y')
plt.title('exponential a caso')
plt.legend()
plt.show()