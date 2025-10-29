class Pessoa:

    def __init__(self,nome,qtd_dependentes):
        self.nome = nome
        self.qtd_dependentes = qtd_dependentes

    def get_nome(self):
        return self.nome

    def get_qtd_dependentes(self):
        return self.qtd_dependentes

    def set_nome(self, novo_valor):
        self.nome = novo_valor

    def set_qtd_dependentes(self, novo_valor):
        if novo_valor >=0:
            self.qtd_dependentes = novo_valor
        else:
            print('Erro: valor não pode ser negativo.')

    def mostra_dados(self):
        print('-Mostra dados: \n -Nome:', self.nome)
        print(' -Depentendes:', self.qtd_dependentes)

    def bonus(self):
        bonus = self.qtd_dependentes * 300
        return bonus






class Professor(Pessoa):
    def __init__(self,nome,qtd_dependentes,qtd_turma=3,valor_turma=1000):
        super().__init__(nome,qtd_dependentes)
        self.qtd_turma = qtd_turma
        self.valor_turma = valor_turma

    def get_qtd_turma(self):
        return self.qtd_turma

    def get_valor_turma(self):
        return self.valor_turma

    def set_qtd_turma(self, novo_valor):
        self.qtd_turma = novo_valor

    def set_valor_turma(self, novo_valor):
        self.valor_turma = novo_valor

    def mostra_dados(self):
        print('-Mostra dados: \n -Nome:', self.nome)
        print(' -Depentendes:', self.qtd_dependentes)
        print(' -Quantidade de Turmas:', self.qtd_turma)
        print(' -Valor da Mensalidade:', self.valor_turma)

    def rendimento(self):
        rendimento = self.qtd_turma * self.valor_turma
        return rendimento

    def salario_total(self):
        salario_final = self.rendimento() + self.bonus()
        return salario_final

class Funcionario(Pessoa):
    def __init__(self,nome,qtd_dependentes, qtd_turma, valor_turma, salario_fixo= 1512):
        super().__init__(nome,qtd_dependentes)
        self.salario_fixo = salario_fixo

    def get_salario_fixo(self):
        return self.salario_fixo

    def set_salario_fixo(self, novo_valor):
        if novo_valor >= 0:
            self.salario_fixo = novo_valor
        else:
            print('Erro: valor nao pode ser negativo.')

    def mostra_dados(self):
        print('-Mostra dados: \n -Nome:', self.nome)
        print(' -Depentendes:', self.qtd_dependentes)
        print(' -Salario Fixo:', self.salario_fixo)

    def salario_total(self):
        salario_final = self.salario_fixo + self.bonus()
        return salario_final


