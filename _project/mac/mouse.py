

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


# record_first_mouse_click_position()