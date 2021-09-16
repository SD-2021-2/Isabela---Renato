from xmlrpc.server import SimpleXMLRPCServer

def e5(num1):
    result = int(num1)
    if(result >=5 and result <=7):
        return "infantil A"
    if(result >=8 and result <=10):
        return "infantil B"
    if(result >=11 and result <=13):
        return "juvenil A"
    if(result >=14 and result <=17):
        return "juvenil B"
    if(result >=18):
        return "adulto"


server = SimpleXMLRPCServer(("172.31.30.239",2020))
server.register_function(e5,"e5")
server.serve_forever()
