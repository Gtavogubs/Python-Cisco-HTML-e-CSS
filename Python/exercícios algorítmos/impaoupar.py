print("Vamos descobrir se o seu número é impar ou par.")
numero = int(input("Qual é o seu número? \n"))
ultimo_numero = numero % 10
if ultimo_numero in (1,3,5,7,9):
    print(f"O número {numero} é impar.\n")
else:
    print(f"O número {numero} é par.\n")