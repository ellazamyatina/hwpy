def is_safe(board, row, col):  # check can we place queen in row №... column №...
    """Проверяет, можно ли поставить ферзя на позицию (row, col)"""

    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):  # check the diagonals
            return False
    return True


# implementation of recursive function
def solve_n_queens_recursive(n, row=0, board=None, count=None):
    if board is None:
        board = [-1] * n
    if count is None:
        count = [0]

    if row == n:
        count[0] += 1
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens_recursive(n, row + 1, board, count)
            board[row] = -1

    return count[0]


def n_queens_recursive(n):
    if n <= 0:
        return 0
    return solve_n_queens_recursive(n)


if __name__ == "__main__":  # test
    for n in range(1, 13):
        result = n_queens_recursive(n)
        print(f"N={n}: {result} решений")
