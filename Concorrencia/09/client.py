import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('LocalHost', 2020))
print("Numero da Carta: ")
numero = input()
print("Naipe(1,2,3,4): ")
naipe = input()
json1 = {
    "numero": numero,
    "naipe": naipe
}
document = json.dumps(json1)
s.sendall((document+"\n").encode())
print("mensagem enviada")
#resposta = s.recv(1024)
#print(resposta)
