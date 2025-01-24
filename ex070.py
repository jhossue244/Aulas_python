print("\033[1;33m=\033[m" * 27)
print("       \033[1;34mBOLIS IMPORTS\033[m")
print("\033[1;33m=\033[m" * 27)
barato = ""
total = totmil = menor = cont = 0
while True:
    produto = str(input("Digite o nome do porduto: "))
    preço = float(input("Preço: R$"))
    cont += 1
    total += preço
    if preço > 1000:
         totmil += 1
    if cont == 1 or preço < menor:
         menor = preço
         barato = produto
    resp = ""
    while resp not in ["S", "N"]:
        resp = str((input("Quer continuar? [S/N] "))).strip().upper()[0]
    if resp == "N":
            break
print(f"O total da compra foi de R${total:.2f}")
print(f"Temos {totmil} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}")
print('{:-^50}'.format("BOLIS IMPORTS AGREDEÇE SUA COMPRA."))