from p055a import FormaGeometrica, Quadrado, Circulo

if __name__ == '__main__':
    q1 = Quadrado("Azul", 2)
    print('-Quadrado 1:')
    print(' -Cor:', q1.get_cor())
    print(' -Lado:', q1.get_lado())
    print(' -Área:', q1.area())
    print(' -Perímetro:', q1.perimetro())

    q2 = Quadrado("Branco")
    print('\n-Quadrado 2:')
    print(' -Cor:', q2.get_cor())
    print(' -Lado:', q2.get_lado())
    print(' -Área:', q2.area())
    print(' -Perímetro:', q2.perimetro())

    c1 = Circulo("Roxo", 5)
    print('\n-Círculo 1:')
    print(' -Cor:', c1.get_cor())
    print(' -Raio:', c1.get_raio())
    print(' -Área:', c1.area())
    print(' -Perímetro:', c1.perimetro())

