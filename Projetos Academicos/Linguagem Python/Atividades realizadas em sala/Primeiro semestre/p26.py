ct=soma=maior=menor=aprovado=0
alunos=int(input("quantos alunos tem na turma: "))
for i in range(1,alunos+1,1):
    print(f"{i}º nota")
    nota=float(input("digite a nota: "))
    ct+=1
    soma+=nota
    if nota > maior:
        maior=nota
    if i == 1 :
        menor= nota
    elif menor > nota:
        menor= nota
    if nota>= 5:
        aprovado+=1

print(f"\na quantidade de alunos foi:{ct}")
print(f"\na soma de todas as notas foi:{soma}")
print(f"\na media da turma foi: { soma/ct:.2f}")
print(f"\na maior nota da turma foi: {maior}")
print(f"\na menor nota da turma foi: {menor}")
print(f"\na quantidade de alunos aprovados foi de:{aprovado}")
