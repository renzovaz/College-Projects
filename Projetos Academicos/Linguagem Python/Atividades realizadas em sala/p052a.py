


class Veiculo:
    def __init__ (self,nome,valor,km ):
        self.nome = nome
        self.valor = valor
        self.km = km

    def get_nome(self):
        return self.nome
    def get_valor(self):
        return self.valor
    def get_km(self):
        return self.km

    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def set_valor(self, novo_valor):
        self.valor = novo_valor
    def set_km(self, novo_km):
        self.valor = novo_km


    def mostra_dados(self):
        print('-Mostra dados: \n -Nome:', self.nome)
        print(' -Valor:', self.valor)
        print(' -Km:', self.km)

    def atualiza_valor(self, valor_aumento):
        self.valor = self.valor + valor_aumento


class Carro(Veiculo):
    def __init__(self, nome,valor,km,qtd_portas=4):
        super().__init__(nome, valor, km)
        self.qtd_portas = qtd_portas

    def get_qtd_portas(self):
        return self.qtd_portas

    def set_qtd_portas(self, nova_qtd):
        self.qtd_portas = nova_qtd

    def mostra_dados(self):
        print('-Mostra dados: \n -Nome:', self.nome)
        print(' -Valor:', self.valor)
        print(' -Km:', self.km)
        print(' -Quantidade de portas:', self.qtd_portas)

class Moto(Veiculo):
    def __init__(self, nome,valor,km,cc):
        super().__init__(nome,valor,km)
        self.cc = cc

    def get_cc(self):
        return self.cc

    def set_cc(self, nova_cc):
        self.cc = nova_cc

    def mostra_dados(self):
        print('-Mostra dados: \n -Nome:', self.nome)
        print(' -Valor:', self.valor)
        print(' -Km:', self.km)
        print(' -Celindrada:', self.cc)



