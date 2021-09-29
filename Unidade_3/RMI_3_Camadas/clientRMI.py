import Pyro4

arg1 = input("Saldo Medio : ").strip()

Resp = Pyro4.Proxy("PYRO:OI")

print(" Saldo Medio : " , arg1 , '\n' ,"Valor de Credito : " , Resp.resposta(arg1))
