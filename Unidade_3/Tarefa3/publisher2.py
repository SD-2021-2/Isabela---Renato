import time
import zmq


def main():

    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://172.31.94.28:2021")

    while True:
        #Exercicio 1 :
        publisher.send_multipart([b"funcionario", b'{ "nome":"Gislaine", "cargo":"programador", "salario":1000}'])
        publisher.send_multipart([b"funcionario", b'{ "nome":"Victor", "cargo":"programador", "salario":1000}'])
        publisher.send_multipart([b"funcionario", b'{ "nome":"Kleber", "cargo":"programador", "salario":1100}'])
        #Exercicio 2 :
        publisher.send_multipart([b"maioridade", b'{ "nome":"Isabela", "sexo":"feminino", "idade":23}'])
        publisher.send_multipart([b"maioridade", b'{ "nome":"Heitor", "sexo":"masculino", "idade":24}'])
        #Exercicio 3 :
        publisher.send_multipart([b"aluno", b'{ "N1":4, "N2":3, "N3":1}'])
        publisher.send_multipart([b"aluno", b'{ "N1":6, "N2":1, "N3":4}'])
        publisher.send_multipart([b"aluno", b'{ "N1":7, "N2":5, "N3":8}'])
        #Exercicio 4 :
        publisher.send_multipart([b"peso", b'{ "altura":1.62, "sexo":"feminino"}'])
        publisher.send_multipart([b"peso", b'{ "altura":1.31, "sexo":"feminino"}'])
        publisher.send_multipart([b"peso", b'{ "altura":1.62, "sexo":"masculino"}'])
        #Exercicio 5 :
        publisher.send_multipart([b"esporte", b'{ "idade":14 }'])
        publisher.send_multipart([b"esporte", b'{ "idade":56 }'])
        #Exercicio 7 :
        publisher.send_multipart([b"aposentadoria", b'{ "idade":45, "tempo":30}'])
        publisher.send_multipart([b"aposentadoria", b'{ "idade":30, "tempo":10}'])
        #Exercicio 8:
        publisher.send_multipart([b"credito", b'{ "saldo":602}'])
        publisher.send_multipart([b"credito", b'{ "saldo":156}'])
        publisher.send_multipart([b"credito", b'{ "saldo":244}'])
        time.sleep(1)

    publisher.close()
    context.term()

if __name__ == "__main__":
    main()
