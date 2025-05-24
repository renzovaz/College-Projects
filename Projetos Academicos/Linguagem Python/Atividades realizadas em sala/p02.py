nota1=float(input("digite sua nota:"))
nota2=float(input("digite sua outra nota:"))
media=(nota1+nota2)/2
if media>=5:
    print("voce esta aprovado no semestre:{:.2f}".format(media))
else:
    print("voce não esta aprovado no semestre:{:.2f}".format(media))
