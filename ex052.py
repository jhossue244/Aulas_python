tot = 0
num = int(input("Digite um número: "))
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[33m", end = " ")
        tot += 1
    else:
        print("\033[31m", end = " ")
    print(c, end = " ")
print(f"\n\033[m número {num} foi divisivel {tot} vezes")
if tot == 2: 
    print("E por isso ele É PRIMO!")
else:
    print("E por isso NÃO É PRIMO!")
