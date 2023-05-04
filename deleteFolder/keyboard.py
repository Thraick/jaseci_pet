from pynput.keyboard import Controller, Key
import time
import pexpect

import os

import os

# os.system('jsctl -m')
# os.system('exit')


import subprocess

def interact_with_shell():
    p = subprocess.Popen(['python'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    p.stdin.write(b'print("hello")\n')
    p.stdin.flush()

    while True:
        output = p.stdout.readline().decode().strip()
        if output:
            print(output)
        else:
            break

interact_with_shell()

# # command to create a shell
# command = "jsctl -m"

# # create an interactive shell session
# shell = pexpect.spawn(command)

# # wait for the shell to start up
# shell.expect('\$')

# # send the command to the shell
# shell.sendline('alias list')

# # wait for the command to finish
# shell.expect('\$')

# # exit the shell
# shell.sendline('exit')



# import subprocess

# # command to create a shell
# command = "jsctl -m"

# # create the shell
# shell = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

# # command to run in the shell
# command = "alias list"

# # send the command to the shell
# shell.stdin.write(command.encode())

# # exit the shell
# shell.stdin.write(b"exit\n")





# # Create a keyboard controller
# keyboard = Controller()
# # os.system('jsctl -m')



# # Wait for a few seconds before typing
# time.sleep(5)
# # os.system('xdotool key ctrl+alt+t')

# # # Type the message
# # keyboard.type('jsctl -m')

# # time.sleep(5)
# # # Press Enter
# # keyboard.press(Key.enter)
# # keyboard.release(Key.enter)


# keyboard.type('alias list')

# time.sleep(5)
# # Press Enter
# keyboard.press(Key.enter)
# keyboard.release(Key.enter)

# # Open the terminal in the specified path
# terminal = pexpect.spawn('/bin/bash', ['-i'])
# terminal.expect('$')

# # Wait for a few seconds before typing
# time.sleep(5)

# # Run the jsctl -m command
# terminal.sendline('hello')
# terminal.sendline('jsctl -m')

# # Wait for a few seconds before typing
# time.sleep(5)

# # Type the message in the shell
# terminal.sendline('Hello, World!')



# import subprocess

# # command to create a shell
# command1 = "jsctl -m"

# # command to run alias list in the shell
# command2 = "alias list"

# # create the shell and execute the command
# with subprocess.Popen(command1, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True) as shell:
#     shell.stdin.write(command2.encode())
#     output, errors = shell.communicate()

# # print the output of the command
# print(output.decode())
