numeros = []
numeros.append(int(input("Digite qualquer número, positivo ou negativo.\n")))
numeros.append(int(input("De novo.\n")))
numeros.append(int(input("Mais uma vez.\n")))
numeros.append(int(input("Sim sim salabim.\n")))
numeros.append(int(input("Mais um.\n")))
numeros.append(int(input("Novamente.\n")))
numeros.append(int(input("One more time\n")))
numeros.append(int(input("Pode ser negativo também, você sabe né?\n")))
numeros.append(int(input("O último.\n")))
print(numeros)
for i in range(len(numeros)):
    if numeros[i] < 0:
        print(numeros[i] , "esse número é negativo. \n")
    elif numeros[i] > 0:
        print(numeros[i] , "esse número é positivo.\n")
    else:
        print("Esse número é 0.\n")


