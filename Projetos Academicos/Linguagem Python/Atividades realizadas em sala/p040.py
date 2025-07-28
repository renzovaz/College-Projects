lista = []
print('digite [-1] para sair.')
while True:
    vlr = int(input('Digite um valor para o progama ler:'))
    if vlr == -1:
        break
    else:
        lista.append(vlr)

# print(f'o maior valor da lista: {max(lista)}')
# print(f'o menor valor da lista: {min(lista)}')

lista.sort()
print(f'O maior valor da lista {lista[-1]}')


lista.sort()
lista.reverse
print(f'O menor valor da lista {lista[0]}')


print(f'Lista na horizontal: {lista}')
print('Lista na vertical:')
for i in lista:
    print(i, '// posição -->', lista.index(i))
    