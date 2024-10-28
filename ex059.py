from time import sleep
opçao = 0
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
while opçao != 5:    
    print('''OPCÕES:
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NÚMEROS
    [5]SAIR DO PROGRAMA''')
    opçao = int(input("Digite sua opção: "))
    if opçao == 1:
        soma = n1 + n2 
        print(f"a soma entre {n1} + {n2} é igual a {soma}")
    elif opçao == 2:
        multi = n1 * n2
        print(f"A multiplicação entre {n1} x {n2} é igual {multi}")
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"Entre {n1} e {n2}  o maior valor é {maior}")
    elif opçao == 4:
        print("Informe novos números!")
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
    elif opçao == 5:
        print("FINALIZANDO...")
    else:
        print("Opção invalida! Tente novamente.")
    sleep(2)
print("VOLTE SEMPRE!! :)")
 