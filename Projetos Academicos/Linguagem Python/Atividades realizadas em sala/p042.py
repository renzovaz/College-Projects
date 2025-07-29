def horas_converte_minuto_2 (x1,x2):
    a = x1 * 60
    b = a + x2
    print('Resultado:',b)

if __name__ == '__main__':
    x1 = int(input('Digite horas:'))
    x2 = int(input('Digite minutos'))
    r = horas_converte_minuto_2