r1 = int(input("Digite primeira reta: "))
r2 = int(input("Digite segunda reta: "))
r3 = int(input("Digite terceira reta: "))

soma1 = r1 + r2
soma2 = r2 + r3
soma3 = r3 + r1

if soma1 > r3 and soma2 > r1 and soma3 > r2:
    print("Formamos um triângulo")
else:
    print("Não se forma triângulo com as medidas destacadas.")
