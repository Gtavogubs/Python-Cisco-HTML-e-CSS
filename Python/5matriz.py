import random # Importa a biblioteca random para gerar elementos aleatórios

# Gerar matrix 3x3 com nomes de frutas
frutas = ["Maçã","Banana","Uva","Laranja","Pera","Manga","Abacaxi","Melancia","Morango"] # Lista com nomes de frutas
matriz = [] # Cria uma lista vazia para armazenar a matriz
for i in range(3): # Loop para criar 3 linhas na matriz
    vetor = random.sample(frutas, 3)
    # Seleciona aleatoriamente 3 frutas da lista na matriz
    matriz.append(vetor)

# Exibir a matriz
print("Matriz gerada com frutas:") # Mensagem pra exibir 

# O i é uma variável de controle do laço for
# A função range(3) gera os números 0, 1 e 2.
# Assim, o laço for será executado 3 vezes, uma para cada número. 
# A cada repetição, o i assume um desses valores:
# Primeira repetição: i = 0
# Segunda repetiçãp:  i = 1
# Terceira repetição  i = 2
for linha in matriz: # Loop para percorrer cada linha da matriz
    print(linha) # Exibe cada linha da matriz

# Verificar se uma fruta está na matriz
fruta = input("\nDigite o nome de uma fruta para buscar na matriz: ") # Solicita uma fruta ao usuário.

encontrado = False # Inicializa uma variável para verificar se a fruta foi encontrada
for i, linha in enumerate(matriz): # Loop para percorrer cada linha com seu índice
    if fruta in linha: # Verifica se a fruta está na linha atual 
        print(f"A fruta{fruta} está na posição: Linha {i + 1}, coluna {linha.index(fruta + 1)}") # Exibe a pocisão da fruta encontrada
        encontrado = True # Marca que a fruta foi encontrada

if not encontrado: # Verifica se a fruta não foi encontrda
    print(f"A fruta {fruta} não foi encontrada na matriz.") # Mensagem caso a fruta não seja encontrada na matriz.

     