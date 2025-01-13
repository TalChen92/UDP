import socket

# Create and bind the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 12345))  # Listen on all interfaces, port 12345

print("UDP server is up and listening")

while True:
    # Wait for incoming data
    data, addr = server_socket.recvfrom(1024)
    
    # Decode and print the received data and sender's address
    print(f"Received message from {addr}: {data.decode()}")
    
