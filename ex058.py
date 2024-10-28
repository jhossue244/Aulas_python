from random import randint


print("-=-"*20)
print("Vou pensar em um número entre 1 e 10. Tente adivinhar...")
print("-=-"*20)
palpites = 0
computador = randint(1, 10)
num = ""
while num != computador:
    num = int(input("Digite um número: "))
    print("\033[1;31mO número é outro tente novamente!\033[m")
    palpites +=1
    if num == computador:
        print("\033[1;32mPARABÉNS!! VOCÊ ACERTOU O NÚMERO.\033[m")
print(f"Você precisou de {palpites} tentativas")
