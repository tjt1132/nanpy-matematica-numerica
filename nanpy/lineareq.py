#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:34:08 2019

@author: ttorres
"""
import numpy as np

def tomas(A, b):
    n = len(b)
    
    # Preallocate beta and gamma
    beta  = np.empty(n)
    gamma = np.empty(n)
    
    # Preallocate x
    x = np.empty(n)
    
    # Calculata all beta and gamma
    for i in range(n):
        if i == 0:
            beta[i]  = A[i][i]
            gamma[i] = b[i] / beta[i]
        else:
            beta[i]  = A[i][i] - (A[i][i - 1] * A[i - 1][i] / beta[i -1])
            gamma[i] = (b[i] - (A[i][i - 1] * gamma[i - 1])) / beta[i]
    
    for i in reversed(range(n)):
        if i == n - 1:
            x[i] = gamma[i]
        else:
            x[i] = gamma[i] - (A[i][i + 1] * x[i + 1] / beta[i])
    
    return x