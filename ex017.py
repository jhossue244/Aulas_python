'''Catetos e Hipotenusa'''
from math import hypot
co = float(input("digite o cateto oposto: "))
ca = float(input("digite po cateto adjcente: "))
hi = hypot(co, ca)
print("A medida vai ser {:.2f}".format(hi))
