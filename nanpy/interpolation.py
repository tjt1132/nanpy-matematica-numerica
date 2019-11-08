#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:29:53 2019

@author: ttorres
"""
import numpy as np
from .lineareq import tomas
from .core import Spline

def spline_natural(xData, yData):
    n = len(xData)       # Number of Nodes
    intervals = n - 1    # Number of Intervals
    
    # Preallocate coeficient arrays
    aCoeficients = np.empty(n)
    bCoeficients = np.empty(intervals)
    dCoeficients = np.empty(intervals)
    
    # Preallocate h arrays
    h = np.empty(intervals)
    
    # Preallocate A and b matrix
    A = np.zeros((n, n))
    b = np.zeros(n)
    
    # Calculate length h of each interval
    for i in range(intervals):
        h[i] = xData[i + 1] - xData[i]

    # Calculate coeficients a
    for i in range(n):
        aCoeficients[i] = yData[i]
        
    # Fill matrix A
    A[0][0] = 1
    A[n - 1][n - 1] = 1
    for i in range(1, n - 1):
        A[i][i]     = 2. * (h[i - 1] + h[i])
        A[i][i + 1] = h[i]
        A[i][i - 1] = h[i - 1]
    
    # Fill vector b
    for i in range(1, n - 1):
        b[i] = (3. * (aCoeficients[i + 1] - aCoeficients[i]) / h[i]) - \
        (3. * (aCoeficients[i] - aCoeficients[i - 1]) / h[i - 1])
    
    cCoeficients = tomas(A, b)

    # Calculate cefficients d
    for i in range(intervals):
        dCoeficients[i] = (cCoeficients[i + 1] - cCoeficients[i]) / (3. * h[i])

    # Calculate cefficients b
    for i in range(intervals):
        bCoeficients[i] = ((aCoeficients[i + 1] - aCoeficients[i]) / h[i]) - \
        (h[i] * (cCoeficients[i + 1] + (2 * cCoeficients[i])) / 3)
    
    # Create Spline object
    spline_function = Spline(xData, (aCoeficients, bCoeficients, cCoeficients, dCoeficients))
    
    return spline_function

def spline_clamped(xData, yData, derivatives):
    n = len(xData)       # Number of Nodes
    intervals = n - 1    # Number of Intervals
    
    # Preallocate coeficient arrays
    aCoeficients = np.empty(n)
    bCoeficients = np.empty(intervals)
    dCoeficients = np.empty(intervals)
    
    # Preallocate h arrays
    h = np.empty(intervals)
    
    # Preallocate A and b matrix
    A = np.zeros((n, n))
    b = np.zeros(n)
    
    # Calculate length h of each interval
    for i in range(intervals):
        h[i] = xData[i + 1] - xData[i]

    # Calculate coeficients a
    for i in range(n):
        aCoeficients[i] = yData[i]
        
    # Fill matrix A
    A[0][0] = 2 * h[0]
    A[0][1] = h[0]
    A[n - 1][n - 2] = h[n - 2]
    A[n - 1][n - 1] = 2 * h[n - 2]
    for i in range(1, n - 1):
        A[i][i]     = 2. * (h[i - 1] + h[i])
        A[i][i + 1] = h[i]
        A[i][i - 1] = h[i - 1]
    
    # Fill vector b
    b[0] = (3. * (aCoeficients[1] - aCoeficients[0]) / h[0]) - 3 * derivatives[0]
    b[n - 1] = 3 * derivatives[1] - (3. * (aCoeficients[n - 1] - aCoeficients[n - 2]) / h[n - 2])
    for i in range(1, n - 1):
        b[i] = (3. * (aCoeficients[i + 1] - aCoeficients[i]) / h[i]) - \
        (3. * (aCoeficients[i] - aCoeficients[i - 1]) / h[i - 1])
    
    cCoeficients = tomas(A, b)

    # Calculate cefficients d
    for i in range(intervals):
        dCoeficients[i] = (cCoeficients[i + 1] - cCoeficients[i]) / (3. * h[i])

    # Calculate cefficients b
    for i in range(intervals):
        bCoeficients[i] = ((aCoeficients[i + 1] - aCoeficients[i]) / h[i]) - \
        (h[i] * (cCoeficients[i + 1] + (2 * cCoeficients[i])) / 3)
    
    # Create Spline object
    spline_function = Spline(xData, (aCoeficients, bCoeficients, cCoeficients, dCoeficients))
    
    return spline_function