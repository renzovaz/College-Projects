
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Superclasse abstrata que representa um animal em uma clínica veterinária.
    Atributos comuns: nome, idade (anos), peso (kg), especie (padrão 'Indefinida')
    """

    def __init__(self, nome: str, idade: int, peso: float, especie: str = 'Indefinida'):
        self._nome = nome
        self._idade = idade
        self._peso = peso
        self._especie = especie

    
    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    def get_peso(self):
        return self._peso

    def get_especie(self):
        return self._especie

    
    def set_nome(self, novo_nome: str):
        if not novo_nome:
            raise ValueError("Nome não pode ser vazio.")
        self._nome = novo_nome

    def set_idade(self, nova_idade: int):
        if not isinstance(nova_idade, int) or nova_idade < 0:
            raise ValueError("Idade deve ser um inteiro >= 0.")
        self._idade = nova_idade

    def set_peso(self, novo_peso: float):
        
        try:
            peso_float = float(novo_peso)
        except Exception:
            raise ValueError("Peso deve ser um número.")
        if peso_float <= 0:
            raise ValueError("Peso deve ser maior que zero.")
        self._peso = peso_float

    def set_especie(self, nova_especie: str):
        if not nova_especie:
            self._especie = 'Indefinida'
        else:
            self._especie = nova_especie

    
    def calcular_idade_em_meses(self):
        """Retorna a idade em meses."""
        return self._idade * 12

    def alimentar(self, gramas: float):
        """
        Alimenta o animal: aumenta o peso proporcionalmente.
        Recebe gramas (float) e converte para kg (dividindo por 1000).
        """
        try:
            g = float(gramas)
        except Exception:
            raise ValueError("Quantidade em gramas inválida.")
        if g <= 0:
            raise ValueError("A quantidade de alimento deve ser positiva.")
        aumento_kg = g / 1000.0
        self._peso += aumento_kg
        return self._peso

   
    @abstractmethod
    def emitir_som(self) -> str:
        """Deve retornar uma string representando o som do animal."""
        pass



class Mamifero(Animal):
    """
    Subclasse concreta: Mamifero
    Atributos específicos: tipo_pelo, vacinado (bool), numero_crias (int), cor
    """

    def __init__(self, nome: str, idade: int, peso: float,
                 tipo_pelo: str = 'curto', vacinado: bool = True,
                 numero_crias: int = 0, cor: str = 'Indefinida'):
        super().__init__(nome, idade, peso)
        self._tipo_pelo = tipo_pelo
        self._vacinado = vacinado
        self._numero_crias = numero_crias
        self._cor = cor

    
    def get_tipo_pelo(self):
        return self._tipo_pelo

    def get_vacinado(self):
        return self._vacinado

    def get_numero_crias(self):
        return self._numero_crias

    def get_cor(self):
        return self._cor

    
    def set_tipo_pelo(self, novo_tipo: str):
        if novo_tipo.lower() not in ('curto', 'longo', 'sem pelo'):
            
            raise ValueError("tipo_pelo deve ser 'curto', 'longo' ou 'sem pelo'.")
        self._tipo_pelo = novo_tipo

    def set_vacinado(self, status: bool):
        if not isinstance(status, bool):
            raise ValueError("vacinado deve ser booleano.")
        self._vacinado = status

    def set_numero_crias(self, n: int):
        if not isinstance(n, int) or n < 0:
            raise ValueError("numero_crias deve ser inteiro >= 0.")
        self._numero_crias = n

    def set_cor(self, cor: str):
        if not cor:
            self._cor = 'Indefinida'
        else:
            self._cor = cor

    
    def emitir_som(self) -> str:
        return f"{self._nome} (mamífero) faz: som de mamífero (ex.: latido/miado)."

   
    def brincar(self, minutos: int):
        """Brincar reduz levemente o peso. Retorna peso atual."""
        if not isinstance(minutos, int) or minutos <= 0:
            raise ValueError("minutos deve ser inteiro positivo.")
        perda = (minutos * 0.001)  # 1g por minuto -> 0.001 kg/min
        self._peso = max(0.0, self._peso - perda)
        return self._peso



class Ave(Animal):
    """
    Subclasse concreta: Ave
    Atributos específicos: envergadura (m), pode_voar (bool), cor, numero_ovos
    """

    def __init__(self, nome: str, idade: int, peso: float,
                 envergadura: float = 0.5, pode_voar: bool = True,
                 cor: str = 'Indefinida', numero_ovos: int = 0):
        super().__init__(nome, idade, peso)
        self._envergadura = envergadura
        self._pode_voar = pode_voar
        self._cor = cor
        self._numero_ovos = numero_ovos

    
    def get_envergadura(self):
        return self._envergadura

    def get_pode_voar(self):
        return self._pode_voar

    def get_cor(self):
        return self._cor

    def get_numero_ovos(self):
        return self._numero_ovos

    
    def set_envergadura(self, valor: float):
        try:
            v = float(valor)
        except Exception:
            raise ValueError("envergadura deve ser numérico.")
        if v <= 0:
            raise ValueError("envergadura deve ser maior que zero.")
        self._envergadura = v

    def set_pode_voar(self, pode: bool):
        if not isinstance(pode, bool):
            raise ValueError("pode_voar deve ser booleano.")
        self._pode_voar = pode

    def set_cor(self, cor: str):
        if not cor:
            self._cor = 'Indefinida'
        else:
            self._cor = cor

    def set_numero_ovos(self, n: int):
        if not isinstance(n, int) or n < 0:
            raise ValueError("numero_ovos deve ser inteiro >= 0.")
        self._numero_ovos = n

    
    def emitir_som(self) -> str:
        return f"{self._nome} (ave) faz: piu-piu / som de ave."

    
    def voar(self, minutos: int):
        """
        Simula voo: diminui peso por gasto de energia se pode_voar True.
        Retorna o peso atual.
        """
        if not isinstance(minutos, int) or minutos <= 0:
            raise ValueError("minutos deve ser inteiro positivo.")
        if not self._pode_voar:
            raise RuntimeError(f"{self._nome} não pode voar.")
        gasto = (minutos * 0.0008)  # 0.8g por minuto -> 0.0008 kg/min
        self._peso = max(0.0, self._peso - gasto)
        return self._peso



class AnimalGenerico(Animal):
    """
    Implementa o método abstrato de forma genérica para permitir instanciar
    um 'Animal' e testar os métodos da superclasse.
    """

    def __init__(self, nome: str, idade: int, peso: float, especie: str = 'Indefinida'):
        super().__init__(nome, idade, peso, especie)

    def emitir_som(self) -> str:
        return f"{self._nome} faz um som genérico."
