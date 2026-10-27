from src.calc import addition
<<<<<<< HEAD
import pytest
from src.calc import division
=======
from src.calc import multiplication

>>>>>>> origin/develop

def test_addition():
    assert addition(2, 3) == 5

<<<<<<< HEAD
def test_division():
    assert division(10, 2) == 5
    assert division(9, 3) == 3

def test_division_par_zero():
    with pytest.raises(ValueError, match="Division par zéro impossible"):
        division(10, 0)
=======

def test_multiplication():
    assert multiplication(2, 3) == 6
>>>>>>> origin/develop
