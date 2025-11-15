from collections import Counter, deque


def encode(msg):
    if not msg:
        return "", {}

    freq = Counter(msg)
    chars = deque(sorted(freq.keys(), key=lambda x: freq[x]))

    if len(chars) == 1:
        return "0" * len(msg), {chars[0]: "0"}

    codes = {}
    while len(chars) > 1:
        a = chars.popleft()
        b = chars.popleft()

        for char in a:
            codes[char] = "0" + codes.get(char, "")
        for char in b:
            codes[char] = "1" + codes.get(char, "")

        new_char = a + b
        chars.append(new_char)
        chars = deque(sorted(chars, key=lambda x: freq[x]))

    encoded = "".join(codes[ch] for ch in msg)
    return encoded, codes
