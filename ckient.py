import socket
HEADER_SIZE = 64
PORT = 3000
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "exit"
# run server.py to check the ip address and update as required
SERVER_IP_ADDRESS = input("Enter Server Address: ")
REMOTE_ADDRESS = (SERVER_IP_ADDRESS, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(REMOTE_ADDRESS)
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER_SIZE - len(send_length))
    client.send(send_length)
    client.send(message)
send("Hello!")
send("Type 'exit' to close connection")
loop = True
while loop:
    mesg=input("Enter Message")
    if mesg == "exit":
        loop = False
        send("exit")