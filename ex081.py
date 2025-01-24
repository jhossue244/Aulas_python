
valores = []
while True:
    num = int(input("Digite um número: "))
    valores.append(num)
    resp = str(input("Quer continuar? ")).strip().upper()[0]
    if resp == "N":
        break
    valores.sort(reverse=True)
print(f"Você digitou {len(valores)} elementos.")
print(f"Os valores na ordem descrescente são {valores}")
if 5 in valores:
    print("O número 5 está presente na lista")
else:
    print("O número 5 não está presente na lista")