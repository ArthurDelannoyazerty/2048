from actions import Actions
from grid import Grid
import numpy as np
import unittest

class TestGrid(unittest.TestCase):

    def test_get_column_grid_empty(self): 
        """Test that aa empty grid is still empty after an action"""
        grid = Grid() 
        
        grid.matrix = np.array([[0, 0, 0, 0], 
                                [0, 0, 0, 0],
                                [0, 0, 0, 0], 
                                [0, 0, 0, 0]])
        
        true_array = np.array([0, 0, 0, 0])
        generated_array1 = grid.get_column(0)
        generated_array2 = grid.get_column(1)
        generated_array3 = grid.get_column(2)
        generated_array4 = grid.get_column(3)
        
        test1 = np.allclose(generated_array1, true_array)
        test2 = np.allclose(generated_array2, true_array)
        test3 = np.allclose(generated_array3, true_array)
        test4 = np.allclose(generated_array4, true_array)
        
        self.assertTrue(test1 and test2 and test3 and test4)

    def test_get_column_grid_custom(self): 
        """Test that aa empty grid is still empty after an action"""
        grid = Grid() 
        
        grid.matrix = np.array([[1, 2, 3, 4], 
                                [4, 3, 2, 1],
                                [5, 6, 7, 8], 
                                [8, 7, 6, 5]])
        
        true_column1 = np.array([1, 4, 5, 8])
        true_column2 = np.array([2, 3, 6, 7])
        true_column3 = np.array([3, 2, 7, 6])
        true_column4 = np.array([4, 1, 8, 5])
        
        generated_array1 = grid.get_column(0)
        generated_array2 = grid.get_column(1)
        generated_array3 = grid.get_column(2)
        generated_array4 = grid.get_column(3)
        
        test1 = np.allclose(generated_array1, true_column1)
        test2 = np.allclose(generated_array2, true_column2)
        test3 = np.allclose(generated_array3, true_column3)
        test4 = np.allclose(generated_array4, true_column4)
        
        self.assertTrue(test1 and test2 and test3 and test4)
    
      



if __name__ == '__main__':
    unittest.main()