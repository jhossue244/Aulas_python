valores = []
impares = []
pares = []
while True:
    num = int(input("Digite um número: "))
    valores.append(num)
    resp = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if resp == "N":
        break
for p in valores:
    if p % 2 == 0:
        pares.append(p)
for i in valores:
    if i % 2 == 1:
        impares.append(i)
print(f"Os valores digitados foram {valores}")
print(f"Os valores pares digitados são {pares}")
print(f"Os valores impares digitados foram {impares}")
