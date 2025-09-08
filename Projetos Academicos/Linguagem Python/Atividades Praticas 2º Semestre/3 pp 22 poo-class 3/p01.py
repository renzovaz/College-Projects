class Funcionario:
    def __init__(self, nome, salario, idade, carga_horaria):
        self.nome = nome
        self.set_salario(salario)  
        self.idade = idade
        self.carga_horaria = carga_horaria

    
    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

    def get_idade(self):
        return self.idade

    def get_carga_horaria(self):
        return self.carga_horaria

    
    def set_nome(self, nome):
        self.nome = nome

    def set_salario(self, salario):
        if salario < 0:
            print("Erro: salário não pode ser negativo.")
            self.salario = 0.0
        else:
            self.salario = salario

    def set_idade(self, idade):
        self.idade = idade

    def set_carga_horaria(self, carga_horaria):
        self.carga_horaria = carga_horaria

   
    def mostra_dados_1(self):
        print(f"Nome: {self.nome}, Salário: {self.salario}, Idade: {self.idade}, Carga Horária: {self.carga_horaria}h/semana")

    
    def mostra_dados_2(self):
        print(f"Nome: {self.get_nome()}, Salário: {self.get_salario()}, Idade: {self.get_idade()}, Carga Horária: {self.get_carga_horaria()}h/semana")

    
    def retorna_dados(self):
        return (self.nome, self.salario, self.idade, self.carga_horaria)

    
    def aumentar_salario(self, valor):
        if valor > 0:
            self.salario += valor
        else:
            print("Valor de aumento deve ser positivo.")

    
    def calcular_salario_mensal_proporcional(self):
        
        base_carga = 40
        proporcao = self.carga_horaria / base_carga
        return self.salario * proporcao
