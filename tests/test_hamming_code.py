import pytest
from rewriting_test.hamming_code import hamming_encode, hamming_decode


def test_encode_no_error():
    data = "1010"
    encoded = hamming_encode(data)
    assert hamming_decode(encoded) == -1
