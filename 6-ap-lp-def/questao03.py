def somar_tres_valores(a, b, c):
    soma = a + b + c
    return soma

if __name__ == "__main__":
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    valor3 = int(input("Digite o terceiro valor: "))

    resultado = somar_tres_valores(valor1, valor2, valor3)
    print("A soma dos três valores é:", resultado)