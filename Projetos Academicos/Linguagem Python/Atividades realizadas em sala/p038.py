lista_notas = []
print('digite [-1] para sair')

while True:
    nota = int(input('Digite a nota do aluno para o progama ler:'))
    if nota == -1:
        break
    lista_notas.append(nota)

print(f'Lista {lista_notas}')
print(f'Soma das notas dos alunos: {sum(lista_notas)}')
media_notas = sum(lista_notas) / len(lista_notas)
print(f'Media das notas dos alunos: {media_notas}')
