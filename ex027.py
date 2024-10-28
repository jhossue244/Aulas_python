'''primeiro e ultimo nome de uma pessoa '''
n = str(input("Digite seu nome completo: "))
nome = n.split()
print("O seu primeiro nome é {}".format(nome[0]))
print("Seu ultimo nome é {}".format(nome[len(nome)-1]))
