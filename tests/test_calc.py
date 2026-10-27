
import pytest
from src.calc import addition, multiplication, division


def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0


def test_multiplication():
    assert multiplication(3, 4) == 12
    assert multiplication(5, 0) == 0


def test_division():
    assert division(10, 2) == 5


def test_division_par_zero():
    with pytest.raises(ValueError):
        division(10, 0)
