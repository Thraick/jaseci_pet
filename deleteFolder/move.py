import subprocess

def run_command_in_new_terminal(command):
    script = f'tell application "Terminal"\n' \
             f'    do script "{command}"\n' \
             f'    activate\n' \
             f'end tell\n'
    subprocess.call(['osascript', '-e', script])



# run_command_in_new_terminal("jsctl -m")
# run_command_in_new_terminal("jsctl -m")


import subprocess

script = 'tell application "Terminal" to id of window 1'
result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)

# Extract the window ID from the output
window_id = result.stdout.strip()
print(f"The ID of Window 1 is: {window_id}")


# osascript -e 'tell application "Terminal" to id of window 1'
