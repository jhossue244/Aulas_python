distancia  = float(input("Qual a distancia da sua viagem? "))
print(f"Você está prestes a começar uam viagem de {distancia}Km")
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f"E o preço da sua passagem será de R${preço:.2f}")
