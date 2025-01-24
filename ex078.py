valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f"Digite um número para a posição {c}: ")))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(f"Você digitou os valores {valores}")
print(f"O maior número digitao foi {maior} nas posição ", end = "")
for i, v in enumerate(valores):
    if v == maior:
        print(f"{i}...", end="")
print()
print(f"O mnenor número digitado foi {menor} na posição ", end="")
for i, v in enumerate(valores):
    if v == menor:
        print(f"{i}...", end="")
print()
