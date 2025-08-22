class Aluno:
    
    def __init__(self, nome, idade, matricula, curso):
        self.__nome = nome        
        self.__idade = idade
        self.__matricula = matricula
        self.__curso = curso

    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade
    
    def set_idade(self, idade):
        self.__idade = idade

    def get_matricula(self):
        return self.__matricula
    
    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_curso(self):
        return self.__curso
    
    def set_curso(self, curso):
        self.__curso = curso

    
    def mostra_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"Idade: {self.__idade}")
        print(f"Matrícula: {self.__matricula}")
        print(f"Curso: {self.__curso}")

    
    def mostra_dados_get(self):
        print(f"Nome: {self.get_nome()}")
        print(f"Idade: {self.get_idade()}")
        print(f"Matrícula: {self.get_matricula()}")
        print(f"Curso: {self.get_curso()}")

    
    def calcula_ano_nascimento(self, ano_atual=2025):
        return ano_atual - self.__idade



def main():
    
    aluno1 = Aluno("Renzo", 20, "2025001", "Engenharia de Software")
    aluno2 = Aluno("Maria", 22, "2025002", "Direito")
    aluno3 = Aluno("João", 19, "2025003", "Medicina")

    print("\n=== Dados dos alunos (usando atributos) ===")
    aluno1.mostra_dados()
    aluno2.mostra_dados()
    aluno3.mostra_dados()

    print("\n=== Dados dos alunos (usando GETS) ===")
    aluno1.mostra_dados_get()
    aluno2.mostra_dados_get()
    aluno3.mostra_dados_get()

    print("\n=== Testando método funcional extra ===")
    print(f"{aluno1.get_nome()} nasceu em {aluno1.calcula_ano_nascimento()}")
    print(f"{aluno2.get_nome()} nasceu em {aluno2.calcula_ano_nascimento()}")
    print(f"{aluno3.get_nome()} nasceu em {aluno3.calcula_ano_nascimento()}")

    print("\n=== Alterando dados com SETS ===")
    aluno1.set_nome("Renzo Machado")
    aluno1.set_curso("Ciência da Computação")
    aluno1.mostra_dados_get()



main()
