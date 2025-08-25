
class Veiculo(object):

    def __init__( self, modelo, ano, valor):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def get_modelo(self):
        return self.modelo
    def get_ano(self):
        return self.ano
    def get_valor(self):
        return self.valor
    def set_modelo(self,novo_modelo):
        self.modelo = novo_modelo
    def set_ano(self,novo_ano):
        self.ano = novo_ano
    def set_valor(self,novo_valor):
        self.valor = novo_valor
    def mostra_dados(self):
        print('-Mostra dados: \nModelo:', self.modelo)
        print('Ano:', self.ano)
        print('valor:', self.valor)
    def retornta_dados(self):
        v = f'Modelo: {self.modelo} Ano: {self.ano} Valor: {self.valor}'
        return v
    def aumenta_valor(self,aumento):
        self.valor = self.valor + aumento

if __name__ == '__main__':
    n1 = Veiculo ('SW4', 2024, 439.000)
    print('Veiculo 1:',n1)
    n2 = Veiculo ('hilux',2023, 319.000)
    print('Veiculo 2:',n2)

    print('Veiculo 1: \nModelo:', n1.get_modelo())
    print('Ano:', n1.get_ano())
    print('Valor:', n1.get_valor())
    print('\nVeiculo 2: \nModelo:', n2.get_modelo())
    print('Ano:', n2.get_ano())
    print('Valor:', n2.get_valor())

    n1.set_modelo('Fusca')
    # print('Veiculo 1: \nModelo:', n1.get_modelo())
    n1.set_ano(1969)
    # print('Veiculo 1: \nAno:', n1.get_ano())
    n1.set_valor(25.000)
    # print('Veiculo 1: \nValor:', n1.get_valor())

    n2.set_modelo('Corsa')
    # print('Veiculo 2: \nModelo:', n2.get_modelo())
    n2.set_ano(2002)
    # print('Veiculo 2: \nAno:', n2.get_ano())
    n2.set_valor(13.431)
    # print('Veiculo 2: \nValor:', n2.get_valor())

    n1.mostra_dados()
    n2.mostra_dados()

    print(n1.retornta_dados())
    print(n2.retornta_dados())

    x1 = float(input('Digite o valor do aumento do veiculo:'))
    n1.aumenta_valor(x1)
    print('O Valor do veiculo agora é:',n1.get_valor())
