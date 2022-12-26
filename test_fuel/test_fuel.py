import pytest
from fuel import convert, gauge
import random

def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("0/100") == 0
    assert convert("1/100") == 1
    assert convert("100/100") == 100
    assert convert("1/1") == 100

def test_convert_exceptions():
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("12/3.4")
    with pytest.raises(ValueError):
        convert("4.2/3.4")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_guage():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    i = random.randint(2,98)
    assert gauge(i) == f"{i}%"
