def calcular_imc (n1,n2):
    calcular_peso = n1 / (n2*n2)
    return calcular_peso

if __name__ == '__main__':
    for i in range (2):
        x1 = float(input('digite o seu peso:'))
        x2 = float(input('digite a sua altura:'))
        r = calcular_imc(x1,x2)
        print('o valor do seu IMC é:', r)