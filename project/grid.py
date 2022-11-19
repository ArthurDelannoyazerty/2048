import numpy as np
import random

class Grid:
    
    def __init__(self, size):
        self.size = size
        self.matrix = np.zeros((size, size), dtype=int)
    
    
    def get_column(self, n):
        if n<0 or n>self.size :
            return None
        
        column = np.zeros((self.size), dtype=int)
        for i in range(0, self.size):
            column[i] = self.matrix[i][n]
        
        return column

    def set_column(self, index_column, array):
        if index_column >= self.size or index_column < 0:
            raise IndexError("Column index out of bounds.")
        if array.size != self.size:
            raise IndexError("Array has a bad format.")
        
        
        for i in range(0, self.size):
            self.matrix[i][index_column] = array[i]
            
    
    def get_row(self, index_row):
        if index_row<0 or index_row>self.size :
            return None
        return self.matrix[index_row]
    
    
    def set_row(self, index_row, array):
        if index_row >= self.size or index_row < 0:
            raise IndexError("Column index out of bounds.")
        if array.size != self.size:
            raise IndexError("Array has a bad format.")
        self.matrix[index_row] = array
    
    
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
        
        