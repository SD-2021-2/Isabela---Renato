import Pyro4

@Pyro4.expose
class Exercicio8(object):
    def resposta(self, arg1):
        arg2 = int(arg1)
        if ( arg2 >= 0 and arg2 <= 200):
            return 0

        if ( arg2 >= 201 and arg2 <= 400):
           return  arg2*0.2

        if ( arg2 >= 401 and arg2 <= 600):
           return arg2*0.3

        if ( arg2 >= 601):
           return arg2*0.4

daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(Exercicio8)      # register the greeting maker as a Pyro object
ns.register("ex8", uri)  # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls
