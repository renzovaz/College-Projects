menor_valor=9999999999999999999999999999999999999999999999999999999
ct=0
soma=0
print("digite 0 para sair")
while True:
    valor = int(input("digite um numero:"))
    if valor==0:
        break
    else:
        soma= soma +valor
        ct+=1
    if valor<menor_valor:
        menor_valor=valor
print("o menor valor é:{}".format(menor_valor))
print("voce inseriu {} valores.".format(ct))
print("a soma de todos os valores inseridos é:{}".format(soma))
