from classes import Funcionario, Gerente, Desenvolvedor

def main():
    print("===== TESTE DA SUPERCLASSE FUNCIONARIO =====")
    f1 = Funcionario("Carlos Silva", "12345678901", 3000.00)
    f1.exibir_informacoes()
    print("Bônus (10%): R$", f1.calcular_bonus(10))

    f1.set_salario(3500)
    f1.set_cpf("98765432100")
    f1.exibir_informacoes()
    print()

    print("===== TESTE DA SUBCLASSE GERENTE =====")
    g1 = Gerente("Mariana Souza", "12312312312", 8000, "Vendas", 5)
    g2 = Gerente("Pedro Lima", "99988877766", 9000, "Marketing")

    g1.exibir_informacoes()
    print("Departamento:", g1.get_departamento())
    print("Equipe:", g1.get_equipe())
    print("Bônus Gerente:", g1.calcular_bonus_gerente())
    print()

    g2.set_equipe(3)
    g2.exibir_informacoes()
    print("Departamento:", g2.get_departamento())
    print("Equipe:", g2.get_equipe())
    print("Bônus Gerente:", g2.calcular_bonus_gerente())
    print()

    print("===== TESTE DA SUBCLASSE DESENVOLVEDOR =====")
    d1 = Desenvolvedor("João Pereira", "55544433322", 6000, "Python", 4)
    d2 = Desenvolvedor("Ana Costa", "44433322211", 5500, "JavaScript")

    d1.exibir_informacoes()
    print("Linguagem:", d1.get_linguagem())
    print("Projetos:", d1.get_projetos())
    print("Produtividade:", d1.produtividade())
    print()

    d2.set_projetos(2)
    d2.exibir_informacoes()
    print("Linguagem:", d2.get_linguagem())
    print("Projetos:", d2.get_projetos())
    print("Produtividade:", d2.produtividade())

if __name__ == "__main__":
    main()
