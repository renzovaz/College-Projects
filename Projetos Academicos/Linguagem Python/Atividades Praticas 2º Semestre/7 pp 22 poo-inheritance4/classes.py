class Funcionario:
    def __init__(self, nome, cpf, salario, cargo="Funcionário"):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo

    
    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_salario(self):
        return self.salario

    def get_cargo(self):
        return self.cargo

    
    def set_nome(self, nome):
        self.nome = nome

    def set_cpf(self, cpf):
        
        if len(cpf) == 11 and cpf.isdigit():
            self.cpf = cpf
        else:
            print("CPF inválido! Deve conter 11 dígitos numéricos.")

    def set_salario(self, salario):
        if salario > 0:
            self.salario = salario
        else:
            print("Salário deve ser maior que zero!")

    def set_cargo(self, cargo):
        self.cargo = cargo

   
    def calcular_bonus(self, percentual):
        """Retorna o valor do bônus com base no percentual."""
        return self.salario * (percentual / 100)

    def exibir_informacoes(self):
        """Exibe as informações básicas do funcionário."""
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R${self.salario:.2f}")



class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, departamento, equipe=0, cargo="Gerente"):
        super().__init__(nome, cpf, salario, cargo)
        self.departamento = departamento
        self.equipe = equipe  

  
    def get_departamento(self):
        return self.departamento

    def get_equipe(self):
        return self.equipe

   
    def set_departamento(self, departamento):
        self.departamento = departamento

    def set_equipe(self, equipe):
        
        if equipe >= 0:
            self.equipe = equipe
        else:
            print("Erro: número de integrantes da equipe não pode ser negativo!")

    
    def calcular_bonus_gerente(self):
        """Gerente ganha bônus de 10% do salário por pessoa na equipe."""
        return self.salario * 0.1 * self.equipe



class Desenvolvedor(Funcionario):
    def __init__(self, nome, cpf, salario, linguagem, projetos=1, cargo="Desenvolvedor"):
        super().__init__(nome, cpf, salario, cargo)
        self.linguagem = linguagem
        self.projetos = projetos

    
    def get_linguagem(self):
        return self.linguagem

    def get_projetos(self):
        return self.projetos

    
    def set_linguagem(self, linguagem):
        self.linguagem = linguagem

    def set_projetos(self, projetos):
        
        if projetos >= 0:
            self.projetos = projetos
        else:
            print("Erro: número de projetos não pode ser negativo!")

    
    def produtividade(self):
        """Calcula produtividade com base na quantidade de projetos."""
        return self.projetos * 100
