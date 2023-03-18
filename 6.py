def n_queens(n):
    board = [[0 for x in range(n)] for y in range(n)]

    def is_safe(board, row, col):
        # Check the row on the left side
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check the upper diagonal on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check the lower diagonal on the left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve_n_queens(board, col):
        if col == n:
            # Base case: All queens have been placed
            return True

        for i in range(n):
            if is_safe(board, i, col):
                # Place the queen at this row and col
                board[i][col] = 1

                # Recur to place the remaining queens
                if solve_n_queens(board, col + 1):
                    return True

                # If placing queen in (i, col) doesn't lead to a solution
                # then backtrack and remove the queen from (i, col)
                board[i][col] = 0

        return False

    if solve_n_queens(board, 0) == False:
        print("Solution does not exist")
        return False

    # Print the board with queens placed
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print("\n")

n_queens(4)
