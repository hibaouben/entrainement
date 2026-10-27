from src.calc import addition
from src.calc import multiplication


def test_addition():
    assert addition(2, 3) == 5


def test_multiplication():
    assert multiplication(2, 3) == 6
