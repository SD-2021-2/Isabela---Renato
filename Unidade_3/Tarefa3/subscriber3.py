import zmq
import json


def main():

    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://172.31.93.32:2020")
    subscriber.setsockopt(zmq.SUBSCRIBE, b"aluno")

    sub2 = context.socket(zmq.SUB)
    sub2.connect("tcp://172.31.94.28:2021")
    sub2.setsockopt(zmq.SUBSCRIBE, b"aluno")

    poller = zmq.Poller()
    poller.register(subscriber, zmq.POLLIN)
    poller.register(sub2, zmq.POLLIN)

    while True:

        try:
            socks = dict(poller.poll())
        except KeyboardInterrupt:
            exit()

        if subscriber in socks:
            [address, contents] = subscriber.recv_multipart()
            x = json.loads(contents)
            n1 = x["n1"]
            n2 = x["n2"]
            n3 = x["n3"]
            M = (n1+n2)/2
            if ( M >= 7):
                 resultado = "Aprovado"
            else :
                 resultado = "Reprovado"
            if ( M >=3 and M <= 7):
                if ((M+n3)/2 >= 5):
                    resultado = "Aprovado"
                else :
                    resultado = "Reprovado"
            print(resultado)

        if sub2 in socks:
            [address2, contents2] = sub2.recv_multipart()
            y = json.loads(contents2)
            n11 = y["N1"]
            n22 = y["N2"]
            n33 = y["N3"]
            MM = (n11+n22)/2
            if ( MM >= 7):
                 resultado = "Aprovado"
            if ( MM >=3 and MM <= 7):
                if ((MM+n33)/2 >= 5):
                    resultado2 = "Aprovado"
                else :
                    resultado2 = "Reprovado"
            print(resultado2)
    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
