import socket
HOST = 'localhost'
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dados = (HOST, PORT)
tcp.bind(dados)
tcp.listen(1)
print('aguardando conexão')
con, client = tcp.accept()
print('conectado por: ', client)

while True:
    msg = con.recv(1024)
    if (not msg): break
    print(msg.decode(), 'recebido de: ', client)
    reflect = input()
    con.sendall(str.encode(reflect))
    
print('fechando servidor')
con.close()
    