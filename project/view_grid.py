from tkinter import Canvas
import constants as c
from grid import Grid

class ViewGrid(Canvas):
    
    def __init__(self, grid, window):
        self.cell_grid = grid
        width  = c.WIDTH_GRID_PX
        height = c.HEIGHT_GRID_PX
        Canvas.__init__(self, 
                        window,
                        width = width,
                        height = height,
                        bg=c.BACKGROUND_COLOR_GAME,
                        borderwidth=1,
                        highlightthickness=0)
        self.update_grid(grid)
        self.pack()
    
    def update_grid(self, cell_grid):
        self.create_rectangle(0, 0, c.WIDTH_GRID_PX, c.HEIGHT_GRID_PX, fill=c.BACKGROUND_COLOR_GAME)
        self.create_line(0,0,150,150)
        