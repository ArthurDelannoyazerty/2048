import numpy as np
import random

class Grid:
    
    def __init__(self, size):
        self.size = size
        self.matrix = np.zeros((size, size), dtype=int)
        self.add_random_cell()
    
    
    def get_column(self, n):
        if n<0 or n>self.size :
            return None
        
        column = np.zeros((self.size), dtype=int)
        for i in range(0, self.size):
            column[i] = self.matrix[i][n]
        
        return column
    
    def get_row(self, n):
        if n<0 or n>self.size :
            return None
        return self.matrix[n]
    
    def add_random_cell(self):
        chance_of_a_two = 0.7
        random_number_cell = random.random()
        cell_value = 2
        if random_number_cell > chance_of_a_two:
            cell_value = 4
        
        
        retry = True
        while (retry):
            random_x_index = random.randint(0, self.size-1)
            random_y_index = random.randint(0, self.size-1)

            if (self.matrix[random_x_index][random_y_index] == 0):
                self.matrix[random_x_index][random_y_index] = cell_value
                retry = False
        
        