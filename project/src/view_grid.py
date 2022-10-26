from tkinter import Frame
import constants as c
from grid import Grid

class ViewGrid(Frame):
    
    def __init__(self, grid):
        self.grid = grid
        Frame.__init__(self)
        
        self.grid()
        self.master.title('2048')
    
    def init_grid(self):
        background = Frame(self, 
                           bg=c.BACKGROUND_COLOR_GAME,
                           width  = self.grid.size, 
                           height = self.grid.size)
        background.grid()