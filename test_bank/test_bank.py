from bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0

def test_value_hey():
    assert value("hey") == 20
    assert value("Hey") == 20
    assert value("HEY") == 20

def test_value_various():
    assert value("Hello David") == 0
    assert value("Whats' up?") == 100
    assert value("Hey David") == 20
    assert value("New day") == 100
    assert value("Good Morning") == 100