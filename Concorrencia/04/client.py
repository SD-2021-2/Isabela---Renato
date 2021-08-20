import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('LocalHost', 2020))
print("Altura: ")
altura = input()
print("Sexo: ")
sexo = input()
json1 = {
    "altura": altura,
    "sexo": sexo,
}
document = json.dumps(json1)
s.sendall((document+"\n").encode())

resposta = s.recv(1024)
print(resposta)
