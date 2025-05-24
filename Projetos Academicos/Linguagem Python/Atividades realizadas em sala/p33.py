def calcula_dobro(d_valor):
    dobro = d_valor *2
    return dobro

def calcula_triplo(t_valor):
    triplo = t_valor*3
    return triplo

if __name__ == '__main__':
    valor2 = int(input("Valor inteiro:"))
    print("O dobro do valor digitado é:", calcula_dobro(valor2))

    valor3 = int(input("Digite outro valor inteiro:"))
    print("O triplo do valor digitado é:", calcula_triplo(valor3))
