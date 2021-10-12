import zmq
import json


def main():

    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://172.31.93.32:2020")
    subscriber.setsockopt(zmq.SUBSCRIBE, b"credito")

    sub2 = context.socket(zmq.SUB)
    sub2.connect("tcp://172.31.94.28:2021")
    sub2.setsockopt(zmq.SUBSCRIBE, b"credito")

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
            saldo = x["saldo"]

            if ( saldo >= 601):
                credito = saldo*0.4
            elif ( saldo >= 401):
                credito = saldo*0.3
            elif ( saldo >= 201):
                credito = saldo*0.2
            else:
                credito = 0
            print("Saldo : ",saldo,",","Percentual de Credito : ",credito)


        if sub2 in socks:
            [address2, contents2] = sub2.recv_multipart()
            y = json.loads(contents2)
            saldo2 = y["saldo"]

            if ( saldo2 >= 601):
                credito2 = saldo2*0.4
            elif ( saldo2 >= 401):
                credito2 = saldo2*0.3
            elif ( saldo2 >= 201):
                credito2 = saldo2*0.2
            else:
                credito2 = 0
            print("Saldo : ",saldo2,",","Percentual de Credito : ",credito2)

    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
