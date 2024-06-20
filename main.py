from graphics import Window
from maze import Maze

def main():
    main_window_width = 1000
    main_window_height = 800
    num_rows = 12
    num_cols = 16
    margin = 30
    cell_size_x = (main_window_width - 2 * margin) / num_cols
    cell_size_y = (main_window_height - 2 * margin) / num_rows

    win = Window(main_window_width, main_window_height)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    print("maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("maze can't be solved")
    else:
        print("maze solved!")

    win.wait_for_close()

main()
