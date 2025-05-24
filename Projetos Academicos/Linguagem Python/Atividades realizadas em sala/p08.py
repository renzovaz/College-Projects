compra= float(input("qual o preço de compra do produto:"))
venda= float(input("qual o preço de venda do seu produt:"))
valor= venda-compra
if venda>compra:
    print("\nteve lucro")
    print("o seu lucro foi de: {:.2f} reais".format(valor))
elif compra>venda:
    print("\nteve prejuizo")
    print("o seu prejuizo foi de: {:.2f} reais".format(valor))
else:
    print("\nos valores sao iguais")
    print("nao obteve lucro nem prejuizo")
