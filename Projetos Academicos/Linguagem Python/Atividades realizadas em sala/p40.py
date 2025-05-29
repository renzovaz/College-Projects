l_naturais = []
print('digite [-1] para sair.')
while True:
    num = int(input('Digite um número para o progama ler:'))
    if num == -1:
        break
    elif num % 2 == 0:
        l_naturais.append(num)

if len(l_naturais) != 0:

    print(f'Lista na horizontal: {l_naturais}')
    print(f'Media da lista: { sum(l_naturais) / len(l_naturais) }')
    print('Lista na vertical:')
    for i in l_naturais:
        print(i)
else:
    print('Esse número é Ímpar !!!')