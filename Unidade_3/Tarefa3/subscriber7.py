import zmq
import json


def main():

    context = zmq.Context()

    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://172.31.93.32:2020")
    subscriber.setsockopt(zmq.SUBSCRIBE, b"aposentadoria")

    sub2 = context.socket(zmq.SUB)
    sub2.connect("tcp://172.31.94.28:2021")
    sub2.setsockopt(zmq.SUBSCRIBE, b"aposentadoria")

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
            tempo = x["tempo"]
            if ( idade >= 60 and tempo >= 25):
                flag = "sim"
            elif ( idade >= 65):
                flag = "sim"
            elif ( tempo >= 30):
                flag = "sim"
            else:
                flag = "nao"

            if ( flag == "sim"):
                print("Pode se aposentar")
            else :
                print("Nao pode se aposentar")

        if sub2 in socks:
            [address2, contents2] = sub2.recv_multipart()
            y = json.loads(contents2)
            idade2 = y["idade"]
            tempo2 = y["tempo"]
            if ( idade2 >= 60 and tempo2 >= 25):
                flag2 = "sim"
            elif ( idade2 >= 65):
                flag2 = "sim"
            elif ( tempo2 >= 30):
                flag2 = "sim"
            else:
                flag2 = "nao"

            if ( flag2 == "sim"):
                print("Pode se aposentar")
            else :
                print("Nao pode se aposentar")

    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()
