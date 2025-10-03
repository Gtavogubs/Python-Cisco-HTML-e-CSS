p = []
pares = [0,2,4,6,8,]
p.append(int(input("Digite um número. \n")))
p.append(int(input("Mais uma vez. \n")))
p.append(int(input("Mais uma vez. \n")))
p.append(int(input("Mais uma vez. \n")))
p.append(int(input("Mais uma vez. \n")))
p.append(int(input("Mais uma vez. \n")))
p.append(int(input("Mais uma vez. \n")))
p.append(int(input("Mais uma vez. \n")))
p.append(int(input("Mais uma vez. \n")))
p.append(int(input("Mais uma vez. \n")))
print(f"Números que você escolheu: {p}")
for i in range(len(p)):    
    u = p[i] % 10
    if u in pares:
        print(f"Seu número {p[i]} é par")
    else:
        print(f"Seu número {p[i]} é impar.")
