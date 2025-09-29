class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def get_nome(self):
        return self.nome
    def get_salario(self):
        return self.salario
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def set_salario(self, novo_salario):
        self.salario = novo_salario
    def mostra_dados(self):
        print('-Mostra dados: \nNome:', self.nome)
        print('-Salário:', self.salario)
        print("-Valor bonificação:", self.metodo_bonificacao())
    def metodo_bonificacao(self):
        aumento10 = self.salario * 0.10
        return aumento10

class Gerente(Funcionario):
    def __init__(self, nome, salario, qtd_funcionario):
        super().__init__(nome, salario)
        self.qtd_funcionario = qtd_funcionario
    def get_qtd_funcionario(self):
        return self.qtd_funcionario
    def set_qtd_funcionario(self, novo_qtd):
        self.qtd_funcionario = novo_qtd  
    def mostra_dados(self):
        print('-Mostra dados: \nNome:', self.nome)
        print('-Salário:', self.salario)
        print('-Quantidade Funcionario:', self.qtd_funcionario)
        print("-Valor bonificação:", self.metodo_bonificacao()) 
    
