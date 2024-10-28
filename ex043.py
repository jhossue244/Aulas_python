#CALCUALNDO O IMC DE UMA PESSOA


print("\033[1;33m=\033[m" * 15)
print("CALCULE SEU IMC")
print("\033[1;33m=\033[m" * 15)
peso = float(input("Digite o seu peso? (Kg): "))
altura = float(input("Digite a sua altura? (m): "))
imc = peso / (altura ** 2)
print(f"O seu IMC é {imc:.1f}")
if imc < 18.5:
    print("Você está ABAIXO DO RECOMENDADO ! Procure um nutricionista para respver isso.")
elif 18.5 <= imc < 25:
    print("Você está com o PESO SAUDÁVEL! continue desse jeito!")
elif 25 <= imc < 30:
    print("Você está com SOBREPESO! Procure um nutricionista")
elif 30 <= imc < 40:
    print("Você está com OBECIDADE! Procure um nutricionitas.")
elif imc > 40: 
    print("VOCÊ ESTÁ COM OBECIDADE MÓRBIDA! PROCURE UM NUTRICIONISTA URGENTE!!!!!")
