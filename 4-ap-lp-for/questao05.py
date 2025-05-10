print('ordem decrescente dos números naturais.')
n1=int(input('digite um valor inicial:'))
ct=0
for i in range (n1,-1,-1):
    print(i)
    ct+=1
print('a sequencia possui {} valores.'.format(ct))
print('o progama encerrou.')