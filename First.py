#sum of two numbers
a=1
b=3
print(a+b) #o/p = 4
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 5000))
server.listen(1)

print("Server is waiting for connection...")

conn, address = server.accept()
print("Connected with:", address)

while True:
    message = conn.recv(1024).decode()

    if not message or message.lower() == "bye":
        break

    print("Client:", message)

    reply = input("Server: ")
    conn.send(reply.encode())

conn.close()
server.close() # client and server record 
