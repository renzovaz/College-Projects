
l_nomes = []
def menu():
    print('\n-- MENU CRUD --')
    print('[c] - create  (inserir um item)')
    print('[r] - read    (mostrar toda a lista)')
    print('[u] - update  (substituir um item)')
    print('[d] - delete  (remover um item)')
    print('[e] - exit    (sair)')
    while True:
        v = input('Opção: ') .lower()
        if v == 'c' or v == 'r' or v == 'u' or v == 'd' or v == 'e' :
            return v
        else:
            print('Opção inválida, tente novamente')

def create():
    while True:
        nome = input('Nome:')
        l_nomes.append(nome)
        if nome == '':
            break
def read():
    if l_nomes != []:
        for item in l_nomes:
            print(item)
    else:
        print('Lista vazia.')
def update():
    novo_valor = input('digite o novo nome:')
    indice = int(input('qual a posição(índicie):'))
    l_nomes[indice] = novo_valor
def delete():
    remover = input('Qual nome você quer remover da lista?')
    l_nomes.remove(remover)


if __name__ == '__main__':
    while True:
        op = menu()
        if op == 'c':
            create()
        elif op == 'r':
            read()
        elif op == 'u':
            update()
        elif op == 'd':
            delete()
        elif op == 'e':
            break



