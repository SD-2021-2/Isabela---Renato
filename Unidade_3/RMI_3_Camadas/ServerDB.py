import Pyro4

@Pyro4.expose
class Exercicio8(object):
    def resultado(self, arg1):
        arg2 = int(arg1)
        if ( arg2 >= 0 and arg2 <= 200):
            return 0

        if ( arg2 >= 201 and arg2 <= 400):
           return  arg2*0.2

        if ( arg2 >= 401 and arg2 <= 600):
           return arg2*0.3

        if ( arg2 >= 601):
           return arg2*0.4

serverDB = Pyro4.Daemon(host = "172.31.18.190", port = 2020)
ns = Pyro4.locateNS(host = "172.31.30.239", port = 2020)
uri = serverDB.register(Exercicio8)
print(uri)
ns.register("ex8", uri)

print("ServerDB Ready.")
serverDB.requestLoop()
