print("-=" * 10)
print("EMPRETISMO BANCARIO")
print("-=" * 10)
casa= float(input("Qual o valor da casa: "))
salario = float(input("Qual o valor do seu salrio: "))
anos  = int(input("Em quantos anos você ira pagar a casa: "))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print(f"Para pagar uma casa de R${casa:.2f} em {anos} anos ", end="")
print(f"a prestação será de R${prestação}")
if prestação <= minimo:
    print("Emprestimo pode se CONCEDIDO.")
else:
    print("Emprestimo NEGADO.")