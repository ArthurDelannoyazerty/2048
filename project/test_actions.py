from actions import Actions
from grid import Grid
import numpy as np
import unittest

class TestActions(unittest.TestCase):

    def test_empty_grid_up_4_4(self): 
        """Test that an empty grid is still empty after an action"""
        grid = Grid(4) 
        action = Actions(grid)
        grid.matrix = np.array([[0, 0, 0, 0], 
                                [0, 0, 0, 0],
                                [0, 0, 0, 0],
                                [0, 0, 0, 0]])
        old_matrix = grid.matrix
        action.action_up()
        
        test = np.allclose(grid.matrix, old_matrix)
        
        self.assertTrue(test)
          
    def test_custom_grid_up_4_4(self): 
        """Test that an empty grid is still empty after an action"""
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
        
        action.action_up()#TODO check qction up
        
        test = np.allclose(grid.matrix, true_matrix)
        
        self.assertTrue(test)


if __name__ == '__main__':
    unittest.main()