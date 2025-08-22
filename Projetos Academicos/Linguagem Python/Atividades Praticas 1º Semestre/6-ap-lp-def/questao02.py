def calcula_idade(ano_nascimento):
    ano_atual = 2025  
    idade = ano_atual - ano_nascimento
    return idade

if __name__ == "__main__":
    ano = int(input("Digite o ano de nascimento: "))
    idade = calcula_idade(ano)
    print("Sua idade é:", idade)