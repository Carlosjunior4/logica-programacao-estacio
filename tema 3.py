# Tema 3: Calculadora de IMC
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura ** 2)

print(f"Seu IMC é {imc:.2f}")
if imc < 18.5: print("Abaixo do peso")
elif imc < 25: print("Peso ideal")
else: print("Sobrepeso/Obesidade")