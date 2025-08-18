
class Aluno(object):
    def __init__(self,nome,mensalidade,idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade
    def get_nome(self):
        return self.nome
    def get_mensalidade(self):
        return self.mensalidade
    def get_idade(self):
        return self.idade
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def set_mensalidade(self, novo_mensalidade):
        self.mensalidade = novo_mensalidade
    def set_idade(self, novo_idade):
        self.idade = novo_idade
    def mostra_dados(self):
        print('-Mostra dados: \nNome:', self.nome)
        print('Mensalidade:', self.mensalidade)
        print('Idade:', self.idade)

    # def aumento_mensalidade_valor(self, aumento):
    #     self.mensalidade += aumento


if __name__ == '__main__':
    n1 = Aluno('Kaio', 1100.00,21)
    print(n1)
    n2 = Aluno('Eric',1300.00,20)
    print(n2)
    print("-Aluno 1: \nNome:", n1.get_nome())
    print("-Aluno 1: \nMensalidade:", n1.get_mensalidade())
    print("-Aluno 1: \nIdade:", n1.get_idade())
    print("-Aluno 2: \nNome:", n2.get_nome())
    print("-Aluno 2: \nMensalidade:", n2.get_mensalidade())
    print("-Aluno 2: \nIdade:", n2.get_idade())

    n1.set_nome('Clodoaldo')
    # print("-Nome:", n1.get_nome())
    n2.set_nome('Garibalda')
    # print("-Nome", n2.get_nome())

    n1.set_mensalidade(2000)
    # print("-Mensalidade:", n1.get_mensalidade())
    n2.set_mensalidade(2135)
    # print("-Mensalidade", n2.get_mensalidade())

    n1.set_idade(18)
    # print("-idade:", n1.get_idade())
    n2.set_idade(19)
    # print("-idade", n2.get_idade())

    n1.mostra_dados()
    n2.mostra_dados()