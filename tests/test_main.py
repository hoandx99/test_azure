import pytest
from src import main

class Test:
    def test_sum(self):
        assert main.sum(4, 5) == 9

    def test_sum_float(self):
        assert not main.sum(2.4, 3.6) == 1.0

    def test_minus(self):
        assert main.minus(6, 2) == 4

    def test_multiplication(self):
        assert main.multiplication(4, 3) == 12

    def test_multiplication_zero(self):
        assert main.multiplication(4, 0) == 0

    def test_division_zero(self):
        with pytest.raises(ZeroDivisionError) as excinfo:  
            main.division(1, 0)  
        assert str(excinfo.value) == "division by zero" 
