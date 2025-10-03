print("Digite o número 0, ou não vamos parar de encher seu saco.")
n = []
tentativas = 0
n.append(int(input("Digite um número de 0 a 10: ")))
while True:
    if n[-1] == 0:
       print("Agora vamos calcular a média dos seus números.")
       break
    else:
        n.append(int(input("Digite mais um número de 0 a 10: \n")))
        print(f"{n} Até agora esses são os números que você escolheu.")
        tentativas +=1
m = sum(n)/2
print(f"A média do conjunto é {m} \n")

        