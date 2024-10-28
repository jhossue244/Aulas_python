#primeira opção para resolução desse exercicio
'''from math import factorial
num = int(input("Digite um número para calcular o seu fatorial: "))
f = factorial(num)
print(f"O fatorial de {num} é {f}")'''
#segunda opção com laço de while
'''num = int(input("Digite um número para ver o seu fatorial: "))
f = 1
c = num
print(f"Calculando {num}! = ", end = "")
while c > 0:
    print(c, end=" ")
    print("x " if c > 1 else "=", end="")
    f *= c
    c -= 1
print(f"{f}", end = "")'''
#terceira opção com laço for
num = int(input("Digite um número para ver o seu fatorial: "))
f = 1
for c in range(num, 0, -1):
    print(c, end = "")
    print(" x " if c > 1 else "=", end = "")
    f *= c
print(f"{f}")
  