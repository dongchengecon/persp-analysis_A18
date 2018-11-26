# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 23:00:44 2018

@author: pcc
"""
import p1a

def test_smallest_factor1():
    assert p1a.smallest_factor(9) == 3, "failed on full square"
    
def test_smallest_factor2():    
    assert p1a.smallest_factor(6) == 2, "failed on small numbers"