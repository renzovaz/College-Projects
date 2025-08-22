def main():
    print("Cálculo da Média da Turma")
    print("Digite as notas dos alunos (use -1 para encerrar).")

    notas = []  

    while True:
        nota = float(input("Digite a nota: "))
        if nota == -1:  
            break
        notas.append(nota)  

    if notas:  
        media = sum(notas) / len(notas)  
        print("\nNotas digitadas:", notas)
        print("Quantidade de alunos:", len(notas))
        print(f"Média da turma: {media:.2f}")
    else:
        print("Nenhuma nota foi informada.")

main()
