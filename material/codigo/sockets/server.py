from http import server
import socket

# socket(type, protocol)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Launch the server bind(address, port)
server_socket.bind(('localhost', 555))

# Listen the request of the clients listen(max_clients)
server_socket.listen(2)

while True:
    # Store the connection socket and its address
    conn, address = server_socket.accept()
    
    # recv(size_of_trama)
    buffer = conn.recv(64) 

    if len(buffer):
        print(f"\nNew message:\n{buffer}")

# Close the port
server_socket.close()