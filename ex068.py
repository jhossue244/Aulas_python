from random import randint
print("-=" * 15)
print("        PAR OU ÍMPAR")
print("-=" * 15)
v = 0
#faz o jogo rodar até o jogador perder
while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 11)#faz o computador gerar um número entre 1 e 10
    total = computador + jogador
    tipo = ""#variavel criada para saber se o jogador quer par ou impar
    while tipo not in ["P", "I"]:
        tipo = str(input("Par ou Ímpar [P/I]: ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador {computador}. Total foi {total} ", end ="")
    print("DEU PAR" if total % 2 == 0 else "DEU ÍMPAR")
#aqui o programa descobri se o resultado deu par ou impar
    if tipo == "P":
        if total % 2 == 0:
            print("Você VENCEU!")
            v += 1
        else:
            print("Você PERDEU!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você VENCEU!")
            v += 1
        else:
            print("Você PERDEU!")
            break
        print("Vamos jogar novamente...")
print(f"GAME OVER. Você venceu {v} vezez.")
