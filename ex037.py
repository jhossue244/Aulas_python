from time import sleep

num = int(input("\033[33mDigite um numero inteiro: \033[m"))
print("\033[0;7;37mESCOLHA UMA BASE DE CONVERSÃO\033[m")
print("\033[32m1 para Binário\\033[m")
print("\033[36m2 para Octal\033[m")
print("\033[35m3 para hexadecimal\033[m")
escolha =int(input("digite a opção (1, 2 ou 3): "))
print("CALCULANDO...")
sleep(3)
if escolha == 1 :
    print(f"O binario de {num} é igual a {bin(num)[2:]}")
elif escolha == 2 :
    print(f"o octal de {num} é igual a {oct(num )[2:]}")
elif escolha == 3 :
    print(f"o hexadecimal de {num} é igual a {hex(num)[2:]}")
else:
    print("OPÇÃO INVALIDA!TENTE NOVAMENTE.")
