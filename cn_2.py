import socket

HOST = ''        # Listen on all interfaces
PORT = 8080

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow reuse of address
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind and listen
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print('Server listening on {}:{}'.format(HOST, PORT))

# Accept client connection
client_socket, client_address = server_socket.accept()
print('Accepted connection from {}:{}'.format(client_address[0], client_address[1]))

# Communication loop
while True:
    data = client_socket.recv(1024).decode()
    
    if not data:
        break

    print('Received message: {}'.format(data))
    
    response = input('Enter a response: ')
    client_socket.sendall(response.encode())

print('Closing connection')
client_socket.close()
server_socket.close()
