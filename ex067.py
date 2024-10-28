from time import sleep


while True:
    num = int(input("Quer ver a tabuada de qual número? "))
    print("_" * 30)
    if num < 0:
        break
    for c in range(1, 11):
        print(f"{num} x {c} = {num * c}")
    print("_" * 30)
print("Encerrando...")
sleep(4)
print("PROGRAMA ENCERRADO, Volte sempre!")
