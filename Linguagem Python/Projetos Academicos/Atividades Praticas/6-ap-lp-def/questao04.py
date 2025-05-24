## Uma escola deseja automatizar o cálculo da nota final de um aluno em uma disciplina. A nota final será calculada somando três notas: uma prova, um trabalho e uma participação.

def calcular_nota_final(nota_prova, nota_trabalho, nota_participacao):
    return nota_prova + nota_trabalho + nota_participacao

if __name__ == "__main__":
    print("=== CÁLCULO DA NOTA FINAL DO ALUNO ===")

    nota_prova = float(input("Digite a nota da prova (0 a 10): "))
    nota_trabalho = float(input("Digite a nota do trabalho (0 a 10): "))
    nota_participacao = float(input("Digite a nota da participação (0 a 10): "))

    nota_final = calcular_nota_final(nota_prova, nota_trabalho, nota_participacao)

    print("\n A nota final do aluno é:", nota_final)
