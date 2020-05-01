#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: rouabah
This program is based on Exercise 1.1 of e_Lecture #1. It contains:
    - Anwser to Question 1
    - About Covariance Matrix (related to Sec. 2.1 of e-Lecture #2)
    - Anwser to Question 2: Determine the best fit  (related to Sec. 2.2 of e-Lecture #2)                         
"""

# Packages 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Laoding data (we will learn about this in next lectures)
It_Confirmed_Cases= np.loadtxt('Italy_ConfirmedCases_LastMonth.txt')
days = np.arange(It_Confirmed_Cases.size)+1

#%%  Anwser to Question 1: 
##########################
    
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



#%% About Covariance Matrix (related to Sec. 2.1 of e-Lecture #2)
###########################

"""
fit1_cov is the covaraince matrix of the paramaters estimate produced by model_1
The covariance matrix is d*d dimensional where d is the number of parameters 
in the model:
    The diagonal elements of the matrix represent the variance in the parameters.
    In our case the element (1,1) of the matrix represent the variance in p0.
    The element (2,2) of the covariance patrix represent tha variance of the
    parameter p1.
"""

# Calculate standard deviations
fit1_std = np.sqrt(np.diag(fit1_cov))
fit2_std = np.sqrt(np.diag(fit2_cov))
"""
produce a list with two elements: first element is the stabdard deviation in p0
and the second element std of p1
"""  


# Calculate the correlation coefficient
rho1 = fit1_cov[0][1]/(fit1_std[0]*fit1_std[1])
rho2 = fit1_cov[0][1]/(fit2_std[0]*fit2_std[1])


#%% Anwser to Question 2: Determine the best fit  (related to Sec. 2.2 of e-Lecture #2)
################################################

"""
Answer to question (2):
-----------------------  
It is clear from the figures that the linear model produce a better fit
 than the exponential one. But eye appreciation is not enough.
 In the following part we use two equivalent methods to determine
 which of the two fits is the best fit for our data (see Sec.2.2 of e-Lecture #2)
"""

y = It_Confirmed_Cases
f1 = model_1(days, a, b)
f2 = model_2(days, c, d) 

# residual sum of the square   
 
SSres1 = 0
SSres2 = 0
for i in range(y.size):
    SSres1 = SSres1 + (y[i] - f1[i])**2
    SSres2 = SSres2 + (y[i] - f2[i])**2
    
if SSres1 < SSres2:
    print("The linear function ""model_1"" gives the best fit")
elif SSres1 > SSres2:
    print("The exponential function ""model_2"" gives the best fit")
else:
    print("The two models give equivalent fits" )
    
"""
The residual sum of squares could be enough to determine the best fit
but a more conventional method is the calculation of the 
coefficient of determination (see Sec.2.2 of e-Lecture #2).
In the best case R2 = 1. 
"""

# total sum of the squares

SStot = 0
for i in range(y.size):
    SStot += (y[i] - np.mean(y))**2
    
# coefficient of determination

R2_fit1 = 1 -  SSres1/SStot
R2_fit2 = 1 -  SSres2/SStot
    
if 1-R2_fit1 < 1-R2_fit2:
    print("model_1 gives the best fit")
elif 1-R2_fit1 > 1-R2_fit2:
    print("model_2 gives the best fit")
else:
    print("The two models give equivalent fits" )


