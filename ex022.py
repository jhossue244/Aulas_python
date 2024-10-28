''''analisador de texto'''

nome = str(input("digite seu nome completo: ")).strip()
print("ANALISANDO SEU NOME...")
print("Seu nome em letras maiusculas {}".format(nome.upper()))
print("Seu nome em letras minusculas é {}".format(nome.lower()))
print("Seu nome ao todo tem {} letras".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))
