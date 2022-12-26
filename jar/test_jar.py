from jar import Jar
import pytest

def test_init():
    jar = Jar(0)
    assert jar.capacity == 0
    assert jar.size == 0

    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(100)
    assert jar.capacity == 100
    assert jar.size == 0

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.capacity == 12
    assert jar.size == 1

    with pytest.raises(ValueError):
        jar.deposit(12)

    with pytest.raises(ValueError):
        jar.deposit(100)

    jar.deposit(2)
    assert jar.size == 3

def test_withdraw():
    jar = Jar()
    jar.deposit(1)
    assert jar.capacity == 12
    assert jar.size == 1
    jar.withdraw(1)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(12)

    with pytest.raises(ValueError):
        jar.withdraw(100)

    jar.deposit(2)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(3)

    with pytest.raises(ValueError):
        jar.withdraw(12)

def test_string():
    jar = Jar()
    jar.deposit(1)
    assert jar.__str__() == "🍪"
    assert jar.size == 1

    jar.deposit(5)
    assert jar.__str__() == "🍪🍪🍪🍪🍪🍪"
    assert jar.size == 6

    jar.withdraw(6)
    assert jar.__str__() == ""
    assert jar.size == 0