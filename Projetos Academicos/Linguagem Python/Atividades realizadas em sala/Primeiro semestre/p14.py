ct=0
soma=0
print("digite [-1] para sair")
while True:
    numero=int(input("digite um numero:"))
    if numero==-1:
        break
    ct=ct+1
    soma= soma+numero
print("quantidade de numeros:{}".format(ct))
print("a soma de todos os numeros é:{}".format(soma))
