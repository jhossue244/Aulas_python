times  = ("corinthians", "Palmeiras", "Santos", "Grêmio", 
"Cruzeiro", "Flamengo", "Vasco", "Chapecoense",
"Atlético", "Botafogo", "Atlético-PR", "Bahia", 
"São paulo", "Fluminense", "Sport Recife", 
"EC vitória", "coritiba", "Avaí", "ponte preta",
"Atlético-GO")
print("-=" * 15)
print(f"Os 5 primeiros são: {times[0:5]}")
print("-=" * 15)
print(f"Os 4 ultimos são: {times[-4:]}")
print("-=" * 15)
print(f"Times em ordem alfabética: {sorted(times)}")
print("-=" * 15) 
print(f"Chapecoense está na {times.index('Chapecoense') + 1} posição ")
