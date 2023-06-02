###############################################
# Sudoku by xcvrys
# Discord: xcvrys#3939 
# LinkedIn: https://www.linkedin.com/in/xcvrys/
#
# This program uses backtracking algorithm to generate a valid Sudoku puzzle.
# Then it removes some cells from the grid to make it solvable.
# 
# Usage: 
#   python main.py
###############################################

import tkinter as tk
from SudokuGUI import SudokuGUI

if __name__ == '__main__':
  root = tk.Tk()
  root.title('Sudoku by xcvrys')
  root.resizable(False, False)
  SudokuGUI(root, 30)
  root.mainloop()
