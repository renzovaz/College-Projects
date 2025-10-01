

class Veiculo:
    def __init__(self, marca, ano):
        self._marca = marca
        self._ano = ano

    
    def get_marca(self):
        return self._marca

    def get_ano(self):
        return self._ano


    def set_marca(self, nova_marca):
        if len(nova_marca.strip()) < 2:
            print("Marca inválida. Digite pelo menos 2 caracteres.")
        else:
            self._marca = nova_marca

    def set_ano(self, novo_ano):
        if novo_ano < 1886:  
            print("Ano inválido. O veículo deve ser de 1886 em diante.")
        else:
            self._ano = novo_ano

   
    def exibir_informacoes(self):
        return f"Veículo: {self._marca} - Ano: {self._ano}"



class Carro(Veiculo):
    def __init__(self, marca, ano, modelo, portas, cor):
        super().__init__(marca, ano)  
        self._modelo = modelo
        self._portas = portas
        self._cor = cor

    
    def get_modelo(self):
        return self._modelo

    def get_portas(self):
        return self._portas

    def get_cor(self):
        return self._cor

  
    def set_modelo(self, novo_modelo):
        if len(novo_modelo.strip()) < 2:
            print("Modelo inválido. Digite pelo menos 2 caracteres.")
        else:
            self._modelo = novo_modelo

    def set_portas(self, novas_portas):
        if novas_portas not in [2, 4]:
            print("Número de portas inválido. Só é permitido 2 ou 4.")
        else:
            self._portas = novas_portas

    def set_cor(self, nova_cor):
        self._cor = nova_cor

  
    def exibir_informacoes(self):
        return f"Carro: {self._marca} {self._modelo}, Ano: {self._ano}, Portas: {self._portas}, Cor: {self._cor}"
