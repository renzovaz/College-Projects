class VeiculoEletrico:
    def __init__(self, modelo: str, autonomia: float, ano: int, preco: float):
        self.modelo = modelo          
        self.autonomia = autonomia    
        self.ano = ano                
        self.preco = preco            

    
    def get_modelo(self):
        return self.modelo

    def get_autonomia(self):
        return self.autonomia

    def get_ano(self):
        return self.ano

    def get_preco(self):
        return self.preco

    
    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_autonomia(self, autonomia):
        self.autonomia = autonomia

    def set_ano(self, ano):
        self.ano = ano

    def set_preco(self, preco):
        self.preco = preco

    
    def mostra_dados1(self):
        print(f"Modelo: {self.modelo}")
        print(f"Autonomia: {self.autonomia} km")
        print(f"Ano: {self.ano}")
        print(f"Preço: R$ {self.preco:.2f}")

    def mostra_dados2(self):
        print(f"Modelo: {self.get_modelo()}")
        print(f"Autonomia: {self.get_autonomia()} km")
        print(f"Ano: {self.get_ano()}")
        print(f"Preço: R$ {self.get_preco():.2f}")

    
    def retorna_dados(self):
        return {
            "modelo": self.modelo,
            "autonomia": self.autonomia,
            "ano": self.ano,
            "preco": self.preco
        }

    
    def aumentar_preco(self, valor_aumento: float):
        self.preco += valor_aumento
        print(f"Preço do {self.modelo} atualizado para R$ {self.preco:.2f}")

    
    def verifica_viagem(self, distancia: float):
        if distancia <= self.autonomia:
            print(f"O {self.modelo} consegue realizar a viagem de {distancia} km.")
        else:
            print(f"O {self.modelo} NÃO consegue realizar a viagem de {distancia} km. Autonomia insuficiente.")



def main():
    veiculo1 = VeiculoEletrico("Tesla Model 3", 500.0, 2023, 250000.0)
    veiculo2 = VeiculoEletrico("Nissan Leaf", 300.0, 2022, 120000.0)
    veiculo3 = VeiculoEletrico("Chevrolet Bolt", 400.0, 2021, 150000.0)

    
    print("\n===== MOSTRANDO DADOS 1 =====")
    veiculo1.mostra_dados1()
    veiculo2.mostra_dados1()
    veiculo3.mostra_dados1()

    
    print("\n===== MOSTRANDO DADOS 2 =====")
    veiculo1.mostra_dados2()
    veiculo2.mostra_dados2()
    veiculo3.mostra_dados2()

    
    print("\n===== RETORNANDO DADOS =====")
    print(veiculo1.retorna_dados())
    print(veiculo2.retorna_dados())
    print(veiculo3.retorna_dados())

    
    valor_aumento = float(input("\nDigite o valor para aumentar o preço dos veículos: R$ "))
    veiculo1.aumentar_preco(valor_aumento)
    veiculo2.aumentar_preco(valor_aumento)
    veiculo3.aumentar_preco(valor_aumento)

    
    print("\n===== VERIFICANDO AUTONOMIA PARA VIAGEM =====")
    veiculo1.verifica_viagem(450)
    veiculo2.verifica_viagem(350)
    veiculo3.verifica_viagem(380)

if __name__ == "__main__":
    main()
