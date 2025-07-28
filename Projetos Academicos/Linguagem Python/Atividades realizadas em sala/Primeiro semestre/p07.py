compra= float(input("qual o preço de compra do produto:"))
venda= float(input("qual o preço de venda do seu produt:"))
if venda>compra:
    print("teve lucro")
elif compra>venda:
    print("teve prejuizo")
else:
    print("os valores sao iguais")
