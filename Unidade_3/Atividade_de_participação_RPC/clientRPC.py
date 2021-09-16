import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://172.31.30.239:2020/")
print("Idade do nadador : ")
num1 = input()

result = proxy.e5(num1)
print(f"Classificação é : {result}")
