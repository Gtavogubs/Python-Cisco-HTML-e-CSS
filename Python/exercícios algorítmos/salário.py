print("Você recebeu um aumento de 15 R$ nesse seu salário miserável de CLT. \n")
salario = int(input("Mas me diga qual é o seu salário para sabermos quanto aumentou. \n"))
desconto = salario * 15 / 100
total = desconto + salario
print(f"O seu salário de pobre aumentou {desconto} R$, e agora são {total} R$.")