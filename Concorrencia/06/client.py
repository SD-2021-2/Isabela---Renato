import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('LocalHost', 2020))
print("Nome: ")
nome = input()
print("Nivel: ")
nivel = input()
print("Salario bruto: ")
salario = input()
print("Numero de dependentes: ")
numero = input()

json1 = {
    "nome": nome,
    "nivel": nivel,
    "salario": salario,
    "numero": numero,
}
document = json.dumps(json1)
s.sendall((document+"\n").encode())
print("mensagem enviada")
#resposta = s.recv(1024)
#print(resposta)
