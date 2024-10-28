from time import sleep

num = int(input("Digite um número: "))
print("\033[7;37mANALISANDO O ANTECESSOR E O SUCESSOR....\033[m")
sleep(3)
print(f"Analisando o valor \033[1;36m{num}\033[m, seu Antecessor é \033[1;31m{num - 1}\033[m e o Sucessor é \033[1;31m{num + 1}\033[m ")
