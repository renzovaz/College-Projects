def calcular_media (n1,n2,n3):
    calculo_media= n1+n2+n3
    resultado_media = calculo_media/ 3
    return resultado_media

if __name__ == '__main__':
    x1 = int(input('digite o valor da nota 1:'))
    x2 = int(input('digite o valor da nota 2:'))
    x3 = int(input('digite o valor da nota 3:'))
    r = calcular_media(x1,x2,x3)
    print('a media das notas recebidas é:',r)