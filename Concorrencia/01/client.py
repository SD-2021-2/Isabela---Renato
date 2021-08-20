import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('LocalHost', 2020))
print("Nome: ")
nome = input()
print("Cargo: ")
cargo = input()
print("Salario: ")
salario = input()
json1 = {
    "nome": nome,
    "cargo": cargo,
    "salario": salario,
}
document = json.dumps(json1)
s.sendall((document+"\n").encode())

resposta = s.recv(64)
print(resposta)
