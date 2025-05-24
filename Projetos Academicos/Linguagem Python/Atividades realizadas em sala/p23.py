cont=soma=0
opcao=str(input("vocer que seja decrecente ou crescente: use[D ou C] ")).upper().strip()
inic=int(input("de onde voce quer que eu comece a contar: "))
finl=int(input("onde voce quer que eu pare "))
op_maisc= opcao[0]
if op_maisc == "C":

    for c in range(inic,finl+1,1):
        if c== finl:
            print(c, end=".")

        else:
            print(c, end=",")
        cont+=1
        soma+=c

if op_maisc == "D":

    for c in range(inic,finl-1,-1):
        if c== finl:
            print(c, end=".")

        else:
            print(c, end=",")
        cont+=1
        soma+=c
print(f"\na quantidade de numeros foi: {cont}")
print(f"a soma dos numeros é: {soma}")
