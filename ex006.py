from time import sleep
from math import sqrt

num = int(input("Digite um número: "))
print("CALCULANDO...")
sleep(3)
print(f"o dobro de {num} vale {num * 2}")
print(f"O trilpo de {num} vale {num * 3}")
print(f"A raiz quadrada de {num} é igual a {sqrt(num):.2f}")
