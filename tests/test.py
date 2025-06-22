from src.mathoperations import add,subt

def test_add():
    assert add(5, 3) == 8
    assert add(-5, 3) == -2
    assert add(-5, -3) == -8
    assert add(5, -3) == 2

def test_sub():
    assert subt(5, 3) == 2
    assert subt(-5, 3) == -8
    assert subt(-5, -3) == -2
    assert subt(5, -3) == 8