import pytest
from rewriting_test.walkers_method import Walker


def test_single_event():
    w = Walker([("A", 1.0)])
    for i in range(100):
        assert w.get_random() == "A"


def test_invalid_empty_list():
    with pytest.raises(ValueError):
        Walker([])


def test_negative_probability_raises():
    with pytest.raises(ValueError):
        Walker([("A", 0.5), ("B", -0.1), ("C", 0.6)])


def test_sum_not_one_raises():
    with pytest.raises(ValueError):
        Walker([("A", 0.2), ("B", 0.2)])
