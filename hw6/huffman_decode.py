def decode(encoded, table):
    if not encoded:
        return ""

    rev_table = {v: k for k, v in table.items()}

    result = []
    current = ""
    for bit in encoded:
        current += bit
        if current in rev_table:
            result.append(rev_table[current])
            current = ""
    return "".join(result)
