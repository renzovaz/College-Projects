cont=soma=0
inic=int(input("de onde voce quer que eu comece a contar: "))
finl=int(input("onde voce quer que eu pare "))
if inic < finl:
    print(f"valores na ordem crescente")
    for c in range(inic,finl+1,1):
        if c== finl:
             print(c, end=".")

        else:
            print(c, end=",")
        cont+=1
        soma+=c
else:
    print(f"valores na ordem decrescente")
    for c in range(inic,finl-1,-1):
        if c == finl:
            print(c, end=".")

        else:
            print(c, end=",")
        cont += 1
        soma += c

print(f"\na quantidade de numeros foi: {cont}")
print(f"a soma dos numeros é: {soma}")
