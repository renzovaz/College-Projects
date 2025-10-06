from p052a import Veiculo, Carro, Moto

if __name__ == '__main__':
    veiculo1 = Veiculo("Golf",180000.00, 20000)
    veiculo2 = Veiculo("Creta",170000.00, 35)
    veiculo1.mostra_dados()
    veiculo2.mostra_dados()

    veiculo1.set_km(66000.00)
    veiculo1.set_valor(160000.00)
    veiculo1.mostra_dados()


    veiculo2.set_km(6000)
    veiculo2.set_valor(168000.00)
    veiculo2.mostra_dados()

    carro1 = Carro ("Strada",80000.00, 70000,3)
    carro2 = Carro ("Hilux",345000.00,22)

    carro1.mostra_dados()

    carro2.mostra_dados()

    moto1 = Moto ("Xj6", 45000.00, 22000, 600)
    moto2 = Moto ("CB1000", 58000.00,32000, 1000)

    moto1.mostra_dados()

    moto2.mostra_dados()
