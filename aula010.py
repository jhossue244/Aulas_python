n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
m = (n1 + n2)/2
print("A sua media é {:.1f}".format(m))
if m >= 6.0: 
    print("A sua media foi boa! PARABENS!!!")
else:
    print("A sua media foi pessima! ESTUDE MAIS!!!!")