print('sequência do dobro dos números naturais até dez na ordem crescente:')
ct=0
soma=0
media=0
for i in range (1,11):
    print(i,end=' => ')

    print(i*2)
    ct += 1
    soma += i*2
    media = soma / ct
print('o a média dos valores mostrados é:',media)
print('o progama encerrou.')