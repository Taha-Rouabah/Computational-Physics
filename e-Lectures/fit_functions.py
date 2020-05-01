#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: rouabah

This file contains all the fitting models and function we are going to use
in the program eLecture02_p2.py contanining solutions for Ex 2.1 and Ex. 2.2
"""

import numpy as np

# model for linear fit
def linear(x, p0, p1):
	return p0 + p1*x
	
# model for exponential fit
def exponential(x, p0, p1):
	return p0 * np.exp(p1*x)

# model for power law fit
def power(x, p0, p1):
  return p0 * x**p1

# function for calculation of the coefficient of determination of a given fit
def R2(y_fit, y):
	y_mean = np.mean(y)
	SSres = sum([(y[i] - y_fit[i])**2 for i in range(y.size)])
	SStot = sum([(y[i] - y_mean)**2 for i in range(y.size)])
	return (1-(SSres/SStot))

# function for comparaison of two fits through their coefficient of determination
def fit_comparator(R2_fit1, R2_fit2):
    if R2_fit1 - R2_fit2 < 1e-6:
        print('\n ** The two fits are equivalent ** \n')
    elif 1-R2_fit1 < 1-R2_fit2:
        print("model_1 gives the best fit")
    elif 1-R2_fit1 > 1-R2_fit2:
        print("model_2 gives the best fit")

