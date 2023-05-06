from jaseci.actions.live_actions import jaseci_action
import subprocess
import time
from pynput.keyboard import Controller as KeyController, Key, Listener

keyboard = KeyController()


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




# import subprocess

# # Replace <TERMINAL_PID> with the actual PID of the desired terminal window
# terminal_pid = "55365"

# # Define the command to execute
# command = "echo 'Hello, World!'"

# # Execute the command in the terminal window using the PID
# subprocess.run(['osascript', '-e', 'tell application "Terminal" to do script "{}" in window id {}'.format(command, terminal_pid)])


import subprocess

def get_open_terminals_count():
    # Run AppleScript to get the count of open terminals
    script = 'tell application "System Events" to count windows of process "Terminal"'
    result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
    
    # Parse the output and return the count
    count = int(result.stdout.strip()) if result.stdout else 0
    return count

# Example usage
open_terminals_count = get_open_terminals_count()
print("Open Terminals Count:", open_terminals_count)
