import curses

def get_cursor_position():
    # initialize curses
    stdscr = curses.initscr()

    # turn off cursor display
    curses.curs_set(0)

    # get cursor position
    row, col = curses.getsyx()

    # restore cursor display
    curses.curs_set(1)

    # end curses
    curses.endwin()

    return row, col

# call the function to get the current cursor position
row, col = get_cursor_position()

print("Cursor position: row = {}, col = {}".format(row, col))
