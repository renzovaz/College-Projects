def mostra_valor(valor):
    print(valor)

def mostra2_valores(valor1, valor2): #para mostrar dois valores ao mesmo tempo, precisou colocar duas variáveis dentro da def
    print(valor1, valor2)

if __name__ == '__main__':
    print("Valores:")
    mostra_valor(5)
    mostra_valor(23.8)

    v_inteiro = 43
    mostra_valor(v_inteiro)
    v_real = 37.4
    mostra_valor(v_real)

    v_inteiro = int(input("Digite um número inteiro:"))
    mostra_valor(v_inteiro)
    v_real = float(input("Digite um número real:"))
    mostra_valor(v_real)

    print("Dois valores são mostrados ao mesmo tempo:")
    mostra2_valores(5, 10)
    