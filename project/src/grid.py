import numpy as np
from cell import Cell

class Grid:
    
    def __init__(self, size = 4):
        self.size = size
        self.new_grid(size)
        
    
    def new_grid(self, size):
        self.matrix = np.empty((size, size), Cell)