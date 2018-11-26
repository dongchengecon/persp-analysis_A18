# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 22:58:45 2018

@author: pcc
"""

# original function 

def smallest_factor(n):
    """Return the smallest prime factor of the positive integer n."""
    if n == 1: return 1
    for i in range(2, int(n**.5)+1):
        if n % i == 0: return i
    return n