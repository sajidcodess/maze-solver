import unittest
from graphics import Window
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 8
        num_rows = 6
        margin = 0
        window = Window(800, 600)
        m = Maze(margin, margin, num_rows, num_cols, 8, 8, window)
        self.assertEqual(len(m._cells), num_cols)
        self.assertEqual(len(m._cells[0]), num_rows)


if __name__ == "__main__":
    unittest.main()
