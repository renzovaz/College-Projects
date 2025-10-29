from classes import Pessoa, Funcionario, Gerente


print("=== Testando Superclasse Pessoa ===")
p1 = Pessoa("Carlos", 30)
p1.apresentar()
p1.aniversario()
p1.set_nome("Ca")  
p1.set_idade(-5)   
p1.set_nome("Carla")
p1.set_idade(31)
print(p1.get_nome(), p1.get_idade())


print("\n=== Testando Subclasse Funcionario ===")
f1 = Funcionario("Ana", 25, "Atendente", 2000, "Noturno")
f2 = Funcionario("Lucas", 22, "Vendedor", 1800)  

f1.trabalhar()
f2.trabalhar()

f1.set_salario(-100)  
f1.set_cargo("Supervisora")
f1.set_salario(2500)

print(f1.get_cargo(), f1.get_salario(), f1.get_turno())


f2.apresentar()
f2.aniversario()


print("\n=== Testando Subclasse Gerente ===")
g1 = Gerente("Marcos", 40, "Gerente de Vendas", 5000, 8)
g2 = Gerente("Paula", 38, "Gerente de RH", 5500) 

g1.liderar()
g2.liderar()

g1.set_equipe(-3)  
g1.set_equipe(10)

g1.apresentar()
g2.aniversario()
