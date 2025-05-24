def converte(a,b):
    return (a*60)+b

def converte2(a,b):
    print(f"\nEntrada: horas: {a}, minutos: {b} Saida: {(a*60)+b} minutos\n")

if __name__ == '__main__':
    n1=int(input("horas: "))
    n2=int(input("minutos: "))
    print(f"\nEntrada: horas: {n1}, minutos: {n2} Saida: {converte(n1,n2)} minutos\n")

    n3=int(input("horas: "))
    n4=int(input("minutos: "))
    converte2(n3,n4)
