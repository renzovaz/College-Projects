cont=soma=0
inic=int(input("de onde voce quer que eu comece a contar: "))
finl=int(input("onde voce quer que eu pare "))
for c in range(inic,finl+1):
    print(c, end=" ")
    cont+=1
    soma+=c
print(f"a quantidade de numeros foi:{cont}")
print(f"a soma dos numeros é: {soma}")
