import curses
import atexit
import time
import os
from pynput.mouse import Controller, Button
from pynput.keyboard import Controller as KeyController, Key, Listener

# Create a mouse controller object
mouse = Controller()

# Create a keyboard controller object
keyboard = KeyController()

# Define a function to move the mouse to a given position and click


def click_mouse(position):
    mouse.position = position
    time.sleep(1)
    mouse.click(Button.left)

# Define a function to type a given command in the terminal


def on_press(key):
    if key == Key.right:
        # The text cursor has moved to the right, so we can run the next command
        return False


def type_command(command):
    # Wait for a short time to give the terminal time to activate
    time.sleep(1)

    # Type the command in the terminaljsctl -m
    keyboard.type(command)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # Listen for the Key.right arrow key event to determine that the text cursor has moved to the right
    with Listener(on_press=on_press) as listener:
        listener.join()

# Define a function to move the mouse to a given position, click, and type a command





# def move_mouse_click_and_type(position, command1, command2):
#     click_mouse(position)

#     type_command(command1)
#     type_command(command2)


# import ncurses as curses

# def move_mouse_click_and_type(position, command1, command2):
#     click_mouse(position)

#     # Set a timeout for input
#     curses.halfdelay(10)

#     # Create a new window for input
#     input_win = curses.newwin(1, curses.COLS, curses.LINES - 1, 0)

#     # Type the first command and wait for it to finish
#     type_command(command1)
#     while True:
#         # Check if the terminal window has focus
#         ch = input_win.getch()
#         if ch == curses.KEY_FOCUSED:
#             # Type the second command if the terminal window has focus
#             type_command(command2)
#             break
#         elif ch != -1:
#             # Handle other input
#             input_win.addstr(f"Input received: {ch}\n")

#     # Refresh the screen
#     input_win.refresh()



# # Register the function to be called when the code stops running
# atexit.register(move_mouse_click_and_type, (538.2100219726562,
#                 784.7853393554688), 'jsctl -m', 'actions list'
#                 )


import subprocess
import time
from pynput.mouse import Controller, Button

mouse = Controller()

def click_mouse_1(command):

    # Send the command to the active terminal window using AppleScript
    applescript = 'tell application "System Events" to keystroke "{}\\r"'.format(command)
    subprocess.Popen(['osascript', '-e', applescript])

    # Wait for the command to finish running
    while True:
        try:
            # Try to find the process ID of the command and send a SIGINT signal to it
            pid = subprocess.check_output(['pgrep', '-f', command])
            pid = pid.decode('utf-8').strip()
            subprocess.Popen(['kill', '-2', pid])
            break
        except subprocess.CalledProcessError:
            # If the process doesn't exist anymore, break out of the loop
            break




atexit.register(click_mouse, (538.2100219726562, 784.7853393554688))
atexit.register(click_mouse_1, 'ls')