import pytest
from sd.sd import standard_deviation

def test_standard_deviation():
    assert standard_deviation([1,2,3,4,5]) == 1.4142135623730951, 'pass normal case test, the answer should be 1.41'
    assert standard_deviation([1]) == 0.0, 'pass one-item case test, the answer should be 0.0'
    
