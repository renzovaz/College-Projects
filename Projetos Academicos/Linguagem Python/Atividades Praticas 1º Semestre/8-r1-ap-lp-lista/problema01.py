numeros = []

print("Digite números (digite -1 para sair):")

while True:
    entrada = int(input("Número: "))
    if entrada == -1:
        break
    numeros.append(entrada)  

print(f"Quantidade de números digitados: {len(numeros)}")