ct=0
soma=0
print("digite [0] para sair")
while True:
    nota=float(input("digite a nota:"))
    if nota==0:
        break
    if nota%2==0:
        ct=ct+1
        soma= soma+nota
media=soma/ct
print("quantidade de numeros pares:{}".format(ct))
print("a soma de todos os numeros pares é:{}".format(soma))
print("media dos pares é ={:.2f}".format(media))
