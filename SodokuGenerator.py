'''Objective: Develop a program that can solve a given Sudoku puzzle using a backtracking algorithm. The goal of this task is to understand recursion, backtracking, and problem-solving techniques.

Question: You are required to write a Python program to solve a 9x9 Sudoku puzzle. The puzzle board is represented as a list of lists, where empty cells are denoted by 0. Your program should fill in the empty cells with numbers from 1 to 9 while adhering to the following Sudoku rules:

Each row must contain the numbers 1 to 9 without repetition.
Each column must contain the numbers 1 to 9 without repetition.
Each of the nine 3x3 sub-grids must contain the numbers 1 to 9 without repetition.'''

# Function to check if placing num at (row, col) is valid
def is_valid(board, row, col, num):
    # Check if the number is already in the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number is already in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is already in the 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# Function to solve the Sudoku using backtracking
def solve_sudoku(board):
    # Find the next empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try placing digits 1-9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        
                        # Recursively attempt to solve the puzzle
                        if solve_sudoku(board):
                            return True
                        
                        # Backtrack if placing num doesn't lead to a solution
                        board[row][col] = 0
                
                return False
    
    # If all cells are filled, the puzzle is solved
    return True

# Function to print the board
def print_board(board):
    for row in board:
        print(row)

# Example Sudoku puzzle
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Print the original Sudoku board
print("Original Sudoku Puzzle:")
print_board(sudoku_board)

# Solve the Sudoku puzzle
solve_sudoku(sudoku_board)

# Print the solved Sudoku board
print("\nSolved Sudoku Puzzle:")
print_board(sudoku_board)
