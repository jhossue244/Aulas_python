#minha soluçaõ que deu o mesmo resultado
"""num = cont = soma = 0
while num != 999:
    num = int(input("Digite um número: "))
    if num != 999:
        cont += 1
        soma += num
print(f"Foram digitados {cont} números desconsiderando o 999")
print(f"A soma desse números é foi {soma}")"""

#Solução do guanabara que deu o mesmo resulatado tbm
num = cont = soma = 0
num = int(input("Digite um número [999 para parar]: "))
while num != 999:
    cont += 1
    soma += num
    num = int(input("Digite um número [999 para parar]: "))
print(f"Você digitou {cont} números e a soma entre eles foi {soma}")
