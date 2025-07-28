from datetime import date
ano= date.today().year
nasc=int(input("em que ano voce nasceu:"))
idade=ano-nasc
if idade>=16:
    if idade>=18:
        print("\nvoce ja pode votar e ter cnh pois nasceu em: {}"
             "\ne tem aproximadamente:{} anos".format(nasc,idade))

    else:print("\nvoce ja pode votar mas nao pode ter cnh pois nasceu em: {}"
             "\ne tem aproximadamente:{} anos".format(nasc,idade))
else:
    print("\nvoce ainda nao pode votar e nem ter cnh pois nasceu em: {}"
          "\ne tem aproximadamente{} aons".format(nasc,idade))
