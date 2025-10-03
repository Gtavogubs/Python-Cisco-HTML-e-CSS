print("Vamos classificar você em relação à sua idade.")
i = int(input("Qual é a sua idade? \n"))
if i <= 12:
    print("Você é uma criança.")
elif i <= 17:
    print("Você é um adolescente.")
elif i <= 59:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")