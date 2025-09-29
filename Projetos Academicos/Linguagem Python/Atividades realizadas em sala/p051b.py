from p051a import Funcionario,Gerente

if __name__ == '__main__':
    funcionario1 = Funcionario("renzo", 1445.00)
    funcionario2 = Funcionario("eric", 1980.00)
    gerente1 = Gerente("arlindo", 16000.00, 5)
    gerente2 = Gerente("Mozaniel", 30000.00, 2)

    print("\n-Funcionario 1: \n-Nome:", funcionario1.get_nome())
    print("-Salário:", funcionario1.get_salario())
    print("-Valor bonificação:", funcionario1.metodo_bonificacao())
    
    print("\n-Funcionario 2: \n-Nome:", funcionario2.get_nome())
    print("-Salário:", funcionario2.get_salario())
    print("-Valor bonificação:", funcionario2.metodo_bonificacao())

   


    funcionario1.set_nome('Kaio')
    funcionario2.set_nome('cauan')

    funcionario1.set_salario(2110.00)
    funcionario2.set_salario(4500.00)

    print("\n-Funcionario 1: \n-Nome:", gerente1.get_nome())
    print("-Salário:", gerente1.get_salario())
    print("-Quantidade de Funcionarios:", gerente1.get_qtd_funcionario())
    print("-Valor bonificação:", gerente2.metodo_bonificacao())
    
    print("\n-Funcionario 2: \n-Nome:", gerente2.get_nome())
    print("-Salário:", gerente2.get_salario())
    print("-Quantidade de Funcionarios:", gerente2.get_qtd_funcionario())
    print("-Valor bonificação:", gerente2.metodo_bonificacao())

    gerente1.set_nome('Divanete')
    gerente2.set_nome('Daniele')

    gerente1.set_salario(13000.00)
    gerente2.set_salario(14000.00)

    gerente1.set_qtd_funcionario(8)
    gerente2.set_qtd_funcionario(1)

    print("\n-Gerente 1: \n-Nome:", gerente1.get_nome())
    print("-Salário:", gerente1.get_salario())
    print("-Quantidade de Funcionarios:", gerente1.get_qtd_funcionario())
    print("-Valor bonificação:", gerente1.metodo_bonificacao())
    
    print("\n-Gerente 2: \n-Nome:", gerente2.get_nome())
    print("-Salário:", gerente2.get_salario())
    print("-Quantidade de Funcionarios:", gerente2.get_qtd_funcionario())
    print("-Valor bonificação:", gerente2.metodo_bonificacao())

    
   
