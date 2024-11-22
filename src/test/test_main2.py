import pytest
from src.main2 import sum, sub, div

def test_sum():
    assert sum(1, 2) == 3

def test_sub():
    assert sub(5, 3) == 2
    assert sub(10, 20) == -10
    assert sub(0, 0) == 0

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (15, 3, 5),
    (8, 4, 2),
    (100, 10, 10),
    (7, 2, 3.5),
    (1, 3, 1/3),
    (0, 5, 0),
])
def test_div(a, b, expected):
    assert div(a, b) == pytest.approx(expected)
