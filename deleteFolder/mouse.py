# import pyautogui

# def record_and_click():
#     click_position = None
#     while click_position is None:
#         original_position = pyautogui.position()
#         print("Click anywhere on the screen...")
#         click_position = pyautogui.click()
#         print("Clicked at position:", click_position)


# record_and_click()

# import Quartz.CoreGraphics as cg

# def record_and_click():
#     click_position = None
#     while click_position is None:
#         print("Click anywhere on the screen...")
#         event = cg.wait_event()
#         if event['event'] == cg.kCGEventLeftMouseDown:
#             click_position = event['location']
#             print("Clicked at position:", click_position)


# record_and_click()



# import sys
# import platform
# import pyautogui

# def record_and_click():
#     click_position = None
#     while click_position is None:
#         print("Click anywhere on the screen...")
#         if platform.system() == "Darwin":
#             # macOS uses left mouse button for click
#             pyautogui.mouseDown(button='left')
#             pyautogui.mouseUp(button='left')
#         else:
#             # Linux uses left mouse button for click
#             pyautogui.mouseDown(button='left')
#             pyautogui.mouseUp(button='left')
#         click_position = pyautogui.position()
#         if click_position is not None:
#             print("Clicked at position:", click_position)
#             break


# record_and_click()


# # Clicked at position: Point(x=852, y=767)


# import pyautogui

# def get_click_position():
#     print("Click anywhere on the screen...")
#     # pyautogui.mouseDown()
#     # pyautogui.mouseUp()
#     click_position = pyautogui.position()
#     print("Clicked at position:", click_position)


# get_click_position()


# import pygame

# # Initialize pygame
# pygame.init()

# # Get the dimensions of the screen
# screen_info = pygame.display.Info()
# screen_width, screen_height = screen_info.current_w, screen_info.current_h

# # Set up the screen
# screen = pygame.display.set_mode((screen_width, screen_height))

# # List to store mouse click positions
# click_positions = []

# # Main game loop
# while True:
#     # Handle events
#     for event in pygame.event.get():
#         # Check for mouse button click
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             # Get the position of the mouse click
#             mouse_pos = pygame.mouse.get_pos()
            
#             # Record the position
#             click_positions.append(mouse_pos)
            
#             # Quit the game
#             pygame.quit()
#             quit()

#         # Check for quit event
#         if event.type == pygame.QUIT:
#             # Quit the game
#             pygame.quit()
#             quit()

#     # Update the display
#     pygame.display.update()


# import pyautogui

# Wait for user to click the mouse
# click_pos = pyautogui.locateOnScreen('click_prompt.png')
# while click_pos is None:
#     click_pos = pyautogui.locateOnScreen('click_prompt.png')

# Record the position of the first mouse click
# mouse_pos = pyautogui.position()

# Quit the program
# quit()


import time
from pynput import mouse

def record_first_mouse_click_position():
    # Create a function to handle mouse clicks
    def on_click(x, y, button, pressed):
        if pressed:
            # Record the position of the first mouse click
            nonlocal mouse_pos
            mouse_pos = (x, y)
            print(mouse_pos)

            # Stop listening for mouse clicks
            return False

    # Create a listener for mouse clicks
    mouse_pos = None
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    return mouse_pos


# mouse_pos = record_first_mouse_click_position()

# (538.2100219726562, 784.7853393554688) first

# (765.9791259765625, 812.3346557617188) terminal
# (1320.7354736328125, 610.0415649414062) new ternimal 





# from pynput.mouse import Button, Controller

# def click_at_position(position):
#     # Create a mouse controller object
#     mouse = Controller()

#     # Move the mouse to the given coordinates
#     mouse.position = position

#     # Click the left mouse button at the current position
#     mouse.click(Button.left)

# # click_at_position((765.9791259765625, 812.3346557617188))


# from pynput.mouse import Controller

# def move_mouse_to_position(position):
#     # Create a mouse controller object
#     mouse = Controller()

#     # Move the mouse to the given coordinates
#     mouse.position = position

#     click_at_position(position)

# move_mouse_to_position((765.9791259765625, 812.3346557617188))




# import atexit
# from pynput.mouse import Controller, Button

# import os
# # Create a mouse controller object
# mouse = Controller()

# # Define the function to move the mouse to the given position
# def move_mouse_to_position(position):
#     mouse.position = position
#     mouse.click(Button.left)
#     os.system('jsctl -m')

# # Register the function to be called when the code stops running
# atexit.register(move_mouse_to_position, (765.9791259765625, 812.3346557617188))




import atexit
from pynput.mouse import Controller, Button

from pynput.keyboard import Controller as KeyController, Key


import os

# Create a mouse controller object
mouse = Controller()

# Define the function to move the mouse to the given position and click
def move_mouse_and_type(position):
    mouse.position = position
    time.sleep(1)
    mouse.click(Button.left)

    # Wait for a short time to give the terminal time to activate
    time.sleep(1)
    keyboard = KeyController()

    # Type the first part of the command
    keyboard.type('jsctl -m')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(5)
    keyboard.type('actions list')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


    # Type the command in the terminal
    # os.system(command)

# Register the function to be called when the code stops running
atexit.register(move_mouse_and_type, (538.2100219726562, 784.7853393554688))


# import atexit
# import time
# from pynput.keyboard import Controller, Key
# from pynput.mouse import Controller as MouseController, Button

# def type_command(command):
#     # Create a keyboard controller object
#     keyboard = Controller()

#     # Type the command
#     keyboard.type(command)

# def click_position(position):
#     # Create a mouse controller object
#     mouse = MouseController()

#     # Click the mouse at the given position
#     mouse.position = position
#     mouse.click(Button.left)
#     time.sleep(1)

# def type_and_click(position):
    # Type the first part of the command
    

    # Get the current position of the keyboard focus
    # focus_position = Controller().position

    # Click the mouse at the desired position
    # click_position(position)

    # Move the keyboard focus back to the previous position and type the second part of the command
    # Controller().position = focus_position
    # type_command('jsctl -m')
    # time.sleep(5)
    # type_command('alias list')

# atexit.register(type_and_click, (538.2100219726562, 784.7853393554688))