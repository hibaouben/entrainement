from src.calc import addition
import pytest
from src.calc import division

def test_addition():
    assert addition(2, 3) == 5

def test_division():
    assert division(10, 2) == 5
    assert division(9, 3) == 3

def test_division_par_zero():
    with pytest.raises(ValueError, match="Division par zéro impossible"):
        division(10, 0)