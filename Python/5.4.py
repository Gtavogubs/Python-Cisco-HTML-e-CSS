# Criando uma lista com nomes de frutas
frutas = ["Maçã" , "Banana" , "Uva" , "Laranja"]

# Exibindo a lista completa
print("Lista de frutas:", frutas)


# Exemplo 2
# Lista com números inteiros
numeros = [10, 20, 30, 40, 50]

# Soma de todos os elementos da lista
soma = sum(numeros)

# Exibindo o resultado
print("A Soma dos números é:" , soma)

# Exemplo 3
# Lista Vazia
nomes = []

# Adicionando nomes à lista
nomes.append("Ana")
nomes.append("Carlos")
nomes.append("Beatriz")

# Mostrando os nomes inseridos
print("Nomes na lista:", nomes)


# Exemplo 4
# Lista com cores
cores = ["Azul" , "Verde" , "Amarelo" , "Vermelho"]

# Acessando o primeiro elemento (índice 0)
print("A primeira cor é:", cores[0])

# Acessando o último elemento (índice -1)
print("A última cor é:", cores[-1])

# Exemplo 5
# Lista vazia para armazenar os pares
pares = []

# Laço que vai de 2 até 20, de 2 em 2
for i in range(2 , 21 , 2):
    pares.append(i) # Adiciona o número na lista

# mostrando a lista de pares
print("Números pares de 2 a 20:" , pares)