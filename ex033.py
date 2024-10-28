a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))
#verificando que  é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificando o maior
maior = a 
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f"o menor valor digitado foi {menor}")
print(f"O valor maior digitado foi {maior}")