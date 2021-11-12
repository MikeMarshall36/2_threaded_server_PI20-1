import socket
from time import sleep
user_name = input('Введите имя пользователя: ')+': '
sock = socket.socket()
sock.setblocking(1)
sock.connect(('127.0.0.1', 9091))

msg = user_name + input(f'{user_name}')
while len(msg) != 0:
    sock.send(msg.encode())
    data = sock.recv(1024)
    exit_check = msg.lower()
    if exit_check == 'exit':
        sock.close()
        break
    print(data.decode())
    msg = user_name + input(f'{user_name}')