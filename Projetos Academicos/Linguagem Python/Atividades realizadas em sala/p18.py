n=int(input("quantos numeros voce quer que eu conte ? "))
c=0
for numeros in range(0,11):
    if numeros == n:
        print(numeros, end=".")
    else:
        print(numeros, end=",")
    c+=1
print(f"\nquantidade de numeros que eu contei: {c}")
