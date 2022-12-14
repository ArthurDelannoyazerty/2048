import keyboard
import time
import constants as c
import numpy as np

class Actions():
    
    def __init__(self, grid):
        self.grid = grid
    
    def start_actions(self):
        while (True):
            key = keyboard.read_key()
            
            if key == c.KEY_UP :
                print("up")
            elif key == c.KEY_DOWN:
                print("down")
            elif key == c.KEY_RIGHT:
                print("right")
            elif key == c.KEY_LEFT:
                print("left")
            else :
                print("other key pressed : " + key)
            
            time.sleep(0.2)
    
    
    def action_up(self):
        matrix_size = self.grid.size
        for column_index in range(0, matrix_size):
            array = self.grid.get_column(column_index)
            array = self.action_array(array)
            self.grid.set_column(column_index, array)
            
            
    def action_down(self):
        matrix_size = self.grid.size
        for column_index in range(0, matrix_size):
            array = self.grid.get_column(column_index)
            array = array[::-1]
            array = self.action_array(array)
            array = array[::-1]
            self.grid.set_column(column_index, array)
    
    def action_left(self):
        matrix_size = self.grid.size
        for row_index in range(0, matrix_size):
            array = self.grid.get_row(row_index)
            array = self.action_array(array)
            self.grid.set_row(row_index, array)
            
    def action_right(self):
        matrix_size = self.grid.size
        for row_index in range(0, matrix_size):
            array = self.grid.get_row(row_index)
            array = array[::-1]
            array = self.action_array(array)
            array = array[::-1]
            self.grid.set_row(row_index, array)
            
    
    def action_array(self, array):
        
        number_zeros = 0
        for i in range(0, array.size):
            if array[i] == 0:
                number_zeros +=1
        
        if number_zeros == array.size:
            return array
        
        array_no_zero = np.zeros(array.size - number_zeros)
        index_free_space = 0
        for i in range(0, array.size):
            if array[i] != 0:
                array_no_zero[index_free_space] = array[i]
                index_free_space +=1
        
        index_free_space = 0
        new_array = np.zeros(array.size)
        flag_jump = False
        for i in range(0, array_no_zero.size-1):
            if flag_jump:
                flag_jump = False
                continue
            
            if array_no_zero[i] == array_no_zero[i+1]:
                new_array[index_free_space] = array_no_zero[i] * 2
                index_free_space +=1
                flag_jump = True
            
            if array_no_zero[i] != array_no_zero[i+1]:
                new_array[index_free_space] = array_no_zero[i]
                index_free_space +=1
        
        if not flag_jump:
            new_array[index_free_space] = array_no_zero[array_no_zero.size-1]
            
        return new_array