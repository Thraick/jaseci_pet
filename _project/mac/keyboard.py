from jaseci.actions.live_actions import jaseci_action
import subprocess
import time
from pynput.keyboard import Controller as KeyController, Key, Listener

keyboard = KeyController()


@jaseci_action(act_group=["keyboard"], allow_remote=True)
def type_command(command):
    # command = 'osascript -e \'tell application "Terminal" to id of window 1\''

    # time.sleep(1)

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




import pyautogui

@jaseci_action(act_group=["keyboard"], allow_remote=True)
def is_text_cursor_visible():
    position = pyautogui.position()
    pixel_color = pyautogui.pixel(position[0], position[1])
    pixel_color != (0, 0, 0)  # Check if the pixel color is non-black
    print("Text Cursor Visible:", pixel_color)
    return pixel_color






@jaseci_action(act_group=["keyboard"], allow_remote=True)
def run_command_when_cursor_available(command):
    while not is_text_cursor_visible():
        time.sleep(1)  # Wait for 1 second if cursor is not available
    type_command(command)



# osascript -e 'tell application "Terminal" to id of window 1'


# def run_command_in_terminal(command, window_id):
#     # Build the AppleScript command to run the command in the specified window
#     # script = f'tell application "Terminal"\n do script "{command}" in window id {window_id}\nend tell'

#     # # Use subprocess to run the script using osascript
#     # subprocess.run(['osascript', '-e', script])

#     # Escape any double quotes in the command string
#     # escaped_command = command.replace('"', '\\"')

#     # # Build the AppleScript command to run the command in the specified window
#     # script = f'tell application "Terminal"\n do script "{escaped_command}" in window id {window_id}\nend tell'

#     # # Use subprocess to run the script using osascript
#     # subprocess.run(['osascript', '-e', script])

#     escaped_command = command.replace('"', '\\"')

#     # Build the AppleScript command to run the command in the specified tab of the specified window
#     script = f'tell application "Terminal"\n do script "{escaped_command}" in tab 1 of window id {window_id}\nend tell'
    
#     # Use subprocess to run the script using osascript
#     subprocess.run(['osascript', '-e', script])


# # command = 'echo "Hello, world"'
# # run_command_in_terminal(command=command, window_id=35709)


# import os

# # Replace "your command here" with the command you want to run in the terminal
# command = "ls"

# # Replace 35709 with the terminal ID you want to run the command in
# terminal_id = "35709"

# # os.system(f"osascript -e 'tell application \"Terminal\" to do script \"{command}\" in window id {terminal_id}'")
# # os.system(f"osascript -e 'tell application \"Terminal\" to do script \"{command}\" in tab 1 of window id {terminal_id}'")
# # os.system(f"osascript -e 'tell application \"Terminal\" to do script \"{command}\" in tab of window id {terminal_id}'")


# # def run_command(command):
# #     process = subprocess.Popen(
# #         command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# #     output, error = process.communicate()
# #     if error:
# #         print(f"Error running command '{command}': {error.decode()}")
# #     return output.decode()


# # output = run_command("ls -la")
# # print(output)

# # # pid = os.getpid()
# # pid = 35709

# # subprocess.run(["ls"], env={"TERM_SESSION_ID": str(pid)})

# # Replace this with the title of the target Terminal window
# # target_title = "My Terminal Window"

# # # Construct the AppleScript command to send the "ls" command to the target window
# # command = f'tell application "Terminal" to do script "ls" in window 1 where name contains "{target_title}"'

# # # Execute the AppleScript command using the osascript tool
# # subprocess.run(["osascript", "-e", command])



# def click_mouse_1(command):

#     # Send the command to the active terminal window using AppleScript
#     applescript = 'tell application "System Events" to keystroke "{}\\r"'.format(command)
#     subprocess.Popen(['osascript', '-e', applescript])

#     # Wait for the command to finish running
#     while True:
#         try:
#             # Try to find the process ID of the command and send a SIGINT signal to it
#             pid = subprocess.check_output(['pgrep', '-f', command])
#             print (pid)
#             pid = pid.decode('utf-8').strip()
#             subprocess.Popen(['kill', '-2', pid])
#             break
#         except subprocess.CalledProcessError:

#             # If the process doesn't exist anymore, break out of the loop
#             break


# click_mouse_1('ls')



# import os

# def run_command_in_terminal(command, window_id, tab_index):
#     os.system(f"osascript -e 'tell application \"Terminal\" to do script \"{command}\" in tab {tab_index} of window id {window_id}'")


# window_id = "35709"  # Replace with the actual window ID
# tab_index = 1  
# run_command_in_terminal("ls -l", window_id, tab_index)



import subprocess

# Get the title of the Terminal window
def get_terminal_title(window_id):
    script = '''
    tell application "Terminal"
        set targetWindow to window id {}
        return name of targetWindow
    end tell
    '''.format(window_id)

    result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
    return result.stdout.strip()

# Replace <WINDOW_ID> with the actual ID of the desired terminal window
window_id = "<WINDOW_ID>"

# Get the title of the Terminal window
terminal_title = get_terminal_title(window_id)
print("Terminal window title:", terminal_title)


import subprocess

# Set the title of the Terminal window
def set_terminal_title(window_id, title):
    script = '''
    tell application "Terminal"
        set targetWindow to window id {}
        set custom title of targetWindow to "{}"
    end tell
    '''.format(window_id, title)

    subprocess.run(['osascript', '-e', script])

# Replace <WINDOW_ID> with the actual ID of the desired terminal window
window_id = "39480"
new_title = "New Terminal Title"

# Set the title of the Terminal window
# set_terminal_title(window_id, new_title)
