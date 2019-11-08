#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: ttorres
"""

import numpy as np

def relative(xk0, xk1):
    return np.abs((xk0 - xk1) / xk0)

def absolute(xk1, xk0):
    return np.abs(xk0 - xk1)

def condition(A, norm='inf'):
    if norm == '1':
        return np.max(np.sum(A, axis=0)) * np.max(np.sum(np.linalg.inv(A), axis=0))
    elif norm == 'inf':
        return np.max(np.sum(A, axis=1)) * np.max(np.sum(np.linalg.inv(A), axis=1))
    
    
def errorVecR(v1, v0):
    return np.linalg.norm(v1 - v0, ord=np.inf) / np.linalg.norm(v1, ord=np.inf)

def errorVecA(v1, v0):
    return np.linalg.norm(v1 - v0, ord=np.inf)