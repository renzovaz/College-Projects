def soma(a,b):
    return a + b

def subtrai(a,b):
    return a - b

if __name__ == '__main__':
    v1=int(input("digite o primeiro valor: "))
    v2 = int(input("digite o segundo valor: "))
    print(f"\nTESTE 1: Entrada {v1} e {v2}     Saida: soma= {soma(v1,v2)} subtraçao= {subtrai(v1,v2)}")
