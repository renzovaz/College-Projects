media=ct=soma=0
for i in range(0,5,1):
    nota=float(input("digite a nota: "))
    ct+=1
    soma+=nota
media= soma/ct
print(f"a soma de todas as notas foi:{soma}")
print(f"a media da turma foi: {media:.2f}")
