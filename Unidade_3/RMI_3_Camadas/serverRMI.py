import Pyro4

@Pyro4.expose
class ObjetoIntermediario(object):
    def resposta(self, arg1):

        aux = Pyro4.Proxy("PYRONAME:ex8")
        result = aux.resultado(arg1)
        return result

Server = Pyro4.Daemon(host = "172.31.25.134", port = 2020)
ns = Pyro4.locateNS(host = "172.31.30.239", port = 2020)
uri = Server.register(ObjetoIntermediario)
print(uri)
ns.register("OI", uri)

print("Servant Server Ready.")
Server.requestLoop()
