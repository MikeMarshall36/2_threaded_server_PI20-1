import socket
import threading

CreatedThread = True

sock = socket.socket()
sock.bind(('127.0.0.1', 9091))
sock.listen(1)

def Therad_Spammer():
    global CreatedThread
    client_sock, addr = sock.accept()
    print(f"Connected to: {addr}")
    CreatedThread = True
    while True:
        msg = client_sock.recv(1024)
        decoded_msg = msg.decode()
        print(decoded_msg)
        decoded_msg = decoded_msg.split()
        out_put = ''
        decoded_msg[0] = 'Echo: '
        for i in range(len(decoded_msg)):
            out_put += decoded_msg[i]
        client_sock.send(out_put.encode())
        exit_check = msg.lower()
        if exit_check == 'exit':
            sock.close()
            break

while True:
    if CreatedThread:
        threading.Thread(target=Therad_Spammer).start()
        CreatedThread = False
