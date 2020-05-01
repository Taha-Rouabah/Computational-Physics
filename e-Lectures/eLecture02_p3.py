#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: rouabah
This program contains solution of Exercises 2.2
"""


# Packages

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from fit_functions import *  # load all functions in "fit_functions.py"
"""
all the functions that we need for the exercise have been gethered in 
the file "fit_funtions.py" that is loaded by the above command
"""

# Data
x = np.array([1., 3., 5., 7.])
log_x = np.log(x)
x_bis = np.linspace(x[0], x[-1], 50)    # this will be used to generate smooth curves
log_x_bis = np.log(x_bis)               # this will be used to generate smooth curves
y = np.array([4.00000, 0.76980, 0.35777, 0.21598])
log_y = np.log(y)

#%% Questions 1 & 2:
    
# Exponential fit of data
fit1, fit1_cov = curve_fit(power, x, y)
y_fit1 = power(x, fit1[0], fit1[1])
y_fit1_bis = power(x_bis, fit1[0], fit1[1]) # this will give a smooth curve

# linear fit of ln(y) vs x data
fit2, fit2_cov = curve_fit(linear, log_x, log_y)
y_fit2 = linear(log_x, fit2[0], fit2[1])
y_fit2_bis = linear(log_x_bis, fit2[0], fit2[1])
"""
this above line is not really needed for the linear fit
 as the curve is a straight line that do not need to be smoothed
"""

# Plot data and fits
plt.plot(x,y, 'o')
plt.plot(x, y_fit1, 'g')
plt.plot(x_bis, y_fit1_bis, 'r-')   # smoothed curve
plt.xlabel('x')
plt.ylabel('y')
plt.title('y vs x (regular plot)')
plt.show()

# log-log plot
plt.plot(log_x,log_y,'o')
plt.plot(log_x, y_fit2, 'g')
plt.xlabel('log(x)')
plt.ylabel('log(y)')
plt.title('log(y) vs log(x) (log-log plot)')
plt.show()

#%% Question 3:
    
# Calculate coefficients of determination and Compare fits
R2_fit1 = R2(y_fit1, y)
print('\n The R2 given by the power law fit is {}'.format(R2_fit1))
R2_fit2 = R2(y_fit2, log_y)
print('\n The R2 given by the linear fit is {}'.format(R2_fit2))
fit_comparator(R2_fit1, R2_fit2)

"""
* The comprator function will show that the two fits are equivalents
* If you calculate the difference between the covariance matrix
the result will be of the order of 10^(-12) means that the covariance matrices
are the same.
"""








