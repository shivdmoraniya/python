import socket

HOST = 'localhost'
PORT = 8080

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((HOST, PORT))
print('Connected to {}:{}'.format(HOST, PORT))

# Communication loop
while True:
    message = input('Enter a message (or type "exit" to quit): ')
    
    if message.lower() == 'exit':
        break

    client_socket.sendall(message.encode())

    data = client_socket.recv(1024).decode()
    
    if not data:
        break

    print('Received response: {}'.format(data))

print('Closing connection')
client_socket.close()
