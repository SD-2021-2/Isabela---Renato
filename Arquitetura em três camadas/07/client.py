import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('LocalHost', 2020))
print("Idade: ")
idade = input()
print("Tempo de servico: ")
tempo = input()
json1 = {
    "idade": idade,
    "tempo": tempo,
    }
document = json.dumps(json1)
s.sendall((document+"\n").encode())

resposta = s.recv(1024)
print(resposta)
