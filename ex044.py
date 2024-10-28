print("\033[1;34m=\033[m" * 13)
print("\033[1;36mBOLIS IMPORTS\033[m")
print("\033[1;34m=\033[m" * 13)
preço = float(input("Preço das compras: R$"))
print("FORMAS DE PAGAMENTO")
print("[1] dinehiro/cheque")
print("[2] Avista no cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")
opção = int(input("Digite a opção desejada: "))
if opção == 1: 
    total =  preço - (preço * 10) / 100
elif opção == 2:
    total = preço - (preço * 5) / 100
elif opção == 3:
    total = preço
    parcelas = preço / 2
    print(f"Sua compra será parceladas em 2x  de R${parcelas:.2f} ")
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input("Quantas parcelas? "))
    parcelas = total / totparc
    print(f"Sua compra R${preço} parcelado em {totparc}x de R${parcelas} COM JUROS")
else:
    total = preço
    print("\033[1;31mOPÇÃO INVALIDA.\033[m")
print(f"Sua compra de R${preço} vai custar R${total} no final")
