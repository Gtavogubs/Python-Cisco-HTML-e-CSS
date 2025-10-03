print("Calculadora de IMC")
a = int(input("Qual é sua altura?"))
p = int(input("Qual é o seu peso?"))
i = p / (a*a)
if i < 18.5:
    print("Abaixo do peso")
elif 18.5 <= i < 24.9:
    print("Peso normal")
elif 25 <= i < 29.9:
    print("Sobrepeso")
elif 30 <= i < 34.9:
    print("Obesidade grau I")
elif 35 <= i < 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")
