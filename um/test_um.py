from um import count
from random import randint

def test_one():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("Hello Um...") == 1
    assert count("Um hello yum...") == 1

def test_zero():
    assert count("") == 0
    assert count("Cat") == 0
    assert count("   ") == 0
    assert count("Yummy") == 0
    assert count("umm...") == 0
    assert count("yum ") == 0

def test_multiple():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    x = randint(1, 10)
    string = "um yum hello um.. " * x
    assert count(string) == 2 * x
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
