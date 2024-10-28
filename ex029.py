vel = float(input("Digite a velocidade do Carro: "))
multa = (vel - 80)*7
if vel > 80:
    print("Você foi multado por ultrapassar a velocidade permitada!")
    print("TOTAL A PAGAR: {}".format(multa))
else:
    print("Você está dentro da velocidade e")