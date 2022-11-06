from actions import Actions
from grid import Grid
import numpy as np
import unittest

class TestActions(unittest.TestCase):

    def test_empty_grid(self): 
        """Test that an empty grid is still empty after an action"""
        grid = Grid() 
        action = Actions(grid)
        grid.matrix = np.array([[0, 0, 0], 
                                [0, 0, 0],
                                [0, 0, 0]])
        old_matrix = grid.matrix
        action.action_up()
        np.testing.assert_allclose(grid.matrix, old_matrix, "Test up empty matrix")
    
    
      



if __name__ == '__main__':
    unittest.main()