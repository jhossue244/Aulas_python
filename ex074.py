from random import randint


numeros = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)

print(f"Os números sorteados foram ", end = "")
for n in numeros:
    print(f"{n}", end = "")
print(f"\nO maior número foi {max(numeros)}")
print(f"O menor número foi {min(numeros)}")
