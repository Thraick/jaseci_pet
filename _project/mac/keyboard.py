from jaseci.actions.live_actions import jaseci_action
import subprocess
import time

from pynput.mouse import Controller, Button
from pynput.keyboard import Controller as KeyController, Key, Listener

mouse = Controller()
keyboard = KeyController()


@jaseci_action(act_group=["keyboard"], allow_remote=True)
def click_mouse(x, y):

    position = (float(x), float(y))
    mouse.position = position
    time.sleep(1)
    mouse.click(Button.left)
    time.sleep(2)



@jaseci_action(act_group=["keyboard"], allow_remote=True)
def type_command():
    command = 'osascript -e \'tell application "Terminal" to id of window 1\''

    time.sleep(1)

    # keyboard = Controller()
    keyboard.type(command)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    return "Command entered"

@jaseci_action(act_group=["keyboard"], allow_remote=True)
def run_command(command):
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        print(f"Error running command '{command}': {error.decode()}")
    return output.decode()



# osascript -e 'tell application "Terminal" to id of window 1'