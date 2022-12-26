from numb3rs import validate
from random import randint

def test_valid_inputs():
    assert validate(r"0.0.0.0") == True
    assert validate(r"1.1.1.1") == True
    assert validate(r"255.255.255.255") == True
    assert validate(r"255.255.255.0") == True
    assert validate(r"255.255.0.255") == True
    assert validate(r"255.0.255.255") == True
    assert validate(r"255.0.0.255") == True
    assert validate(f"{randint(0,255)}.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}") == True

def test_invalid_inputs():
    assert validate(r"cat") == False
    assert validate(r"-1.1.1.1") == False
    assert validate(r"0.1.1.-1") == False
    assert validate(r"1:1:1:1") == False
    assert validate(r"256.256.256.256") == False
    assert validate(r"255.256.256.256") == False
    assert validate(r"256.255.256.256") == False
    assert validate(r"256.256.255.256") == False
    assert validate(r"256.256.256.255") == False
    assert validate(f"256.{(randint(0,255))}.{randint(0,255)}.{randint(0,255)}") == False
    assert validate(f"{randint(0,255)}.256.{randint(0,255)}.{randint(0,255)}") == False
    assert validate(f"{randint(0,255)}.{randint(0,255)}.256.{randint(0,255)}") == False
    assert validate(f"{randint(0,255)}.{randint(0,255)}.{randint(0,255)}.256") == False
    assert validate(f"{randint(256,10000000)}.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}") == False
    assert validate(f"{randint(0,255)}.0{randint(0,255)}.{randint(0,255)}.{randint(0,255)}") == False

def test_format():
    #assert validate(r"1.1.01.1") == False
    assert validate(r"1.1.01.") == False
    assert validate(r"1.1.011") == False
    assert validate(r"1.1") == False
