num = int(input("Digite um número para ver sua tabuada: "))
print("\033[33m=\033[m" * 11)
for tabuada in range(0, 11,):
    print(f"{num} x {tabuada} = {num * tabuada}")
print("\033[33m=\033[m" * 11)
