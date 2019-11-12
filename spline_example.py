#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 06:48:22 2019

@author: ttorres
"""
import numpy as np
import matplotlib.pyplot as plt
from nanpy import interpolation

##############################################################################
# True Function
##############################################################################

true_function   = lambda x: np.exp(x) - np.power(x, 3)
true_function_d = lambda x: np.exp(x) - 3 * np.power(x, 2)

##############################################################################
# Interpolation Nodes
##############################################################################

x0 = -1.
x1 = -0.5
x2 =  0.
x3 =  0.5
y0 =  1.3679
y1 =  0.7315
y2 =  1.0000
y3 =  1.5237

xData = np.array([x0, x1, x2, x3])
yData = np.array([y0, y1, y2, y3])


##############################################################################
# Natural Spline Function
##############################################################################

x = np.linspace(min(xData), max(xData), 90)
spline_func_natural = interpolation.spline_natural(xData, yData)

y_true = true_function(x)
y_spline = spline_func_natural(x)

plt.figure()
plt.plot(xData, yData,    'ro')
plt.plot(x,     y_true,   'b-', label="True")
plt.plot(x,     y_spline, 'm-', label="Spline")
plt.title("Natural Spline")
plt.legend()

##############################################################################
# Clamped Spline Function
##############################################################################

fda = true_function_d(xData[0])
fdb = true_function_d(xData[3])

x = np.linspace(min(xData), max(xData), 90)
spline_func_clamped = interpolation.spline_clamped(xData, yData, [fda, fdb])

y_true = true_function(x)
y_spline = spline_func_clamped(x)

plt.figure()
plt.plot(xData, yData,    'ro')
plt.plot(x,     y_true,   'b-', label="True")
plt.plot(x,     y_spline, 'm-', label="Spline")
plt.title("Clamped Spline")
plt.legend()
plt.show()