def hamming_encode(data: str) -> str:
    """
    data: string  of 1 and 0
    return: strinig with added checking bits
    """
    bits = [int(b) for b in data]

    # count r(quantity of checking bits)
    m = len(bits)
    r = 0
    while (2**r) < (m + r + 1):
        r += 1

    n = m + r  # len of word
    code = [0] * (n + 1)

    # add bits(ecept powers of 2)
    j = 0
    for i in range(1, n + 1):
        if i & (i - 1) != 0:
            code[i] = bits[j]
            j += 1

    # count checking bits
    for p in range(r):
        pos = 2**p
        parity = 0
        for i in range(1, n + 1):
            if i & pos:
                parity ^= code[
                    i
                ]  # it looks lowkey weird, I've never used XOR in python before
        code[pos] = parity

    return "".join(str(code[i]) for i in range(1, n + 1))


def hamming_decode(codeword: str) -> int:
    """
    codeword: string of 0 and 1
    return: if error - indeces of bit, else - "-1"
    """
    bits = [0] + [int(b) for b in codeword]
    n = len(codeword)

    # define r(count of cheking bits)
    r = 0
    while (2**r) <= n:
        r += 1

    syndrome = 0
    for p in range(r):
        pos = 2**p
        parity = 0
        for i in range(1, n + 1):
            if i & pos:
                parity ^= bits[i]
        if parity:
            syndrome += pos

    if syndrome == 0:
        return -1
    else:
        return syndrome


def main():
    data = input("Print string of 0 and 1: ")
    encoded = hamming_encode(data)
    print("The encoded string: ", encoded)

    received = input("Print this string:  ")
    err_pos = hamming_decode(received)

    if err_pos == -1:
        print("Right string. No error")
    else:
        print("Error position is: ", err_pos)


if __name__ == "__main__":
    main()
