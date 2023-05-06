

from pynput import mouse
from jaseci.actions.live_actions import jaseci_action
import time
from pynput.mouse import Controller, Button


@jaseci_action(act_group=["mouse"], allow_remote=True)
def record_first_mouse_click_position():
    # Create a function to handle mouse clicks
    def on_click(x, y, pressed):
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
mouse = Controller()


@jaseci_action(act_group=["mouse"], allow_remote=True)
def click_mouse(x, y):

    position = (float(x), float(y))
    mouse.position = position
    time.sleep(1)
    mouse.click(Button.left)
    time.sleep(2)
