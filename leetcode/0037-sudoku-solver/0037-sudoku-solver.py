class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
       
        col_used = collections.defaultdict(set)
        row_used = collections.defaultdict(set)
        box_used = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    value = board[row][col]
                    col_used[col].add(value)
                    row_used[row].add(value)
                    box_used[(row // 3, col // 3)].add(value)

        def backtrack(row, col):
            if row == 9:
                return True

            if col == 9:
                return backtrack(row + 1, 0)
            if board[row][col] != ".":
                return backtrack(row, col + 1)
            for num in range(1, 10):
                value = str(num)

                if (value in col_used[col] or
                    value in row_used[row] or
                    value in box_used[(row // 3, col // 3)]):
                    continue
                board[row][col] = value
                col_used[col].add(value)
                row_used[row].add(value)
                box_used[(row // 3, col // 3)].add(value)

                if backtrack(row, col + 1):
                    return True
                board[row][col] = "."
                col_used[col].remove(value)
                row_used[row].remove(value)
                box_used[(row // 3, col // 3)].remove(value)

            return False

        backtrack(0, 0)