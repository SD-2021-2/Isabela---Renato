import Pyro4

arg1 = input("Saldo Medio : ").strip()

Resp = Pyro4.Proxy("PYRO:obj_38b64c3cfa064d34a38bbaafe149935c@172.31.30.239:2020")   

print(" Saldo Medio : " , arg1 , '\n' ,"Valor de Credito : " , Resp.resposta(arg1))
