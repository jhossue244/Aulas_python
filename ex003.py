from time import sleep
cores = {"limpa":"\033[m",
         "azul":"\033[34m",
         "verde":"\033[32m"}
n1 = int(input("\033[7;37mDigite um valor:\033[m "))
n2 = int(input("\033[7;37mDigite outro valor:\033[m "))
s = (n1 + n2)
print("\033[7;31mCALCULANDO...\033[m")
sleep(3)
print(f"a soma entre {cores['verde']}{n1}{cores['limpa']} e {cores['verde']}{n2}{cores['limpa']} é igual a {cores['azul']}{s}{cores['limpa']}!")