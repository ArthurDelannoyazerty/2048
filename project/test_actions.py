from actions import Actions
from grid import Grid
import numpy as np
import unittest

class TestActions(unittest.TestCase):

    def test_empty_grid_up_4_4(self): 
        """Test that an empty grid is still empty after an action"""
        grid = Grid(4) 
        action = Actions(grid)
        old_matrix = grid.matrix
        action.action_up()
        
        test = np.allclose(grid.matrix, old_matrix)
        
        self.assertTrue(test)
          
    def test_custom_grid_up_4_4_solo(self): 
        grid = Grid(4) 
        action = Actions(grid)
        grid.matrix = np.array([[0, 0, 0, 0], 
                                [2, 2, 2, 0],
                                [0, 0, 0, 2],
                                [0, 0, 0, 0]])
        
        true_matrix = np.array([[2, 2, 2, 2], 
                                [0, 0, 0, 0],
                                [0, 0, 0, 0],
                                [0, 0, 0, 0]])
        
        action.action_up()
        
        test = np.allclose(grid.matrix, true_matrix)
        
        self.assertTrue(test)
    
    def test_custom_grid_up_4_4_same_multiple_1(self): 
        grid = Grid(4) 
        action = Actions(grid)
        grid.matrix = np.array([[0, 0, 0, 2], 
                                [2, 2, 2, 0],
                                [2, 0, 0, 2],
                                [0, 0, 2, 0]])
        
        true_matrix = np.array([[4, 2, 4, 4], 
                                [0, 0, 0, 0],
                                [0, 0, 0, 0],
                                [0, 0, 0, 0]])
        
        action.action_up()
        
        test = np.allclose(grid.matrix, true_matrix)
        
        self.assertTrue(test)
    
    def test_custom_grid_up_4_4_same_multiple_2(self): 
        grid = Grid(4) 
        action = Actions(grid)
        grid.matrix = np.array([[0, 0, 0, 2], 
                                [2, 2, 2, 0],
                                [4, 0, 4, 2],
                                [0, 8, 2, 4]])
        
        true_matrix = np.array([[2, 2, 2, 4], 
                                [4, 8, 4, 4],
                                [0, 0, 2, 0],
                                [0, 0, 0, 0]])
        
        action.action_up()
        
        test = np.allclose(grid.matrix, true_matrix)
        
        self.assertTrue(test)
    
    def test_custom_grid_up_4_4_same_multiple_3(self): 
        grid = Grid(4) 
        action = Actions(grid)
        grid.matrix = np.array([[2, 0, 0, 2], 
                                [2, 2, 2, 2],
                                [2, 8, 4, 2],
                                [2, 8, 4, 4]])
        
        true_matrix = np.array([[4, 2,  2, 4], 
                                [4, 16, 8, 2],
                                [0, 0,  0, 4],
                                [0, 0,  0, 0]])
        
        action.action_up()
        
        test = np.allclose(grid.matrix, true_matrix)
        
        self.assertTrue(test)


    def test_empty_grid_down_4_4(self): 
        """Test that an empty grid is still empty after an action"""
        grid = Grid(4) 
        action = Actions(grid)
        old_matrix = grid.matrix
        action.action_down()
        
        test = np.allclose(grid.matrix, old_matrix)
        
        self.assertTrue(test)
          
    def test_custom_grid_down_4_4_solo(self): 
        grid = Grid(4) 
        action = Actions(grid)
        grid.matrix = np.array([[0, 0, 0, 0], 
                                [2, 2, 2, 0],
                                [0, 0, 0, 2],
                                [0, 0, 0, 0]])
        
        true_matrix = np.array([[0, 0, 0, 0], 
                                [0, 0, 0, 0],
                                [0, 0, 0, 0],
                                [2, 2, 2, 2]])
        
        action.action_down()
        
        test = np.allclose(grid.matrix, true_matrix)
        
        self.assertTrue(test)
    
    def test_custom_grid_down_4_4_same_multiple_1(self): 
        grid = Grid(4) 
        action = Actions(grid)
        grid.matrix = np.array([[0, 0, 0, 2], 
                                [2, 2, 2, 0],
                                [2, 0, 0, 2],
                                [0, 0, 2, 0]])
        
        true_matrix = np.array([[0, 0, 0, 0], 
                                [0, 0, 0, 0],
                                [0, 0, 0, 0],
                                [4, 2, 4, 4]])
        
        action.action_down()
        
        test = np.allclose(grid.matrix, true_matrix)
        
        self.assertTrue(test)
    
    def test_custom_grid_down_4_4_same_multiple_2(self): 
        grid = Grid(4) 
        action = Actions(grid)
        grid.matrix = np.array([[0, 0, 0, 2], 
                                [2, 2, 2, 0],
                                [4, 0, 4, 2],
                                [0, 8, 2, 4]])
        
        true_matrix = np.array([[0, 0, 0, 0], 
                                [0, 0, 2, 0],
                                [2, 2, 4, 4], 
                                [4, 8, 2, 4]])
        
        action.action_down()
        
        test = np.allclose(grid.matrix, true_matrix)
        
        self.assertTrue(test)
    
    def test_custom_grid_down_4_4_same_multiple_3(self): 
        grid = Grid(4) 
        action = Actions(grid)
        grid.matrix = np.array([[2, 0, 0, 2], 
                                [2, 2, 2, 2],
                                [2, 8, 4, 2],
                                [2, 8, 4, 4]])
        
        true_matrix = np.array([[0, 0,  0, 0], 
                                [0, 0,  0, 2],
                                [4, 2,  2, 4],
                                [4, 16, 8, 4]])
        
        action.action_down()
        
        test = np.allclose(grid.matrix, true_matrix)
        
        self.assertTrue(test)
        

    def test_empty_grid_left_4_4(self): 
        """Test that an empty grid is still empty after an action"""
        grid = Grid(4) 
        action = Actions(grid)
        old_matrix = grid.matrix
        action.action_left()
        
        test = np.allclose(grid.matrix, old_matrix)
        
        self.assertTrue(test)
          
    def test_custom_grid_left_4_4_solo(self): 
        grid = Grid(4) 
        action = Actions(grid)
        grid.matrix = np.array([[0, 0, 2, 0], 
                                [0, 0, 2, 0],
                                [0, 0, 2, 0],
                                [0, 2, 0, 0]])
        
        true_matrix = np.array([[2, 0, 0, 0], 
                                [2, 0, 0, 0],
                                [2, 0, 0, 0],
                                [2, 0, 0, 0]])
        
        action.action_left()
        
        test = np.allclose(grid.matrix, true_matrix)
        
        self.assertTrue(test)
    
    def test_custom_grid_left_4_4_same_multiple_1(self): 
        grid = Grid(4) 
        action = Actions(grid)
        grid.matrix = np.array([[0, 2, 2, 0], 
                                [0, 0, 2, 2],
                                [2, 0, 0, 2],
                                [0, 0, 0, 2]])
        
        true_matrix = np.array([[4, 0, 0, 0], 
                                [4, 0, 0, 0],
                                [4, 0, 0, 0],
                                [2, 0, 0, 0]])
        
        action.action_left()
        
        test = np.allclose(grid.matrix, true_matrix)
        
        self.assertTrue(test)
    
    def test_custom_grid_left_4_4_same_multiple_2(self): 
        grid = Grid(4) 
        action = Actions(grid)
        grid.matrix = np.array([[0, 4, 2, 0], 
                                [8, 0, 2, 0],
                                [2, 4, 2, 0],
                                [4, 2, 0, 2]])
        
        
        true_matrix = np.array([[4, 2, 0, 0], 
                                [8, 2, 0, 0],
                                [2, 4, 2, 0], 
                                [4, 4, 0, 0]])
        
        action.action_left()
        
        test = np.allclose(grid.matrix, true_matrix)
        
        self.assertTrue(test)
    
    def test_custom_grid_left_4_4_same_multiple_3(self): 
        grid = Grid(4) 
        action = Actions(grid)
        grid.matrix = np.array([[2, 2, 2, 2], 
                                [8, 8, 2, 0],
                                [4, 4, 2, 0],
                                [4, 2, 2, 2]])
                                
        true_matrix = np.array([[4,  4,  0, 0], 
                                [16, 2,  0, 0],
                                [8,  2,  0, 0],
                                [4,  4,  2, 0]])
        
        action.action_left()
        
        test = np.allclose(grid.matrix, true_matrix)
        
        self.assertTrue(test)


    def test_empty_grid_right_4_4(self): 
        """Test that an empty grid is still empty after an action"""
        grid = Grid(4) 
        action = Actions(grid)
        old_matrix = grid.matrix
        action.action_right()
        
        test = np.allclose(grid.matrix, old_matrix)
        
        self.assertTrue(test)
          
    def test_custom_grid_right_4_4_solo(self): 
        grid = Grid(4) 
        action = Actions(grid)
        grid.matrix = np.array([[0, 0, 2, 0], 
                                [0, 0, 2, 0],
                                [0, 0, 2, 0],
                                [0, 2, 0, 0]])
        
        true_matrix = np.array([[0, 0, 0, 2], 
                                [0, 0, 0, 2],
                                [0, 0, 0, 2],
                                [0, 0, 0, 2]])
        
        action.action_right()
        
        test = np.allclose(grid.matrix, true_matrix)
        
        self.assertTrue(test)
    
    
    def test_custom_grid_right_4_4_same_multiple_1(self): 
        grid = Grid(4) 
        action = Actions(grid)
        grid.matrix = np.array([[0, 2, 2, 0], 
                                [0, 0, 2, 2],
                                [2, 0, 0, 2],
                                [0, 0, 0, 2]])
        
        true_matrix = np.array([[0, 0, 0, 4], 
                                [0, 0, 0, 4],
                                [0, 0, 0, 4],
                                [0, 0, 0, 2]])
        
        action.action_right()
        
        test = np.allclose(grid.matrix, true_matrix)
        
        self.assertTrue(test)
    
    
    def test_custom_grid_right_4_4_same_multiple_2(self): 
        grid = Grid(4) 
        action = Actions(grid)
        grid.matrix = np.array([[0, 4, 2, 0], 
                                [8, 0, 2, 0],
                                [2, 4, 2, 0],
                                [4, 2, 0, 2]])
        
        
        true_matrix = np.array([[0, 0, 4, 2], 
                                [0, 0, 8, 2],
                                [0, 2, 4, 2], 
                                [0, 0, 4, 4]])
        
        action.action_right()
        
        test = np.allclose(grid.matrix, true_matrix)
        
        self.assertTrue(test)
    
    def test_custom_grid_right_4_4_same_multiple_3(self): 
        grid = Grid(4) 
        action = Actions(grid)
        grid.matrix = np.array([[2, 2, 2, 2], 
                                [8, 8, 2, 0],
                                [4, 4, 2, 0],
                                [4, 2, 2, 2]])
                                
        true_matrix = np.array([[0,  0,  4, 4], 
                                [0, 0,  16, 2],
                                [0,  0,  8, 2],
                                [0,  4,  2, 4]])
        
        action.action_right()
        
        test = np.allclose(grid.matrix, true_matrix)
        
        self.assertTrue(test)


if __name__ == '__main__':
    unittest.main()