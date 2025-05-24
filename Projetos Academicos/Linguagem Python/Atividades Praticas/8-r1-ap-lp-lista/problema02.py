notas = []

print("Digite as notas dos alunos (use -1 para encerrar):")

while True:
    nota = float(input("Nota: "))
    if nota == -1:
        break
    notas.append(nota)

if notas:
    media = sum(notas) / len(notas)
    print(f"\nQuantidade de alunos: {len(notas)}")
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")
