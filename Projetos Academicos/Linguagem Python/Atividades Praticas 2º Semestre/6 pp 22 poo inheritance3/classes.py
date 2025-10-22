class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    
    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    
    def set_nome(self, nome):
        if len(nome.strip()) < 3:
            print("Erro: o nome deve ter pelo menos 3 caracteres.")
        else:
            self._nome = nome

    def set_idade(self, idade):
        if idade < 0:
            print("Erro: a idade não pode ser negativa.")
        else:
            self._idade = idade

    
    def apresentar(self):
        print(f"Olá, meu nome é {self._nome} e tenho {self._idade} anos.")

    def aniversario(self):
        self._idade += 1
        print(f"Parabéns, {self._nome}! Agora você tem {self._idade} anos.")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario, turno="Diurno"):
        super().__init__(nome, idade)
        self._cargo = cargo
        self._salario = salario
        self._turno = turno

   
    def get_cargo(self):
        return self._cargo

    def get_salario(self):
        return self._salario

    def get_turno(self):
        return self._turno

    
    def set_cargo(self, cargo):
        if cargo == "":
            print("Erro: o cargo não pode estar vazio.")
        else:
            self._cargo = cargo

    def set_salario(self, salario):
        if salario <= 0:
            print("Erro: o salário deve ser maior que zero.")
        else:
            self._salario = salario

    def set_turno(self, turno):
        self._turno = turno

    
    def trabalhar(self):
        print(f"{self._nome} está trabalhando no turno {self._turno} como {self._cargo}.")


class Gerente(Funcionario):
    def __init__(self, nome, idade, cargo, salario, equipe=0):
        super().__init__(nome, idade, cargo, salario)
        self._equipe = equipe

    
    def get_equipe(self):
        return self._equipe

    
    def set_equipe(self, equipe):
        if equipe < 0:
            print("Erro: o número de pessoas na equipe não pode ser negativo.")
        else:
            self._equipe = equipe

    
    def liderar(self):
        print(f"O gerente {self._nome} está liderando uma equipe de {self._equipe} pessoas.")
