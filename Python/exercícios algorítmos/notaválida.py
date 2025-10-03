print("Você deve escolher a nota correta de um a 10.")
notas = [1,2,3,4,5,6,7,9,10]
ncerta = 8
tentativas = 0
while True:
    t = int(input("Qual é a nota? \n"))
    if t == ncerta:
        print("Você acertou, parabéns.")
        break
    elif t in notas:
        print("Tente novamente.")
        tentativas += 1
    else:
        print("Valor inválido.")
        tentativas += 1
        

