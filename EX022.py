from itertools import count

nome = str(input("Digite seu nome completo: "))


letras = len(nome.replace(" ",""))

pnomeT = nome.split()


print(f"Nome em maiúsculo: {nome.upper()}")
print(f"Nome em minusculo: {nome.lower()}")
print(f"Total de letras: {letras}")
print("Total de letras no primeiro nome: {}".format(len(pnomeT[0])))
