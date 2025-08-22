soma_pares = 0
quantidade_pares = 0
soma_impares = 0
quantidade_impares = 0
while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    if numero == 0:
        break
    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1
    else:
        soma_impares += numero
        quantidade_impares += 1
if quantidade_pares > 0:
    print(f"Média dos números pares: {soma_pares / quantidade_pares:.2f}")
else:
    print("Nenhum número par foi digitado.")

if quantidade_impares > 0:
    print(f"Média dos números ímpares: {soma_impares / quantidade_impares:.2f}")
else:
    print("Nenhum número ímpar foi digitado.")