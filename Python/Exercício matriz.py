import random
planetas = ["Vênus" , "Marte" , "Terra" , "Urano" , "Saturno" , "Júpiter" , "Tatuíne" , "Estrela da Morte"]
matriz = []
for i in range(3):
    vetor = random.sample(planetas, 3)
    matriz.append(vetor)
print("Planetas do sistema solar... e alguns intrusos:")
for linha in matriz:
    print(linha)
planetas = input("\nDigite o nome de um planeta para checarmos na matriz: ")
encontrado = False
for i, linha in enumerate(matriz):
    if planetas in linha:
     print(f"O Planeta{planetas} está na posição: Linha {i+1}, coluna {linha.index(planetas +1)}")
encontrado = True
if not encontrado:
    print(f"O planeta{planetas} não foi encontrado na matriz.")
