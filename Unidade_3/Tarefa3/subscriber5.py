import zmq
import json


def main():

    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://172.31.93.32:2020")
    subscriber.setsockopt(zmq.SUBSCRIBE, b"esporte")

    sub2 = context.socket(zmq.SUB)
    sub2.connect("tcp://172.31.94.28:2021")
    sub2.setsockopt(zmq.SUBSCRIBE, b"esporte")

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
            idade = x["idade"]
            if ( idade >= 18 ):
                categoria = "adulto"
            elif ( idade >=14 ):
                categoria = "juvenil B"
            elif ( idade >=11 ):
                categoria = "juvenil A"
            elif ( idade >=8 ):
                categoria = "infantil B"
            else:
                categoria = "infantil A"

            print("Categoria : ",categoria)


        if sub2 in socks:
            [address2, contents2] = sub2.recv_multipart()
            y = json.loads(contents2)
            idade2 = y["idade"]
            if ( idade2 >= 18 ):
                categoria2 = "adulto"
            elif ( idade2 >=14 ):
                categoria2 = "juvenil B"
            elif ( idade2 >=11 ):
                categoria2 = "juvenil A"
            elif ( idade2 >=8 ):
                categoria2 = "infantil B"
            else:
                categoria2 = "infantil A"

            print("Categoria : ",categoria2)

    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
