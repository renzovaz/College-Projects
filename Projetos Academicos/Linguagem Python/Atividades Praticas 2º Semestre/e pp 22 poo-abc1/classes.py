from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome, idade, salario, cargo="Indefinido"):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.cargo = cargo


    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_salario(self):
        return self.salario

    def get_cargo(self):
        return self.cargo

   
    def set_nome(self, nome):
        if nome == "":
            print("Nome não pode ser vazio.")
        else:
            self.nome = nome

    def set_idade(self, idade):
        self.idade = idade

    def set_salario(self, salario):
        if salario < 0:
            print("Salário não pode ser negativo.")
        else:
            self.salario = salario

    def set_cargo(self, cargo):
        self.cargo = cargo

    
    def aumentar_salario(self, valor):
        self.salario += valor
        print(f"Salário de {self.nome} aumentado para {self.salario}")

    def mostrar_dados(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | Salário: {self.salario} | Cargo: {self.cargo}")

    
    @abstractmethod
    def calcular_bonus(self):
        pass



class Gerente(Funcionario):
    def __init__(self, nome, idade, salario, setor="Geral", cargo="Gerente"):
        super().__init__(nome, idade, salario, cargo)
        self.setor = setor

    
    def get_setor(self):
        return self.setor

    def set_setor(self, setor):
        self.setor = setor

    
    def calcular_bonus(self):
        return self.salario * 0.2  # 20% de bônus

  
    def realizar_reuniao(self):
        print(f"O gerente {self.nome} está realizando uma reunião no setor {self.setor}.")



class Estagiario(Funcionario):
    def __init__(self, nome, idade, salario, horas_por_dia=6, cargo="Estagiário"):
        super().__init__(nome, idade, salario, cargo)
        self.horas_por_dia = horas_por_dia

    
    def get_horas_por_dia(self):
        return self.horas_por_dia

    def set_horas_por_dia(self, horas):
        if horas <= 0:
            print("Horas devem ser positivas.")
        else:
            self.horas_por_dia = horas

    
    def calcular_bonus(self):
        return self.salario * 0.05  # 5% de bônus

    
    def estudar(self):
        print(f"O estagiário {self.nome} está estudando após o expediente.")
