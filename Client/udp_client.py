import socket
#socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 12345)

client_socket.sendto(b"Hello, Server!", server_address)
client_socket.sendto(b"Another message", server_address)

if __name__ == "__main__":
    print("hello")
    print("add")