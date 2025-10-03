print("Esse código te mostra um número e sua forma fatorial.")
n = int(input("Qual é o número a ser transformado em fatorial?"))
fatorial = 1
for i in range(1, n+1):
    fatorial *= i
print(f"O fatorial de {n} é {fatorial}")