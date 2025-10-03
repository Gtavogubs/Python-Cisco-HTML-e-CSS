print("Bem vindo ao conversor de minutos para horas.")
minutos = float(input("Quantos minutos você deseja converter? \n"))
horas = minutos // 60
min_sobrando = minutos % 60   # Resto (ex: 150 % 60 = 30)
print(f"A conversão estipula que {minutos} minutos são {horas} horas e {min_sobrando}.")
