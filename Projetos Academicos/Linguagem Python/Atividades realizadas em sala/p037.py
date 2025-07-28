lista = []
print('digite [0] para sair.')
while True:
    recebido = int(input('digite um valor:'))
    if recebido == 0:
        break
    else:
        lista.append(recebido)
print(f'Lista na horizontal: {lista}')

print(f'Lista na vertical:')
for i in lista:
    print(i)
print(f'quantidade de elementos na lista: {len(lista)}')
print(f'soma dos elementos da lista: {sum(lista)}')
print(f'maior valor da lista: {max(lista)}')
print(f'menor valor da lista:= {min(lista)}')

n1=int(input('pesquise um valor na lista:'))

if n1 in lista:
    print(f'O valor exite na lista!')
    print(f'o valor se encontra na posição: {lista.index(n1)}')
else:
    print(f'o valor não existe na lista.')

# if lista.count(n1) != 0:
#
#     print(f'ele contem na lista')
# else:
#     print(f'esse valor nao contem na lista')

lista.insert(1, 33)
lista.sort()
print(f'Lista em ordem crescente: {lista}')

lista.sort()
lista.reverse()
print(f'Lista em ordem decrescente: {lista}')

calculo_media=sum(lista)/len(lista)
print(f'Média aritmética da Lista: {calculo_media:.3f}')
ct=0
for x in lista:
    if x>10:
        ct+=1
print(f'Quantidade de valores maiores que 10 na lista: {ct}')

percentual=(ct*100)/len(lista)
lista.remove(33)
print(lista)    