# main.py
from classes import Mamifero, Ave, AnimalGenerico

def main():
    print("=== Testes da Superclasse (via AnimalGenerico) ===")
    ag = AnimalGenerico("Genérico", 2, 4.5, especie="Desconhecida")
    print("Nome:", ag.get_nome())
    print("Espécie:", ag.get_especie())
    print("Idade (anos):", ag.get_idade())
    print("Idade (meses):", ag.calcular_idade_em_meses())
    print("Peso atual:", ag.get_peso())
    print("Alimentando 200g...")
    ag.alimentar(200)
    print("Peso após alimentação:", ag.get_peso())
    print("Som:", ag.emitir_som())
    print()

    print("=== Testes com Mamífero (2 objetos) ===")
    # 1º objeto: todos os argumentos
    m1 = Mamifero("Rex", 3, 12.0, tipo_pelo="curto", vacinado=True, numero_crias=2, cor="Marrom")
    print("m1 nome:", m1.get_nome())
    print("m1 som:", m1.emitir_som())
    print("m1 idade em meses:", m1.calcular_idade_em_meses())
    print("m1 peso:", m1.get_peso())
    print("m1 brincar 30 minutos -> peso:", m1.brincar(30))
    # testar setters com validação
    try:
        m1.set_tipo_pelo("ondulado")
    except Exception as e:
        print("Erro esperado ao set_tipo_pelo inválido:", e)
    m1.set_tipo_pelo("longo")
    print("m1 tipo_pelo agora:", m1.get_tipo_pelo())
    print()

    # 2º objeto: só 3 argumentos (usar defaults)
    m2 = Mamifero("Luna", 1, 4.2)  # usa defaults de tipo_pelo, vacinado, numero_crias, cor
    print("m2 nome:", m2.get_nome())
    print("m2 especie:", m2.get_especie())
    print("m2 tipo_pelo default:", m2.get_tipo_pelo())
    print("m2 brincar 10 minutos -> peso:", m2.brincar(10))
    print("m2 som:", m2.emitir_som())
    print()

    print("=== Testes com Ave (2 objetos) ===")
    # 1º objeto: todos os argumentos
    a1 = Ave("Kiko", 2, 0.9, envergadura=0.8, pode_voar=True, cor="Verde", numero_ovos=3)
    print("a1 nome:", a1.get_nome())
    print("a1 som:", a1.emitir_som())
    print("a1 envergadura:", a1.get_envergadura())
    print("a1 voar 20 minutos -> peso:", a1.voar(20))

    # tentar definir envergadura inválida
    try:
        a1.set_envergadura(0)
    except Exception as e:
        print("Erro esperado ao set_envergadura inválido:", e)
    a1.set_envergadura(0.85)
    print("a1 envergadura agora:", a1.get_envergadura())
    print()

    # 2º objeto: só 3 argumentos (usar defaults)
    a2 = Ave("Piu", 1, 0.25)  # usa defaults de envergadura, pode_voar, cor, numero_ovos
    print("a2 nome:", a2.get_nome())
    print("a2 pode_voar (default):", a2.get_pode_voar())
    # tentar voar
    try:
        print("a2 voar 5 minutos -> peso:", a2.voar(5))
    except Exception as e:
        print("Erro ao tentar voar:", e)
    print("a2 som:", a2.emitir_som())
    print()

    print("=== Testes adicionais: setters da superclasse ===")
    print("m1 peso atual:", m1.get_peso())
    try:
        m1.set_peso(-5)
    except Exception as e:
        print("Erro esperado ao set_peso inválido:", e)
    m1.set_peso(11.5)
    print
