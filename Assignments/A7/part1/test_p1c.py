# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 13:32:42 2018

@author: pcc
"""

import p1c
import pytest

def test_cases():
    assert p1c.operate(1,2,"+") == 3
    assert p1c.operate(1,2,"-") == -1
    assert p1c.operate(1,2,"*") == 2
    assert p1c.operate(1,2,"/") == 0.5
    with pytest.raises(ZeroDivisionError) as err:
        p1c.operate(1,0,'/')
    assert err.value.args[0]=="division by zero is undefined"

    with pytest.raises(TypeError) as err2:
        p1c.operate(1,0,0)
    assert err2.value.args[0]=="oper must be a string"

    with pytest.raises(ValueError) as err3:
        p1c.operate(1,0,'<')
    assert err3.value.args[0]=="oper must be one of '+', '/', '-', or '*'"