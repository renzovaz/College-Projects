from datetime import date
ano= date.today().year
nasc=int(input("em que ano voce nasceu:"))
idade=ano-nasc
if idade>=16:
    print("\nvoce ja pode votar pois nasceu em: {}"
          "\ne tem aproximadamente:{} anos".format(nasc,idade))
else:
    print("\nvoce ainda nao pode votar pois nasceu em: {}"
          "\ne tem aproximadamente{} aons".format(nasc,idade))
