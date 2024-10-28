#Minha solução que deu o mesmo resultado
"""num = 0
contador = 0 
media = 0
r = "S"
menor = 99999
maior = 0
while r == "S":
    num = int(input("Digite um número: "))
    r = str(input("Quer continuar? [S/N]: ")).strip().upper()
    contador += 1
    media += num 
    divisao = media / contador 
    if num == 1:
        maior = num
        menor = num 
    else:
        if num > maior:
            maior = num 
        if num < menor:
            menor = num
print(f"A media de todos os número digitados foi {divisao:.1f}")
print(f"O maior número digitado foi {maior}")
print(f"O menor número digitado foi {menor}")"""

#Soluçaõ do guanabara que deu o mesmo resultado que o meu
resp = "S"
soma = quant = media = maior = menor = 0
while resp in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / quant
print(f"Você digitou {quant} números e a média foi {media}")
print(f"O maior valor foi {maior} e o menor foi {menor} ")
