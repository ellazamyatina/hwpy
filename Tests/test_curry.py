import pytest

from hw5.curry import curry, uncurry


def sum3(a, b, c):
    return a + b + c


def make_list(a, b, c):
    return [a, b, c]


def test_currying():
    curried_sum3 = curry(sum3, 3)
    assert curried_sum3(1)(2)(3) == 6

    curried_list = curry(make_list, 3)
    assert curried_list(1)(2)(3) == [1, 2, 3]

    curried_wrong = curry(make_list, 4)
    with pytest.raises(Exception):
        curried_wrong(1)(2)(3)(4)

    with pytest.raises(Exception):
        uncurried_wrong = uncurry(curried_wrong, 5)
        uncurried_wrong(1, 2, 3, 4, 5)


def test_uncurry():
    curried_sum3 = curry(sum3, 3)
    curried_list = curry(make_list, 3)
    uncurried_sum3 = uncurry(curried_sum3, 3)
    uncurried_list = uncurry(curried_list, 3)

    assert uncurried_sum3(1, 2, 3) == 6
    assert uncurried_list(1, 2, 3) == [1, 2, 3]


def test_negative_arity():
    with pytest.raises(Exception):
        curry(sum3, -3)
    with pytest.raises(Exception):
        uncurry(sum3, -3)
