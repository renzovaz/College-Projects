def maximo(a,b):
    if a > b:
        return a
    else:
        return b

def minimo(a,b):
    if a < b:
        return a
    else:
        return b
if __name__ == '__main__':
    v1=int(input("digite um numero: "))
    v2=int(input("digite outro numero: "))
    print(f"Entrada: {v1} e {v2} Saida: Maior valor: {maximo(v1,v2)}\n")
    v3=int(input("digite um numero: "))
    v4=int(input("digite outro numero: "))
    print(f"Entrada: {v1} e {v2} Saida: Maior valor: {maximo(v3,v4)}\n")
    v5=int(input("digite um numero: "))
    v6=int(input("digite outro numero: "))
    print(f"Entrada: {v1} e {v2} Saida: Menor valor: {minimo(v5,v6)}\n")
