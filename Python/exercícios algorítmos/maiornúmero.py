numeros = []
print("Esse programa tem como objetivo mostrar qual é o maior número dentre os que você escolheu.")
numeros.append(int(input("Escolha um número \n")))
numeros.append(int(input("Escolha outro número \n")))
numeros.append(int(input("Escolha o último número \n")))
print(f"Aqui estão os números que você escolheu: {numeros}")

if numeros[0] > numeros[1] and numeros[0] > numeros[2]:
    print(f"O maior número é {numeros[0]} \n")
elif numeros[1] > numeros[0] and numeros[1] > numeros[2]:
    print(f"O maior número é {numeros[2]}. \n")
else:
    print(f"O maior número é o {numeros[2]}")