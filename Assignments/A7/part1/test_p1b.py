# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 11:19:01 2018

@author: pcc
"""

import p1b
def test_month_length():
    assert p1b.month_length("January") == 31
    assert p1b.month_length("February") == 28
    assert p1b.month_length("February",leap_year=True) == 29
    assert p1b.month_length("July") == 31
    assert p1b.month_length("August") == 31
    assert p1b.month_length("September") == 30
    assert p1b.month_length("October") == 31
    assert p1b.month_length("else") == None