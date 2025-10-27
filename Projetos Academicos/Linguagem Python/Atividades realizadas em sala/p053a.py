class Conta:

    def __init__ (self,nome,saldo):
        self.nome = nome
        self.saldo = saldo

    def get_nome(self):
        return self.nome
    def get_saldo(self):
        return self.saldo

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def mostra_dados(self):
        print('-Mostra dados: \n -Nome:', self.nome)
        print(' -Saldo:', self.saldo)

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Valor do depósito deve ser positivo.')

    def saque(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
            else:
                print('Saldo insuficiente para o saque.')
        else:
            print('Valor do saque deve ser positivo.')


class PessoaFisica(Conta):
    def __init__(self,nome,saldo,genero='Masculino'):
        super().__init__(nome,saldo)
        self.genero = genero

    def get_genero(self):
        return self.genero

    def set_genero(self, novo_valor):
        self.genero = novo_valor

    def mostra_dados(self):
        print('-Mostra dados: \n -Nome:', self.nome)
        print(' -Saldo:', self.saldo)
        print(' -Gênero:', self.genero)




class PessoaJuridica(Conta):
    def __init__(self,nome,saldo,modalidade="MEI"):
        super().__init__(nome,saldo)
        self.modalidade = modalidade

    def get_modalidade(self):
        return self.modalidade

    def set_modalidade(self,novo_valor):
        self.modalidade = novo_valor

    def mostra_dados(self):
        print('-Mostra dados: \n -Nome:', self.nome)
        print(' -Saldo:', self.saldo)
        print(' -Modalidade:', self.modalidade)



