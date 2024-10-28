nome = str(input("Qual é o seu nome: "))
if nome == "jhossue": 
    print("Que nome bonito!")
elif nome == "pedro" or nome == "joão" or nome == "maria":
    print("Seu nome é bem popular no brasil")
elif nome in 'amanda claudia jessica juliana':
    print("Belo nome feminino")
else: 
    print("seu nome é bem normal.")
print(f"Tenha um bom dia, {nome}!")