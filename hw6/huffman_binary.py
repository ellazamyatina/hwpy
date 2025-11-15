# hw6/huffman_binary.py
import pickle
from .huffman_encode import encode
from .huffman_decode import decode


def encode_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    encoded, table = encode(text)  # Прямой вызов

    padding = 8 - len(encoded) % 8
    if padding != 8:
        encoded += "0" * padding

    bytes_data = bytearray()
    for i in range(0, len(encoded), 8):
        bytes_data.append(int(encoded[i : i + 8], 2))

    with open(output_path, "wb") as f:
        pickle.dump((padding, table, bytes_data), f)


def decode_file(input_path, output_path):
    with open(input_path, "rb") as f:
        padding, table, bytes_data = pickle.load(f)

    bits = "".join(f"{byte:08b}" for byte in bytes_data)
    if padding != 8:
        bits = bits[:-padding]

    decoded = decode(bits, table)  # Прямой вызов

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(decoded)
