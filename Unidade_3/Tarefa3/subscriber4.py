import zmq
import json


def main():

    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://172.31.93.32:2020")
    subscriber.setsockopt(zmq.SUBSCRIBE, b"peso")

    sub2 = context.socket(zmq.SUB)
    sub2.connect("tcp://172.31.94.28:2021")
    sub2.setsockopt(zmq.SUBSCRIBE, b"peso")

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
            altura = x["altura"]
            sexo = x["sexo"]
            if ( sexo == "masculino"):
                peso = (72.7*altura)-58
            else:
                peso = (62.1*altura)-44.7

            print("Peso ideal : ",peso)


        if sub2 in socks:
            [address2, contents2] = sub2.recv_multipart()
            y = json.loads(contents2)
            altura2 = y["altura"]
            sexo2 = y["sexo"]
            if ( sexo2 == "masculino"):
                peso2 = (72.7*altura2)-58
            else:
                peso2 = (62.1*altura2)-44.7

            print("Peso ideal : ",peso2)

    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
