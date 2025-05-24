import random
um=dois=tres=quatro=cinco=seis=ct=0
for i in range(0,60):
    sort = random.randint(1, 6)
    print(sort, end=" ")
    ct+=1
    if 1 == sort:
        um+=1

    if 2 == sort:
        dois+=1

    if 3 == sort:
        tres+=1

    if 4 == sort:
        quatro+=1

    if 5 == sort:
        cinco+=1

    if 6 == sort:
        seis+=1
print(f"\no numero 1 apareceu: {um} vezes, e aporcentagem foi {um/ct*100:.2f}% ")
print(f"o numero 2 apareceu: {dois} vezes, e aporcentagem foi {dois/ct*100:.2f}%  ")
print(f"o numero 3 apareceu: {tres} vezes, e aporcentagem foi {tres/ct*100:.2f} % ")
print(f"o numero 4 apareceu: {quatro} vezes, e aporcentagem foi {quatro/ct*100:.2f}%  ")
print(f"o numero 5 apareceu: {cinco} vezes, e aporcentagem foi {cinco/ct*100:.2f}%  ")
print(f"o numero 6 apareceu: {seis} vezes, e aporcentagem foi {seis/ct*100:.2f}%")
