valores = []
while True:
    num = int(input("Digite um número para adicionar a lista: "))
    if num not in valores:
        print("Número adicionado com sucesso...")
        valores.append(num)
    else:
        print("Número já adicionado á lista...")
    resp = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if resp == "N":
        break
valores.sort()
print(f"Você digitou os valores {valores}")
