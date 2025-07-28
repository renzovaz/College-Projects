def  horas_converte_minuto (x1,x2):
    a = x1 * 60
    b = a+x2
    return b

if __name__ == '__main__':

    x1=int(input('digite horas:'))
    x2=int(input('digite minutos:'))
    r = horas_converte_minuto
    print (r)