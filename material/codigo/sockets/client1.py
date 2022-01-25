import socket

# socket(type, protocol)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect((address, port))
client_socket.connect(('localhost', 555))

# send(message)
while True:
    message = input('Write a message: ')
    client_socket.send(message.encode())