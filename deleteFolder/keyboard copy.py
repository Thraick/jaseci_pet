import subprocess
import curses
from jaseci.actions.live_actions import jaseci_action
import os


import atexit
import time
import os
from pynput.mouse import Controller, Button
from pynput.keyboard import Controller as KeyController, Key, Listener
import psutil

# Create a mouse controller object
mouse = Controller()

# Create a keyboard controller object
keyboard = KeyController()


@jaseci_action(act_group=["keyboard"], allow_remote=True)
def click_mouse(x, y):

    position = (float(x), float(y))
    mouse.position = position
    time.sleep(1)
    mouse.click(Button.left)
    time.sleep(2)

    # current_window_pid = psutil.Process(os.getpid()).ppid()
    # return current_window_pid


# @jaseci_action(act_group=["keyboard"], allow_remote=True)
# def type_command(command, window_id):
#     time.sleep(1)

#     print('Window ID:', window_id)
#     # script = 'tell application "Terminal" to do script "{}" in window id "{}"'.format(command, window_id)
#     script = 'tell application "Terminal" to do script "{}" in tab 1 of window id "{}"'.format(command, window_id)


#     # Execute the command in the specified terminal window using subprocess
#     # script = 'tell application "Terminal" to do script "{}" in window id "{}"'.format(command, window_id)
#     process = subprocess.Popen(['osascript', '-e', script])

#     # Wait for the command to finish running
#     while process.poll() is None:
#         time.sleep(1)

#     return "Command entered"

@jaseci_action(act_group=["keyboard"], allow_remote=True)
def type_command():
    command = 'osascript -e \'tell application "Terminal" to id of window 1\''

    time.sleep(1)

    keyboard = Controller()
    keyboard.type(command)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    return "Command entered"

# def checkFocus():
#     def main(stdscr):

#         # Set a timeout for input
#         curses.halfdelay(10)

#         # Loop to handle input
#         while True:
#             # Read keyboard input
#             ch = stdscr.getch()

#             if ch == curses.KEY_FOCUSED:
#                 # Do something when the terminal window gains focus
#                 stdscr.addstr("Terminal window has focus\n")
#             elif ch != -1:
#                 # Do something with other input
#                 stdscr.addstr(f"Input received: {ch}\n")

#             # Refresh the screen
#             stdscr.refresh()

#     curses.wrapper(main)


# import os
# @jaseci_action(act_group=["keyboard"], allow_remote=True)
# def run_command(command, terminal_path):

   # Get the ID of the current terminal window
   # terminal_id = os.getpid()

   # Run the command in the current terminal window
   # os.system(f"echo '{command}' > /dev/pts/{terminal_id}; {command}")
   # os.system(f"echo '{command}' > /dev/ttys021; {command}")
   # os.system(f"echo '{command}' > {terminal_id}; {command} > /dev/tty")
   # os.system(f"echo '{command}' > {terminal_path}; {command}")
   # os.system(f"echo '{command}' > {terminal_path}; {command} > {terminal_path}; echo '\r' > {terminal_path}")

   # os.system(f"echo '{command}' > {terminal_path}; {command} > {terminal_path}")
   # os.system(f"echo '{command}' > {terminal_path}; {command} > {terminal_path}; echo '\r\r' > {terminal_path}")

   # subprocess.call(["osascript", "-e", f'tell application "Terminal" to do script "{command}" in window 1'], env={"TERM": "xterm-color", "TTY": terminal_path})


# run_command("ls", "39189")
# run_command("ls", "/dev/ttys021")

# import os

# pid = os.getpid()
# print(f"PID: {pid}")

@jaseci_action(act_group=["keyboard"], allow_remote=True)
def run_command(command):
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        print(f"Error running command '{command}': {error.decode()}")
    return output.decode()


output = run_command("ls -la")
print(output)


# import subprocess
# import time
# from pynput.mouse import Controller, Button

# mouse = Controller()


# @jaseci_action(act_group=["keyboard"], allow_remote=True)
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


# @jaseci_action(act_group=["keyboard"], allow_remote=True)
# def click_mouse_1(command):
#     # Execute the command and capture its output in real-time
#     process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#     # Wait for the command to finish running
#     while process.poll() is None:
#         # Send SIGINT signal to the process
#         process.send_signal(2)

#     # Get the output of the command
#     stdout, stderr = process.communicate()

#     # Print the output to the console
#     print(stdout.decode('utf-8'))


# click_mouse_1("python --version")

# import pexpect

# @jaseci_action(act_group=["keyboard"], allow_remote=True)
# def ox_move(text:str):
#     # os.system('jsctl -l')

#     # start a new process to run 'python --version'
#     child = pexpect.spawn('python', ['--version'])

#     # # wait for the command to complete
#     child.expect(pexpect.EOF)

#     # # print the output
#     print(child.before.decode())


# import os
# import sys
# import tty
# import termios
# import subprocess
# import select

# # Run a command and check if it has finished
# def run_command(cmd):
#     # Save current terminal attributes
#     attrs = termios.tcgetattr(sys.stdin)
#     try:
#         # Switch terminal to "raw" mode
#         tty.setraw(sys.stdin.fileno())

#         # Run the command in a subprocess
#         proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#         # Wait for the command to finish
#         while True:
#             # Check if the process has finished
#             poll = select.poll()
#             poll.register(proc.stdout, select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR)
#             poll.register(proc.stderr, select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR)
#             events = poll.poll(1000)
#             if not events and proc.poll() is not None:
#                 break

#             # Read and print output from the process
#             for fd, event in events:
#                 data = os.read(fd, 1024)
#                 sys.stdout.write(data.decode())
#                 sys.stdout.flush()

#     finally:
#         # Restore original terminal attributes
#         termios.tcsetattr(sys.stdin, termios.TCSADRAIN, attrs)

# # Call the function to run a command
# run_command("ls")
