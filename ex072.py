sequencia = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

#Minha solução

while True:
    num  = int(input("Digte um número entre 0 e 20: "))
    while num < 0 or num > 20:
        num = int(input("Tente novamente. Digite um número entre 0 e 20: "))
    print(f"Você digitou o número {sequencia[num]}")
    resp = str(input("Quer continuar? [S/N]  ")).strip().upper()[0]
    if resp == "N":
        break

    


#Solução do guanabara 
'''while True:
    while True:
        num = int(input("Digite um número entre 0 e 20: "))
        if  0<= num <= 20:
            break
        print("Tente novamente!", end = "")

    print(f"Voce digitou o número {sequencia[num]}")
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break'''