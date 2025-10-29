from p054a import Pessoa,Professor,Funcionario

if __name__ == '__main__':
    p1 = Professor ("Silvio", 1 , 1200.00 , 5)
    p1.mostra_dados()
    p2 = Professor ("Alice", 1, 1300.00)
    p2.mostra_dados()
    p3 = Professor ("Emilly", 0)
    p3.mostra_dados()
    f1 = Funcionario("Carlos",3,3200.00)
    f1.mostra_dados()
    f2 = Funcionario("Ana",0)
    f2.mostra_dados()
    f3 = Funcionario("Eric",12,1500000.00)
    f3.mostra_dados()

    print(f"Salario do 1º Professor: {p1.salario_total()}")
    print(f"Salario do 2º Professor: {p2.salario_total()}")
    print(f"Salario do 3º Professor: {p3.salario_total()}")

