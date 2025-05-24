a=float(input("digite um valor para A em uma equação do 1ºgrau:"))
b=float(input("digite um valor para B em uma equação do 1ºgrau:"))
if a==0:
    print("nao posso dividir por 0")
else:
    x= -b/a
    print("o valor de x é:{}".format(x))
