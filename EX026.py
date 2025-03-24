from os.path import split

frase = str(input("Digite uma frase: ")).lower().strip()

print("A letra 'A' aparece {}".format(frase.count('a')))
print("A primeira posição é: {}".format(frase.find('a')+1))
print("A ultima posição é: {}".format(frase.rfind('a')+1))