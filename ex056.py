somaidade = 0
totmeulher20 = 0
mediaidade = 0
nomevelho = 0
maioridadehomem = 0
for p in range(1, 5):
    print(f"-----{p}° PESSOA-----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmeulher20 += 1
mediaidade += somaidade / 4
print(f"A mdeia de idade do grupo é de {mediaidade}")
print(f"O home mais velho tem {maioridadehomem} e se chama {nomevelho}")
print(f"Ao todo são {totmeulher20} mulheres com menos de 20 anos.") 
