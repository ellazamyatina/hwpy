import pytest
import random


@pytest.fixture
def random_array() -> list:
    n = random.randint(1, 100)
    arr = []
    for _ in range(n):
        arr.append(random.randint(-10000, 10000))
    print("Given array: ", arr)
    return arr
