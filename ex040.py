print("\033[33m-=\033[m" * 10)
print("E.E CAETANO MIELE")
print("\033[33m-=\033[m" * 10)
n1 = float(input("primeira nota do aluno: "))
n2 = float(input("Segunda nota do aluno: "))
media = (n1 + n2) / 2
print(f"Tirando {n1:.1f} e {n2:.1f}, a media do aluno é {media}")
if media < 5.0:
    print("\033[1;37;41mO aluno está REPROVADO.\033[m")
elif 7 > media >= 5.0:
    print("\033[1;37;43mO aluno está de RECUPERAÇÃO.\033[m")
elif media > 7.0:
    print("\033[1;37;42mO aluno está APROVADO.\033[m")
