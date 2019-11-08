#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:45:12 2019

@author: ttorres
"""
import numpy as np

class Result(object):
    """
    Result structure for nanpy algorithms
    """
    def __init__(self):
        self.is_valid = False
        self.value = 0.
        self.acuracy = 0
        self.total_iterations = 0
        self.history = []
        self.error_history = []
        
class Spline(object):
    
    def __init__(self, nodes, coeficients):
        self.nodes = nodes
        self.a = coeficients[0]
        self.b = coeficients[1]
        self.c = coeficients[2]
        self.d = coeficients[3]
        
        self.total_intervals = len(nodes) - 1
        
    def __call__(self, xData):
        y_parts = []
        for i in range(self.total_intervals):
            x_indeces = np.where(np.logical_and(xData >= self.nodes[i], xData <= self.nodes[i + 1]))
            y_part = self.a[i] + \
            (self.b[i] * (xData[x_indeces] - self.nodes[i])) + \
            (self.c[i] * np.power((xData[x_indeces] - self.nodes[i]), 2)) + \
            (self.d[i] * np.power((xData[x_indeces] - self.nodes[i]), 3))
            
            y_parts.append(y_part)
        
        yData  = np.concatenate(y_parts)

        return yData