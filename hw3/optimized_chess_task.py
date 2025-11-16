def n_queens_optimized(n):  # solve the problem using sets
    def solve(row, cols, diag1, diag2):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if col in cols or row - col in diag1 or row + col in diag2:
                continue
            # call recursive function
            count += solve(
                row + 1, cols | {col}, diag1 | {row - col}, diag2 | {row + col}
            )
        return count

    return solve(0, set(), set(), set()) if n > 0 else 0


# test
if __name__ == "__main__":
    for n in range(1, 13):
        print(f"N={n}: {n_queens_optimized(n)} решений")
