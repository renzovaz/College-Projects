import sys

def mostra_valor(valor):
    print(f'valor recebido: {valor}')

if __name__ == "__main__":
    mostra_valor(sys.argv[1])