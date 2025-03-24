import random

sort = random.randint(0,5)

num = int(input("Tente acertar número que o computador achou entre 0 e 5: "))

if num == sort:
    print("Parabéns você acertou!")

else:
    print("Infelizmente você errou.")