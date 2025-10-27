from p053a import Conta,PessoaFisica,PessoaJuridica

if __name__ == '__main__':
    c1 = Conta("Alice",150000.00)
    c1.mostra_dados()

    cpf1 = PessoaFisica ("Eric",800000.00)
    cpf1.mostra_dados()

    cpf2 = PessoaFisica ("Eduarda",10000.00, "Feminino")
    cpf2.mostra_dados()

    c1.deposito(5000)
    c1.mostra_dados()

    pj1 = PessoaJuridica ("Café ABC", 60000.00, "SA")
    pj1.mostra_dados()


    pj2 = PessoaJuridica ("Padaria", 35000.0)
    pj2.mostra_dados()
