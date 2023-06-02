import random

class SudokuSolver:
  def __init__(self, level) -> None:
    self.level = level
    self.grid = self.generate_sudoku()
    self.solve_sudoku(self.grid)
    self.remove_cells(self.grid, self.level)

  def generate_sudoku(self) -> list:
    """Generate a Sudoku puzzle with a unique solution"""
    grid = [[0] * 9 for _ in range(9)]

    for i in range(0, 9, 3):
      digits = [number for number in range(1, 10)]
      random.shuffle(digits)
      for j in range(3):
        for k in range(3):
          grid[i + j][i + k] = digits.pop()
    self.solve_sudoku(grid)

    return grid
  
  def solve_sudoku(self, grid: list[int]) -> bool:
    """Solve the given Sudoku puzzle, mutating the grid argument"""
    empty_cell = self.find_empty_cell(grid)
    if not empty_cell:
      return True

    row, col = empty_cell
    for num in range(1, 10):
      if self.is_valid(grid, row, col, num):
        grid[row][col] = num

        if self.solve_sudoku(grid):
          return True

        grid[row][col] = 0

    return False
  
  def is_valid(self, grid:int, row:int, col:int, num:int) -> bool:
    """Check if it's valid to place num at grid[row][col], return True/False"""
    if num in grid[row]:
      return False

    for i in range(9):
      if grid[i][col] == num:
        return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
      for j in range(start_col, start_col + 3):
        if grid[i][j] == num:
          return False
    return True
  
  def find_empty_cell(self, grid: list[int]) -> tuple[int, int] or None:
    """Find an empty cell in the grid, return (row, col) or None if not found"""
    for i in range(9):
      for j in range(9):
        if grid[i][j] == 0:
          return i, j
    return None
  
  def remove_cells(self, grid:list[int], count:int) -> None:
    """Remove count number of cells from the grid"""
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)

    for cell in cells:
      row, col = cell
      value = grid[row][col]
      grid[row][col] = 0

      num_solutions = 0
      temp_grid = [row[:] for row in grid]
      self.solve_sudoku(temp_grid)
      if self.has_unique_solution(temp_grid):
        num_solutions += 1

      if num_solutions != 1:
        grid[row][col] = value

      count -= 1
      if count == 0:
        break

  def has_unique_solution(self, grid: list[int]) -> bool:
    """Check if the given grid has a unique solution, return True/False"""
    empty_cell = self.find_empty_cell(grid)
    if not empty_cell:
      return True

    row, col = empty_cell
    for num in range(1, 10):
      if self.is_valid(grid, row, col, num):
        grid[row][col] = num

        if self.has_unique_solution(grid):
          return True

        grid[row][col] = 0

    return False

  def get_grid(self) -> list:
    """Return the grid"""
    return self.grid
  
  def get_level(self) -> int:
    """Return the level"""
    return self.level
  
  def set_level(self, level: int) -> None:
    """Set the level"""
    self.level = level
    self.remove_cells(self.grid, self.level)

  def get_solved_grid(self) -> list:
    """Return the solved grid"""
    solved_grid = [row[:] for row in self.grid]
    self.solve_sudoku(solved_grid)
    return solved_grid
  