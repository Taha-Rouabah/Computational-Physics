#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: rouabah

e-Lecture #1: Data Fitting (1)
Program 1: This program fit the data of Example 1.1 with a linear model
"""

# Packages 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Data
time = [1 , 2 , 3 , 4 , 5 , 6 , 7]      # Time (days)
R = [4.399, 4.212 , 4.123 , 3.809 ,3.652 ,3.206 ,3.033] # Reproduction number

# Plot of Data
plt.plot(time, R, 'b--')
plt.plot(time, R, 'ro', label='Data')
plt.grid(True)
plt.xlabel('Time (days)')
plt.ylabel('Roproduction Number')
plt.legend(loc=0)
plt.show()

# Fit model
def model_1(x, p0,p1):
    return p0 + p1*x

# Fitting
fit1_opt, fit1_cov = curve_fit(model_1, time, R)

# Unpack fitting parameters
b,a = fit1_opt

# Plot fitting curve
plt.plot(time, [(b+ a*t) for t in time], 'b', label='LS Fit')
plt.plot(time, R, 'ro',  label='Data')
plt.grid(True)
plt.xlabel('Time (days)')
plt.ylabel('Roproduction Number')
plt.legend(loc=0)
plt.title('Least Squares Fit')
plt.show()


