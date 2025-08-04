l_nomes = []
def menu():
    print('\n-- MENU CRUD --')
    print('[c] - create  (inserir um item)')
    print('[r] - read    (mostrar toda a lista)')
    print('[u] - update  (substituir um item')
    print('[d] - delete  (remover um item)')
    print('[e] - exit    (sair)')
    return input('Opção:') .lower()
def create():
    nome = input('Nome:')
    l_nomes.append(nome)
def read():
    print(l_nomes)
    for item in l_nomes:
        print(item)
def update():
    novo_valor = input('novo valor:')
    indice = int(input('qual a posição(índicie)'))
    l_nomes[indice] = novo_valor
def delete():
    remover = input('deletar valor')
    l_nomes.remove(remover)


if __name__ == '__main__':
    while True:
        op = menu()
        if op == 'c':
            # print('create ()')
            create()
        elif op == 'r':
            read()
        elif op == 'u':
            update()
        elif op == 'd':
            delete()
        elif op == 'e':
            break




