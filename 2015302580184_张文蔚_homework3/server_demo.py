import socket
words ={'Hello?':'Hi I am here',
'Cool, who are you':'you guess',
'what is your name?':'you guess',
"pardon?":'you guess',
'bye':'bye'}
HOST =''
PORT =50016
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind socket
s.bind((HOST, PORT))
#Start listen
s.listen(1)
print('Listening at port:',PORT)
connect, addr = s.accept()
print('connected by', addr)
while True:
    data = connect.recv(1024)
    data = data.decode()
    if not data:
        break
    print('Received message:', data)
    connect.sendall(words.get(data,'Nothing').encode())
connect.close()