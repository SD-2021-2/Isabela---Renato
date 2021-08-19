import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('LocalHost', 2020))
print("N1: ")
n1 = input()
print("N2: ")
n2 = input()
print("N3: ")
n3 = input()
json1 = {
    "n1": n1,
    "n2": n2,
    "n3": n3,
}
document = json.dumps(json1)
s.sendall((document+"\n").encode())
print("mensagem enviada")
#resposta = s.recv(1024)
#print(resposta)

