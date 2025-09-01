class Pessoa:
    def __init__(self, nome,peso,altura,ano_nascimento):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.ano_nascimento = ano_nascimento

    def get_nome(self):
        return self.nome
    def get_peso(self):
        return self.peso
    def get_altura(self):
        return self.altura
    def get_ano_nascimento(self):
        return self.ano_nascimento

    def set_nome(self,novo_nome):
        self.nome = novo_nome
    def set_peso(self,novo_peso):
        self.peso = novo_peso
    def set_altura(self,novo_altura):
        self.altura = novo_altura
    def set_ano_nascimento(self,novo_ano):
        if novo_ano > 2025:
            print("-Ano de Nascimento: Erro ano inválido.")
        else:
            self.ano_nascimento = novo_ano

    def mostra_dados(self):
        print('-Mostra dados: \n-Nome:', self.nome)
        print('-peso:', self.peso)
        print('-Altura:', self.altura)
        print('-Ano de Nascimento:', self.ano_nascimento)
    def calcula_idade(self):
        print('-idade:',2025 - self.ano_nascimento)
    def calcula_IMC(self):
        calculo_IMC = self.peso / self.altura ** 2
        return calculo_IMC

if __name__ == '__main__':
    pessoa1 = Pessoa('Kaio', 95, 1.88, 2005)
    print('Meu melhor amigo:', pessoa1)
    pessoa2 = Pessoa('Eric', 64,1.84, 2006)
    print('Meu segundo melhor amigo:',pessoa2)


    print("-Pessoa 1: \n-Nome:", pessoa1.get_nome())
    print("-Peso:", pessoa1.get_peso())
    print("-Altura:", pessoa1.get_altura())
    print("-Ano de Nascimento:", pessoa1.get_ano_nascimento())
    pessoa1.calcula_idade()
    print('-IMC da pessoa 1:', pessoa1.calcula_IMC())

    print("-Pessoa 2: \n-Nome:", pessoa2.get_nome())
    print("-Peso:", pessoa2.get_peso())
    print("-Altura:", pessoa2.get_altura())
    print("-Ano de Nascimento:", pessoa2.get_ano_nascimento())
    pessoa2.calcula_idade()
    print('-IMC da pessoa 2:', pessoa2.calcula_IMC())

    pessoa1.set_nome('Renzo')
    pessoa2.set_nome('Cauan')

    pessoa1.set_peso(69)
    pessoa2.set_peso(65)

    pessoa1.set_altura(1.70)
    pessoa2.set_altura(1.78)

    pessoa1.set_ano_nascimento(2007)
    pessoa2.set_ano_nascimento(2008)

    pessoa1.mostra_dados()
    pessoa1.calcula_idade()
    print('-IMC da pessoa 1:', pessoa1.calcula_IMC())
    pessoa2.mostra_dados()
    pessoa2.calcula_idade()
    print('-IMC da pessoa 2:', pessoa2.calcula_IMC())
    # pessoa1.set_ano_nascimento(2005)
    # print("Ano Nascimento alterado:", pessoa1.get_ano_nascimento())
    # pessoa1.set_ano_nascimento(2025)
    # print("Ano Nascimento alterado:", pessoa1.get_ano_nascimento())


