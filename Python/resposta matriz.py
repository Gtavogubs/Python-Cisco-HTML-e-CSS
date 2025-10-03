matriz = []
for l in range(3):
    linha = []
    for c in range(3):
        valor = int(input(f"Digite o valor para inserir na matriz[{l}][{c}]:"))
        linha.append(valor)
    matriz.append(linha)
print("Matriz preenchida.")
for linha in matriz:
    print(linha)
    