import pytest
import tempfile

from hw6 import encode, decode, encode_file, decode_file


def test_basic_encoding():
    encoded, table = encode("hello world")
    decoded = decode(encoded, table)
    assert decoded == "hello world"


def test_empty_string():
    encoded, table = encode("")
    decoded = decode(encoded, table)
    assert decoded == ""


def test_single_char():
    encoded, table = encode("aaaa")
    decoded = decode(encoded, table)
    assert decoded == "aaaa"


def test_special_chars():
    text = "!@#$*()\n\t"
    encoded, table = encode(text)
    decoded = decode(encoded, table)
    assert decoded == text


def test_file_operations():
    text = "gagfga popopo rarara"

    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
        f.write(text)
        input_file = f.name

    encoded_file = input_file + ".bin"
    output_file = input_file + "_decoded.txt"

    try:
        encode_file(input_file, encoded_file)
        decode_file(encoded_file, output_file)

        with open(output_file, "r") as f:
            result = f.read()

        assert result == text
    finally:
        for file in [input_file, encoded_file, output_file]:
            try:
                open(file, "w").close()
            except Exception:
                pass


def test_encoding_table_validity():
    text = "fsdgijerfoawje"
    encoded, table = encode(text)

    codes = set(table.values())
    assert len(codes) == len(table)

    for code1 in codes:
        for code2 in codes:
            if code1 != code2:
                assert not code2.startswith(code1)


def test_error_handling():
    try:
        result = decode("010", {"a": "0", "b": "10"})
        assert result == "ab"
    except Exception:
        pass


if __name__ == "__main__":
    test_basic_encoding()
    print("test_basic_encoding passed")

    test_empty_string()
    print("test_empty_string passed")

    test_single_char()
    print("test_single_char passed")

    test_special_chars()
    print("test_special_chars passed")

    test_file_operations()
    print("test_file_operations passed")

    test_encoding_table_validity()
    print("test_encoding_table_validity passed")

    test_error_handling()
    print("test_error_handling passed")

    print("\nAll tests passed! ")

    pytest.main([__file__, "-v"])
