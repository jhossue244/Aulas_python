from datetime import date

print("\033[1;35m*\033[m" * 23)
print("CONFEDERAÇÃO DE NATAÇÃO")
print("\033[1;35m*\033[m" * 23)
idade = int(input("Digite ao do seu nascimento: "))
atual = date.today().year
categoria = (atual - idade)
print(f"O atleta tem {categoria}")
if categoria <= 9:
    print("Conforme sua idade, a sua categoria é MIRIM")
elif categoria <= 14:
    print("Conforme sua idade, a sua categoria é INFANTIL")
elif categoria <= 19:
    print("Conforme sua idade, a sua categoria é JUNIOR")
elif categoria <= 25:
    print("Conforme sua idade, a sua categoria SÊNIOR")
else:
    print("Conforme sua idade, a sua categoria é MASTER")
    