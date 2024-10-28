print("\033[1;33m-=\033[m"*20)
print("analisador de triangulo".upper())
print("\033[1;33m-=\033[m"*20)
r1 = float(input("primeiro segmento: "))
r2 = float(input("segundo segmento: "))
r3 = float(input("terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("os segmentos acima PODEM FORMAR um triangulo")
else: 
    print("Os segementos acima NÃO PODEM FORMAR um triangulo")