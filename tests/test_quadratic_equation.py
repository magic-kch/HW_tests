import pytest
from first_task.quadratic_equation_solution import quadratic_equation_solution, find_discriminant


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, 8, 15, (-3.0, -5.0)),
        (1, -13, 12, (12.0, 1.0)),
        (-4, 28, -49, (3.5)),
        (1, 1, 1, 'корней нет'),
    ],
)
def test_quadratic_equation_solution(a, b, c, expected):
    assert quadratic_equation_solution(a, b, c) == expected


def test_find_discriminant_less_zero():
    assert find_discriminant(1, 1, 1) < 0


def test_find_discriminant_equal_zero():
    assert find_discriminant(-4, 28, -49) == 0


def test_find_discriminant_more_zero():
    assert find_discriminant(1, -13, 12) > 0
