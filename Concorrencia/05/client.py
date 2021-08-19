import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('LocalHost', 2020))
print("Idade: ")
idade = input()
json1 = {
    "idade": idade,
}
document = json.dumps(json1)
s.sendall((document+"\n").encode())
print("mensagem enviada")
#resposta = s.recv(1024)
#print(resposta)
