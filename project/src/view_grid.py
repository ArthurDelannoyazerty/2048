from tkinter import Frame, Label, CENTER
import constants as c
from grid import Grid

class ViewGrid(Frame):
    
    def __init__(self, grid):
        self.cell_grid = grid
        Frame.__init__(self)
        
        self.grid()
        self.master.title('2048')
        
        self.init_grid(grid)
        self.master.mainloop()
    
    def init_grid(self, cell_grid):
        background = Frame(self, 
                           bg=c.BACKGROUND_COLOR_GAME)
        background.grid()
        
        
        for i in range(cell_grid.size):
            for j in range(cell_grid.size):
                cell = Frame(background,
                             bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                cell.grid(row=i,
                          column=j,
                          padx=c.GRID_PADDING,
                          pady=c.GRID_PADDING
                )
                t = Label( master=cell,
                           text="",
                           bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                           justify=CENTER,
                           font=c.FONT,
                           width=5,
                           height=3)
                t.grid()
        