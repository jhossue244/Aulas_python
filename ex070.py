print("\033[1;33m=\033[m" * 27)
print("       \033[1;34mBOLIS IMPORTS\033[m")
print("\033[1;33m=\033[m" * 27)
total = maior = menor = 0
while True:
    nome = str(input("Nome do produto: ")).strip()
    preço = int(input("Preço: R$"))
    total += preço
    if preço > 1000:
        maior += 1
    if preço < maior:
        menor = preço
    resp = ""
    while resp not in ["S", "N"]:
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print(f"O total da compra foi R${total}")
print(f"temos {maior} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi  que custa {menor}")
