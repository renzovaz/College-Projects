
from classes import Veiculo, Carro


if __name__ == "__main__":
    print("=== TESTANDO SUPERCLASSE VEICULO ===")
    v1 = Veiculo("Toyota", 2020)
    v2 = Veiculo("Ford", 2015)

    
    print(v1.exibir_informacoes())
    print(v2.exibir_informacoes())

    v1.set_marca("T")
    v1.set_ano(1800)
    v1.set_marca("Honda")
    v1.set_ano(2022)
    print(v1.get_marca(), v1.get_ano())

    print("\n=== TESTANDO SUBCLASSE CARRO ===")
    c1 = Carro("Fiat", 2019, "Argo", 4, "Branco")
    c2 = Carro("Chevrolet", 2021, "Onix", 2, "Preto")

    print(c1.exibir_informacoes())
    print(c2.exibir_informacoes())

    c1.set_modelo("A")
    c1.set_portas(3)
    c1.set_modelo("Cronos")
    c1.set_portas(4)
    c1.set_cor("Vermelho")
    print(c1.get_modelo(), c1.get_portas(), c1.get_cor())

    print("\n=== TESTANDO HERANÇA (Método herdado) ===")
    print(v1.exibir_informacoes())
    print(c1.exibir_informacoes())  

