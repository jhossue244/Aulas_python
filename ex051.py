print("=" * 26)
print("    10 TERMOS DE UMA PA")
print("=" * 26)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(c, end = " ")
print("ACABOU")
