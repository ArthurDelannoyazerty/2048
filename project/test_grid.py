from actions import Actions
from grid import Grid
import numpy as np
import unittest

class TestGrid(unittest.TestCase):

    def test_get_column_grid_empty_4_4(self): 
        """Test that an empty grid returns empty columns"""
        grid = Grid(4) 
        
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

    def test_get_column_grid_custom_4_4(self): 
        """Test that a custom grid returns good columns"""
        grid = Grid(4) 
        
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
    
    def test_get_column_grid_custom_5_5(self): 
        """Test that a custom grid returns good columns"""
        grid = Grid(5) 
        
        grid.matrix = np.array([[1, 2, 3, 4, 5], 
                                [4, 3, 2, 1, 0],
                                [5, 6, 7, 8, 9], 
                                [8, 7, 6, 5, 4],
                                [1, 2, 3, 4, 5]])
        
        true_column1 = np.array([1, 4, 5, 8, 1])
        true_column2 = np.array([2, 3, 6, 7, 2])
        true_column3 = np.array([3, 2, 7, 6, 3])
        true_column4 = np.array([4, 1, 8, 5, 4])
        true_column5 = np.array([5, 0, 9, 4, 5])
        
        generated_array1 = grid.get_column(0)
        generated_array2 = grid.get_column(1)
        generated_array3 = grid.get_column(2)
        generated_array4 = grid.get_column(3)
        generated_array5 = grid.get_column(4)
        
        test1 = np.allclose(generated_array1, true_column1)
        test2 = np.allclose(generated_array2, true_column2)
        test3 = np.allclose(generated_array3, true_column3)
        test4 = np.allclose(generated_array4, true_column4)
        test5 = np.allclose(generated_array5, true_column5)
        
        self.assertTrue(test1 and test2 and test3 and test4 and test5)
    
    def test_get_row_grid_empty_4_4(self): 
        """Test that an empty grid returns empty rows"""
        grid = Grid(4) 
        
        grid.matrix = np.array([[0, 0, 0, 0], 
                                [0, 0, 0, 0],
                                [0, 0, 0, 0], 
                                [0, 0, 0, 0]])
        
        true_array = np.array([0, 0, 0, 0])
        generated_array1 = grid.get_row(0)
        generated_array2 = grid.get_row(1)
        generated_array3 = grid.get_row(2)
        generated_array4 = grid.get_row(3)
        
        test1 = np.allclose(generated_array1, true_array)
        test2 = np.allclose(generated_array2, true_array)
        test3 = np.allclose(generated_array3, true_array)
        test4 = np.allclose(generated_array4, true_array)
        
        self.assertTrue(test1 and test2 and test3 and test4)

    def test_get_row_grid_custom_4_4(self): 
        """Test that a custom grid returns good rows"""
        grid = Grid(4) 
        
        grid.matrix = np.array([[1, 2, 3, 4], 
                                [4, 3, 2, 1],
                                [5, 6, 7, 8], 
                                [8, 7, 6, 5]])
        
        true_row1 = np.array([1, 2, 3, 4])
        true_row2 = np.array([4, 3, 2, 1])
        true_row3 = np.array([5, 6, 7, 8])
        true_row4 = np.array([8, 7, 6, 5])
        
        generated_array1 = grid.get_row(0)
        generated_array2 = grid.get_row(1)
        generated_array3 = grid.get_row(2)
        generated_array4 = grid.get_row(3)
        
        test1 = np.allclose(generated_array1, true_row1)
        test2 = np.allclose(generated_array2, true_row2)
        test3 = np.allclose(generated_array3, true_row3)
        test4 = np.allclose(generated_array4, true_row4)
        
        self.assertTrue(test1 and test2 and test3 and test4)

    def test_get_row_grid_custom_5_5(self): 
        """Test that a custom grid returns good rows"""
        grid = Grid(5) 
        
        grid.matrix = np.array([[1, 2, 3, 4, 5], 
                                [4, 3, 2, 1, 0],
                                [5, 6, 7, 8, 9], 
                                [8, 7, 6, 5, 4],
                                [1, 2, 3, 4, 5]])
        
        true_row1 = np.array([1, 2, 3, 4, 5])
        true_row2 = np.array([4, 3, 2, 1, 0])
        true_row3 = np.array([5, 6, 7, 8, 9])
        true_row4 = np.array([8, 7, 6, 5, 4])
        true_row5 = np.array([1, 2, 3, 4, 5])
        
        generated_array1 = grid.get_row(0)
        generated_array2 = grid.get_row(1)
        generated_array3 = grid.get_row(2)
        generated_array4 = grid.get_row(3)
        generated_array5 = grid.get_row(4)
        
        test1 = np.allclose(generated_array1, true_row1)
        test2 = np.allclose(generated_array2, true_row2)
        test3 = np.allclose(generated_array3, true_row3)
        test4 = np.allclose(generated_array4, true_row4)
        test5 = np.allclose(generated_array5, true_row5)
        
        self.assertTrue(test1 and test2 and test3 and test4 and test5)


if __name__ == '__main__':
    unittest.main()