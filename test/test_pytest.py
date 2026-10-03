from src.calculator import func1, func2, func3, func4

def test_fun1():
    assert func1(2, 3) == 5

def test_fun2():
    assert func2(10, 4) == 6

def test_fun3():
    assert func3(4, 3) == 12

def test_fun4():
    assert func4(2, 3) == 10