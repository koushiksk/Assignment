import unittest
from conways_life.universe import Universe

class TestGameOfLife(unittest.TestCase):
    """Test cases for the Game of Life implementation."""

    def test_block_pattern(self):
        """Test a stable block pattern (still life)."""
        # Input A
        initial_cells = {(1, 1), (1, 2), (2, 1), (2, 2)}
        expected_next_gen = {(1, 1), (1, 2), (2, 1), (2, 2)}
        
        universe = Universe(initial_cells)
        universe.tick()
        
        self.assertEqual(universe.get_live_cells(), expected_next_gen)

    def test_boat_pattern(self):
        """Test a stable boat pattern (still life)."""
        # Input B
        initial_cells = {(0, 1), (1, 0), (2, 1), (0, 2), (1, 2)}
        expected_next_gen = {(0, 1), (1, 0), (2, 1), (0, 2), (1, 2)}

        universe = Universe(initial_cells)
        universe.tick()

        self.assertEqual(universe.get_live_cells(), expected_next_gen)

    def test_blinker_pattern(self):
        """Test a simple oscillator (blinker)."""
        # Input C
        initial_cells = {(1, 1), (1, 0), (1, 2)}
        expected_next_gen = {(1, 1), (0, 1), (2, 1)}

        universe = Universe(initial_cells)
        universe.tick()

        self.assertEqual(universe.get_live_cells(), expected_next_gen)
    
    def test_toad_pattern(self):
        """Test a two-phase oscillator (toad)."""
        # Input D
        initial_cells = {(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (2, 4)}
        expected_next_gen = {(0, 2), (1, 1), (1, 4), (2, 1), (2, 4), (3, 3)}

        universe = Universe(initial_cells)
        universe.tick()

        self.assertEqual(universe.get_live_cells(), expected_next_gen)


if __name__ == "__main__":
    unittest.main() 