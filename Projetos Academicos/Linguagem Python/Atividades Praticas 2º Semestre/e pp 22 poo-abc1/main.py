from classes import Funcionario, Gerente, Estagiario

def main():
    print("=== Teste da Superclasse (Funcionario) ===")
    
    print("\n=== Gerente ===")
    g1 = Gerente("Carlos", 40, 8000, "Vendas")
    g1.mostrar_dados()
    print("Bônus:", g1.calcular_bonus())
    g1.realizar_reuniao()

    print("\nAlterando salário do gerente:")
    g1.set_salario(8500)
    g1.mostrar_dados()

    print("\n=== Estagiário ===")
    e1 = Estagiario("João", 21, 1200)
    e1.mostrar_dados()
    print("Bônus:", e1.calcular_bonus())
    e1.estudar()

    print("\nAlterando horas de trabalho:")
    e1.set_horas_por_dia(8)
    print("Horas por dia:", e1.get_horas_por_dia())

    print("\n=== Criando segundo estagiário com menos argumentos ===")
    e2 = Estagiario("Maria", 19, 1000)
    e2.mostrar_dados()
    print("Bônus:", e2.calcular_bonus())

if __name__ == "__main__":
    main()
