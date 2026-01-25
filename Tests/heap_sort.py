from hw4.heap_sort import heap_sort
from conftest import random_array  # noqa: F401
import pytest


@pytest.mark.parametrize(
    ["input", "output"],
    [
        ([4, 3, 2, 0, -1, 2, 3], [-1, 0, 2, 3, 3, 4, 4]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        (
            [5, 4, 1, 13, 345, 1, 403, -14, -5, 1],
            [-14, -5, 1, 1, 1, 4, 5, 13, 345, 403],
        ),
    ],
)
def test_heap_sort_basic(input, output):
    assert heap_sort(input) == output


def test_one_element():
    assert heap_sort([1]) == [1]


def test_empty():
    assert heap_sort([]) == []


def test_negative():
    assert heap_sort([-10, -2, -3, -9, -5, -3, -4]) == [-10, -9, -5, -4, -3, -3, -2]


def test_randomly(random_array):  # noqa: F811
    assert heap_sort(random_array) == sorted(random_array)
