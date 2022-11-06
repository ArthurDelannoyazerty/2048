from grid import Grid
from view_grid import ViewGrid
from main_window import Main_Window
import threading
from actions import Actions


def thread_data(view_grid, grid):
    i=0

def thread_keyboard(view_grid, grid):
    action = Actions(grid)
    

window = Main_Window().window
grid = Grid()
view_grid = ViewGrid(grid, window)

thread_data_manager = threading.Thread(target=thread_data, args=(view_grid, grid))
thread_data_manager.start()

thread_keyboard_manager = threading.Thread(target=thread_keyboard, args=(view_grid, grid))
thread_keyboard_manager.start()

view_grid.create_line(0,100,100,0)

window.mainloop()
