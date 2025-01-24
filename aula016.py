#Tuplas são imutáveis
#lanche = ("hamburguer", "suco", "pizza", "pudim", "batata frita")
"""esse é usado o for in range, mas da o mesmo resultado só que com um metodo diferente
for cont in range(0, len(lanche)):
    print(f"eu vou comer {(lanche[cont])} na posição {cont}")
esse é usa diretamente a variavel composta
for pos, comida in enumerate(lanche):
    print(f"eu vou comer {comida} na posição {pos}")
print("Comi pra caramba")

for comida in lanche:
    print(f"Eu vou comer comida {comida}")"""

#print(sorted(lanche))
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = (a + b)
print(c)
print(c.index(2))