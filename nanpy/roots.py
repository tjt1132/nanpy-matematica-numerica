#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: ttorres
"""

from ..core import error
from ..core import result

def regula_falsi(x_lower, x_upper, function, acuracy):
    
    return_result = result.Result()  # Return result struct
    total_iterations = 0             # Total iterations of root solver
    root_history = []                # History of roots calculated per iteration
    root_error_history = []          # History of errors calculated per iteration
    
    if function(x_lower) * function(x_upper) < 0.:
        #First Iteration to calculate initial error
        y_upper = function(x_upper)
        y_lower = function(x_lower)
        x_middle = x_upper - (y_upper * (x_upper - x_lower) / (y_upper - y_lower))
        
        root_history.append(x_middle)
        
        y_middle = function(x_middle)
        if y_middle * y_lower < 0.:
            root_error = error.relative(x_middle, x_upper)
            root_error_history.append(root_error)
            x_upper = x_middle
        else:
            root_error = error.relative(x_middle, x_lower)
            root_error_history.append(root_error)
            x_lower = x_middle
        
        total_iterations = total_iterations + 1
        
        # Loop until the relative error between iteration is less than the wanted acuracy
        while root_error > acuracy:
            y_upper = function(x_upper)
            y_lower = function(x_lower)
            x_middle = x_upper - (y_upper * (x_upper - x_lower) / (y_upper - y_lower))
            
            root_history.append(x_middle)
            
            if y_middle * y_lower < 0.:
                root_error = error.relative(x_middle, x_upper)
                root_error_history.append(root_error)
                x_upper = x_middle
            else:
                root_error = error.relative(x_middle, x_lower)
                root_error_history.append(root_error)
                x_lower = x_middle
            
            total_iterations = total_iterations + 1
        
        return_result.is_valid = True
        return_result.value = x_middle
        return_result.acuracy = acuracy
        return_result.total_iterations = total_iterations
        return_result.history = root_history
        return_result.error_history = root_error_history
        
    else:
        return_result.is_valid = False
    
    return return_result
