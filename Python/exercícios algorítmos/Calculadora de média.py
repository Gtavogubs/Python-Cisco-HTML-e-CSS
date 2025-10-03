print("Vamos calcular a média de três das suas matérias.")
g = int(input("Qual é sua nota em Geografia?\n"))
c = int(input("Qual é sua nota em Ciências?\n"))
m = int(input("Qual é sua nota em Matemática?\n"))
media = (g + c + m) // 2
print(f"A média das suas matérias é de: {media}")
if media < 7:
    print("Sua nota final ficou abaixo da média, você foi reprovado.")
else:
    print("Você passou de ano!")