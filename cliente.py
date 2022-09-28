import socket
HOST = 'localhost'
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dados = (HOST, PORT)
tcp.connect(dados)

msg = ''
while (msg != 'break'):
    msg = input()
    tcp.sendall(str.encode(msg))
    reflect = tcp.recv(1024)
    print(reflect.decode(), 'recebido do servidor')

print('encerrando conexão')
tcp.close()