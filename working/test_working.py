from working import convert
import pytest

def test_valid():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_more():
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12:01 AM to 11:59 PM") == "00:01 to 23:59"
    assert convert ("12 AM to 11 PM") == "00:00 to 23:00"

def test_invalid():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("12:60 AM to 11:60 PM")
    with pytest.raises(ValueError):
        convert("12 AM - 11 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9am to 5pm")
    with pytest.raises(ValueError):
        convert("AM to PM")