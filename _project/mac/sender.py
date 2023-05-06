# import socket

# # Connect to the server
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(('localhost', 12345))

# # Send commands to the server
# command = "echo 'Hello, World!'"
# command = "echo 'Hello, World!'"
# client_socket.sendall(command.encode())

# # Close the socket
# client_socket.close()



# import socket

# # Function to connect to the server and send commands
# def connect_and_send(command):
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect(('localhost', 12345))
#     # Send command to the server
#     client_socket.sendall(command.encode())
#     # Close the client socket
#     client_socket.close()

# # Example usage: connect to the server and send a command
# command = "echo 'ls'"
# connect_and_send(command)


# import pexpect

# # Spawn a child process
# child = pexpect.spawn('ls')

# # Wait for the command to complete
# child.expect(pexpect.EOF)

# # Get the output
# output = child.before.decode()
# print(output)

# # Close the child process
# child.close()



# import subprocess

# applescript_code = """
# -- Set the target terminal window title or process name
# set targetTitle to "My Terminal" -- Replace with your target terminal window title or process name

# -- Find the terminal window by title or process name
# tell application "Terminal"
#     set targetWindow to missing value
#     repeat with win in windows
#         if (name of win) is equal to targetTitle or (process of win) is equal to targetTitle then
#             set targetWindow to win
#             exit repeat
#         end if
#     end repeat

#     -- Check if the target terminal window was found
#     if targetWindow is not missing value then
#         -- Activate the target terminal window
#         activate targetWindow

#         -- Run commands in the target terminal window
#         tell application "System Events" to tell process "Terminal"
#             keystroke "echo Hello, World!" & return -- Replace with your desired command
#         end tell
#     else
#         display alert "Terminal not found!" message "The target terminal window was not found."
#     end if
# end tell
# """

# # Execute the AppleScript code using osascript
# subprocess.run(["osascript", "-e", applescript_code])


# import subprocess

# applescript_code = """
# -- Set the target terminal window title
# set targetTitle to "My Terminal" -- Replace with your target terminal window title

# -- Find the terminal window by title
# tell application "Terminal"
#     set targetWindow to missing value
#     repeat with win in windows
#         if (name of win) is equal to targetTitle then
#             set targetWindow to win
#             exit repeat
#         end if
#     end repeat

#     -- Check if the target terminal window was found
#     if targetWindow is not missing value then
#         -- Activate the target terminal window
#         activate targetWindow

#         -- Run commands in the target terminal window
#         tell application "System Events" to tell process "Terminal"
#             keystroke "echo Hello, World!" & return -- Replace with your desired command
#         end tell
#     else
#         display alert "Terminal not found!" message "The target terminal window was not found."
#     end if
# end tell
# """

# # Execute the AppleScript code using osascript
# subprocess.run(["osascript", "-e", applescript_code])



import pyautogui

def is_text_cursor_visible():
    position = pyautogui.position()
    pixel_color = pyautogui.pixel(position[0], position[1])
    pixel_color != (0, 0, 0)  # Check if the pixel color is non-black
    print("Text Cursor Visible:", pixel_color)
    return pixel_color

# def is_vertical_line_visible():
#     position = pyautogui.position()
#     pixel_color = pyautogui.pixel(position[0], position[1])
#     return pixel_color == (0, 0, 255)  # Check if the pixel color is blue

# # Check if the text cursor is visible
# text_cursor_visible = is_text_cursor_visible()
# print("Text Cursor Visible:", text_cursor_visible)

# # Check if the vertical line is visible
# vertical_line_visible = is_vertical_line_visible()
# print("Vertical Line Visible:", vertical_line_visible)
