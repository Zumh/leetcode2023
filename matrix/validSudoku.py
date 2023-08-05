def isValidSudoku(board: list[list[str]]) -> bool:
    seen = set()

    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == ".":
                continue
            
            row_key = f"row_{i}_{val}"
            col_key = f"col_{j}_{val}"
            box_key = f"box_{i // 3}_{j // 3}_{val}"
            
            if row_key in seen or col_key in seen or box_key in seen:
                return False
            
            seen.add(row_key)
            seen.add(col_key)
            seen.add(box_key)
    return True
"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


HOW IT WORK?

Initialize an empty set seen to keep track of seen digits.

Iterate through each cell in the 9x9 Sudoku board using two nested loops with indices i and j representing the row and column indices, respectively.

Get the value val of the current cell.

If val is a period ('.'), indicating an empty cell, skip to the next iteration.

Generate unique keys for the current value val in the current row, column, and box using the indices i and j. These keys are used to check whether the same digit has been seen before in the same row, column, or box.

Check if any of the generated keys already exist in the seen set. If any of them exist, it means the same digit has been seen before in the same row, column, or box, violating the Sudoku rules. In this case, return False indicating the board is invalid.

If none of the keys exist in the seen set, add them to the set to mark the digits as seen.

After iterating through all cells without any violations, return True indicating that the Sudoku board is valid according to the rules.
"""
