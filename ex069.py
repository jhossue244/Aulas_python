print("=" * 25)
print("   CADASTRE UMA PESSOA")
print("=" * 25)
tot18 = toth =  totm20 = 0
while True:
    idade = int(input("IDADE: "))
    sexo = ""
    while sexo not in ["F", "M"]:
        sexo = str(input("SEXO [M/F]: ")).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == "M":
        toth += 1
    if sexo == "F" and idade < 20:
        totm20 += 1
    resp = ""
    while resp not in ["S", "N"]:
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {tot18}")
print(f"Ao todo temos {toth} homens cadastrados")
print(f"E temos {totm20} com menos de 20 anos.")
