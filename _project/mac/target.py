# # import socket

# # # Set up a server socket
# # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # server_socket.bind(('localhost', 12345))
# # server_socket.listen(1)

# # # Accept incoming connections
# # print("Waiting for connection...")
# # client_socket, client_address = server_socket.accept()
# # print("Connected by", client_address)

# # # Receive commands and execute them
# # while True:
# #     command = client_socket.recv(1024).decode()
# #     if not command:
# #         break
# #     print("Received command:", command)
# #     # Execute the command in the terminal

# # # Close the sockets
# # client_socket.close()
# # server_socket.close()


# import socket
# import threading

# # Set up the server socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('localhost', 12345))

# # Flag to indicate if the server is running
# running = False

# # Function to handle incoming client connections
# def handle_client(client_socket, client_address):
#     print("Connected by", client_address)
#     while running:
#         # Receive command from client
#         command = client_socket.recv(1024).decode()
#         if not command:
#             break
#         print("Received command:", command)
#         # Execute the command in the terminal
#         # Replace with your command execution logic

#     # Close the client socket
#     client_socket.close()

# # Function to start the server
# def start_server():
#     global running
#     running = True
#     server_socket.listen(1)
#     print("Server started. Waiting for connections...")
#     while running:
#         client_socket, client_address = server_socket.accept()
#         client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
#         client_thread.start()

# # Function to stop the server
# def stop_server():
#     global running
#     running = False
#     # Close the server socket
#     server_socket.close()
#     print("Server stopped.")

# # Start the server (in a separate thread)
# start_thread = threading.Thread(target=start_server)
# start_thread.start()




import socket
import threading
import subprocess

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))

# Flag to indicate if the server is running
running = False

# Function to handle incoming client connections
def handle_client(client_socket, client_address):
    print("Connected by", client_address)
    try:
        while running:
            # Receive command from client
            command = client_socket.recv(1024).decode()
            if not command:
                break
            print("Received command:", command)
            # Execute the command in the terminal
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            if error:
                client_socket.sendall(error)
            else:
                client_socket.sendall(output)
    except ConnectionResetError:
        pass

    # Close the client socket
    client_socket.close()


# Function to start the server
def start_server():
    global running
    running = True
    server_socket.listen(1)
    print("Server started. Waiting for connections...")
    while running:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# Function to stop the server
def stop_server():
    global running
    running = False
    # Close the server socket
    server_socket.close()
    print("Server stopped.")

# Start the server (in a separate thread)
start_thread = threading.Thread(target=start_server)
start_thread.start()
