import socket
HOST ='127.0.0.1' #server IP
PORT =50016 # port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    c = input('Input the content you want to send:')
    s.sendall(c.encode())
    data = s.recv(1024)
    data = data.decode()
    print('Received:', data)
    if c.lower()=='bye':
        break
s.close()