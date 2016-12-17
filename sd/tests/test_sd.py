import pytest
from sd.sd import standard_deviation

def test_standard_deviation():
assert standard_deviation([1,2,3,4,5]) == 1.4142135623730951, 'the standard deviation of 1,2,3,4,5 is equal to 1.414'
