import pytest

def test_multiple_asserts():
    value1 = 10
    value2 = 15
    
    assert value1 < value2
    assert value2 > 0
    assert value1 + value2 == 30