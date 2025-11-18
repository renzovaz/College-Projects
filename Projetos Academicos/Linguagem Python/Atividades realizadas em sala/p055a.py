from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    def __init__(self, cor):
        self.cor = cor

    def get_cor(self):
        return self.cor

    def set_cor(self, nova_cor):
        self.cor = nova_cor

    def mostra_dados(self):
        print('-Mostra dados:')
        print(' -Cor:', self.cor)

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Quadrado(FormaGeometrica):
    def __init__(self, cor, lado=2):
        super().__init__(cor)
        self.lado = lado

    def get_lado(self):
        return self.lado

    def set_lado(self, novo_lado):
        self.lado = novo_lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def mostra_dados(self):
        super().mostra_dados()
        print(' -Lado:', self.lado)


class Circulo(FormaGeometrica):
    def __init__(self, cor, raio=1):
        super().__init__(cor)
        self.raio = raio

    def get_raio(self):
        return self.raio

    def set_raio(self, novo_raio):
        self.raio = novo_raio

    def area(self):
        return 3.14 * (self.raio ** 2)

    def perimetro(self):
        return 2 * 3.14 * self.raio

    def mostra_dados(self):
        super().mostra_dados()
        print(' -Raio:', self.raio)



