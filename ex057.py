sexo = ""
while sexo not in "FM":
    sexo = str(input("Informe o seu sexo [F/M]: ")).strip().upper()[0]
    if sexo not in ["F", "M"]:
        print("Essa opção é invalida! Digite novamente! ")
print(f"Sexo registrado:{sexo}")
