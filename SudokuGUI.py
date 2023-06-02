from SudokuSolver import SudokuSolver
import tkinter as tk
from tkinter import messagebox

class SudokuGUI:
  def __init__(self, master, level) -> None:
    self.master = master
    self.level = level
    self.sudoku = SudokuSolver(self.level)
    self.grid = self.sudoku.get_grid()
    self.solved_grid = self.sudoku.get_solved_grid()
    self.cells = [[None] * 9 for _ in range(9)]
    self.create_widgets()
  
  def create_widgets(self)  -> None:
    """Create the widgets"""
    self.create_menu()
    self.create_grid()
    self.create_buttons()
  
  def create_menu(self) -> None:
    """Create the menu"""
    menu = tk.Menu(self.master)
    self.master.config(menu=menu)

    file_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='New Game', command=self.new_game)
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=self.master.destroy)

    level_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label='Level', menu=level_menu)
    level_menu.add_radiobutton(label='Easy', command=lambda: self.set_level(30))
    level_menu.add_radiobutton(label='Medium', command=lambda: self.set_level(40))
    level_menu.add_radiobutton(label='Hard', command=lambda: self.set_level(50))
  
  def create_grid(self) -> None:
    """Create the grid"""
    frame = tk.Frame(self.master)
    frame.pack()

    for i in range(9):
      for j in range(9):
        validate_cmd = self.master.register(self.validate_integer)
        cell = tk.Entry(frame, width=2, font=('Arial', 20, 'bold'), justify='center', validate="key", validatecommand=(validate_cmd, '%P'))
        cell.grid(row=i, column=j)
        if self.grid[i][j] != 0:
          cell.insert(0, self.grid[i][j])
          cell.config(state='disabled')
        self.cells[i][j] = cell

  def validate_integer(self, input_value: any) -> bool:
    if input_value.isdigit() or input_value == "":
      if len(input_value) > 1: return False
      return True
    else:
      return False

  def create_buttons(self) -> None:
    """Create the buttons"""
    frame = tk.Frame(self.master)
    frame.pack()

    tk.Button(frame, text='Check', command=self.check).pack(side='left')
    tk.Button(frame, text='Solve', command=self.solve).pack(side='left')
    tk.Button(frame, text='New Game', command=self.new_game).pack(side='left')
    tk.Button(frame, text='Show Answer', command=lambda: self.alert_answer()).pack(side='left')
    tk.Button(frame, text='Exit', command=self.master.destroy).pack(side='left')

  def check(self) -> None:
    """Check the solution"""
    for i in range(9):
      for j in range(9):
        cell = self.cells[i][j]
        if cell.get() == '':
          cell.config(bg='red')
          continue
        
        if int(cell.get()) != self.solved_grid[i][j]:
          cell.config(bg='red')
        else:
          cell.config(bg='green')

  def solve(self) -> None:
    """Solve the sudoku"""
    for i in range(9):
      for j in range(9):
        cell = self.cells[i][j]
        cell.config(state='normal')
        cell.delete(0, 'end')
        cell.insert(0, self.solved_grid[i][j])
        cell.config(state='disabled')

  def new_game(self) -> None:
    """Start a new game"""
    self.sudoku = SudokuSolver(self.level)
    self.grid = self.sudoku.get_grid()
    self.solved_grid = self.sudoku.get_solved_grid()

    for i in range(9):
      for j in range(9):
        cell = self.cells[i][j]
        cell.config(state='normal')
        cell.delete(0, 'end')
        cell.config(bg='white')
        if self.grid[i][j] != 0:
          cell.insert(0, self.grid[i][j])
          cell.config(state='disabled')

  def set_level(self, level:int) -> None:
    """Set the level"""
    self.level = level
    self.new_game()

  def alert_answer(self) -> None:
    answer = ''
    for row in self.solved_grid:
      for cell in row:
        answer += str(cell) + ' '
      answer += '\n'
    messagebox.showinfo('Correct answer', answer, parent=self.master, icon='info')
