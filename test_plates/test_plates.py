from plates import is_valid

def test_is_valid_too_short():
    assert is_valid("") == False
    assert is_valid("A") == False
    assert is_valid("1") == False

def test_is_valid_too_large():
    assert is_valid("ABCDEFG") == False
    assert is_valid("ABC1234") == False
    assert is_valid("ABCD123") == False
    assert is_valid("1234567") == False

def test_is_valid_six():
    assert is_valid("ABC123") == True

def test_is_valid_first_zero():
    assert is_valid("AB01") == False
    assert is_valid("ABC012") == False

def test_is_valid_numbers():
    assert is_valid("1") == False
    assert is_valid("12") == False
    assert is_valid("123") == False
    assert is_valid("1234") == False
    assert is_valid("12345") == False
    assert is_valid("12345") == False
    assert is_valid("1234567") == False

def test_is_valid_only_char():
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("PI") == True
    assert is_valid("ABC") == True
    assert is_valid("ABCD") == True
    assert is_valid("ABCDE") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFG") == False

def test_is_valid_more():
    assert is_valid("AB12") == True
    assert is_valid("PI314") == True

def test_is_valid_special_char():
    assert is_valid("PI3.14") == False
    assert is_valid("_AB") == False

def test_is_valid_number_palcement():
    assert is_valid("AB12AB") == False
    assert is_valid("12AB") == False
    assert is_valid("AB123") == True
