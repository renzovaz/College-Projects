def soma(a,b):
    return a + b

def subtrai(a,b):
    return a - b

if __name__ == '__main__':
    v1=int(input("digite o primeiro valor: "))
    v2 = int(input("digite o segundo valor: "))
    opcao= input("[+] para somar [-] para subtrair ")
    if opcao == "+":
        print(f"a soma de {v1} + {v2} é: {soma(v1,v2)}")
    elif opcao == "-":
        print(f"a subtração de {v1} - {v2} é: {subtrai(v1, v2)}")
    else:
        print("opção invalida")
