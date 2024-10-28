from time import sleep

print("-=" * 10)
print("gerador de PA")
print("-=" * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} - ", end = "")
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
