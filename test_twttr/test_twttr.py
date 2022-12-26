from twttr import shorten

#def test_shorten_default():
#    assert shorten() == ""

def test_shorten_blank():
    assert shorten("") == ""

def test_shorten():
    assert shorten("abc") == "bc"

def test_shorten_vowel():
    assert shorten("aeiou") == ""

def test_shorten_alphabets():
    assert shorten("abcdefghijklmnopqrstuvwxyz") == "bcdfghjklmnpqrstvwxyz"

def test_shorten_alphabets_caps():
    assert shorten("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "BCDFGHJKLMNPQRSTVWXYZ"

def test_shorten_numbers():
    assert shorten("1234567890") == "1234567890"

def test_shorten_special_chars():
    assert shorten("!@#$%^&*()_+?-<>|[]~`':;") == "!@#$%^&*()_+?-<>|[]~`':;"