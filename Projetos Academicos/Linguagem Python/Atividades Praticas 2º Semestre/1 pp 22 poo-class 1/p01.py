def somar(a, b):
    resultado = a + b
    print(f"Resultado da soma: {resultado}")

def subtrair(a, b):
    resultado = a - b
    print(f"Resultado da subtração: {resultado}")

def multiplicar(a, b):
    resultado = a * b
    print(f"Resultado da multiplicação: {resultado}")

def dividir(a, b):
    if b != 0:
        resultado = a / b
        print(f"Resultado da divisão: {resultado}")
    else:
        print("Erro: divisão por zero não é permitida.")

def main():
    print("=== Calculadora ===")
    print("Operações disponíveis: +  -  x  /")
    
    operador = input("Digite a operação desejada (+, -, x, /): ")
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    if operador == "+":
        somar(valor1, valor2)
    elif operador == "-":
        subtrair(valor1, valor2)
    elif operador == "x" or operador == "*":
        multiplicar(valor1, valor2)
    elif operador == "/":
        dividir(valor1, valor2)
    else:
        print("Operador inválido.")


main()
