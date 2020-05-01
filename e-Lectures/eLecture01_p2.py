#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: rouabah
This program contains answer to Quaestion-1 of Exercise 1.1 of e_Lecture #1
"""

# Packages 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Laoding data (we will learn about this in next lectures)
It_Confirmed_Cases= np.loadtxt('Italy_ConfirmedCases_LastMonth.txt')
days = np.arange(It_Confirmed_Cases.size)+1

# Fit model
def model_1(x, p0,p1):          # linear model
    return p0 + p1*x

def model_2(x, p0,p1):          # exponential model
    return p0*np.exp(p1*x)


# Data Fitting
 
# Linear model
fit1_opt, fit1_cov = curve_fit(model_1, days, It_Confirmed_Cases)
# exponential model
fit2_opt, fit2_cov = curve_fit(model_2, days, It_Confirmed_Cases)
"""
the curve_fit() function that we use to fit data gives two outputs:
   * the first output (named "fit1_opt" for model_1 and fit2_opt for moedl_2)
   is a list that contains optimal values of the paramaters of the model
   that produce the best fit to data.
   (in our cases model_1 and model_2 have two parameters each
    so fit1_opt and fit2_opt will be lists with two elements)   
   * the second ooutput is a matrix related to errors in the estimation 
   of the parameters. We will explain it in the next lecture.
"""

# Unpack fitting paramaters
a,b = fit1_opt 
"""
 fit1_opt is list containing the optimal values for paramaters p0 and p1 
 obtained by fitting the data using model_1.
 "a" will take the value of p0 and "b" will take the value of p1
"""
c,d = fit2_opt
"""
 fit2_opt is list containing the optimal values for paramaters p0 and p1 
 obtained by fitting the data using model_2
 "c" will take the value of p0 and "d" will take the value of p1
"""

# Plot data and fitting curves:
plt.plot(days, It_Confirmed_Cases, 'ro') # plot data points 
plt.plot(days, a + b*days, 'b')  # plot fitting curve of model_1
plt.xlabel('Days')
plt.ylabel('Confirmed Cases')
plt.title('Data fitting with linear fit model')
plt.show()

plt.plot(days, It_Confirmed_Cases, 'ro') # plot data points 
plt.plot(days, c*np.exp(d*days), 'b')  # plot fitting curve of model_1
plt.xlabel('Days')
plt.ylabel('Confirmed Cases')
plt.title('Data fitting with exponential fit model')
plt.show()






