from grid import Grid
from view_grid import ViewGrid
from main_window import Main_Window




window = Main_Window().window
grid = Grid()
view_grid = ViewGrid(grid, window)

view_grid.create_line(0,100,100,0)

window.mainloop()
