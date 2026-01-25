import itertools


def is_valid_brute_force(board):  # proves that queens placement is correct
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i][0] == board[j][0]:
                return False
            if abs(board[i][0] - board[j][0]) == abs(board[i][1] - board[j][1]):
                return False
    return True


def n_queens_brute_force(n):  # enumeration of all possible queen arrangements
    if n <= 0 or n > 10:
        return 0

    count = 0

    for permutation in itertools.permutations(
        range(n)
    ):  # generate all possible arrangements(in each column)
        board = [(i, permutation[i]) for i in range(n)]  # make table(columns and rows)
        if is_valid_brute_force(board):
            count += 1

    return count


if __name__ == "__main__":  # test
    for n in range(1, 9):
        result = n_queens_brute_force(n)
        print(f"N={n}: {result} решений")
