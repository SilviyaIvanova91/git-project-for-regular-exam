from sample_calculator import sum, substract


def test_sum():
    assert sum(1, 2) == 3
    assert sum(-1, -1) == -2
    assert sum(0, 0) == 0


def test_substract():
    assert substract(5, 3) == 2
    assert substract(-1, -1) == 0
    assert substract(0, 5) == -5


