import random # Importa a biblioteca random para escolher uma palavra aleatória

# Lista de palavras possíveis para o jogo
palavras = ["salame" , "abacate" , "paralelepipedo" , "afogados" , "mandioca" , "cruzeiro"] 

# Escolha uma palavra aleatória da lista
palavra = random.choice(palavras)

#  Cria uma lista com "_" para caa letra da palavra (será mostrada ao jogador)
letras_descobertas = ["_"] * len(palavra)

# Lista que vai guardar as letras erradas que o jogador digitar
letras_erradas = []

# Define o número máximo de tentativas (erros permitidos)
tentativas = 6

# Mensagem inicial do jogo
print("🎲 Bem-vindo ao jogo da Forca!")
print("Adivinhe a palavra letra por letra.")

# Laaço que repete o número de tentativas permitidas
for tentativa in range(1 , tentativas + 1):
    # Mostra a palavra atual com as letras descobertas até o momento
    print("\nPalavra: " , " ".join(letras_descobertas))

    # Mostra as letras que o jogador já errou
    print("Letras erradas:" , "".join(letras_erradas))

    # Pede ao jogador para digiar uma letra
    letra = input(f"Tentativa {tentativa} / {tentativas} - Digite uma letra: ").lower()

    # Verifica se a letra digitada está na palavra
    if letra in palavra:
        # Substitui os "_" pela letra correta nas posições correspondentes
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_descobertas[i] = letra
        print("🫡 Letra correta!")
    else:
        # Se a lista estiver errada, adiciona na lista de letras erradas
        letras_erradas.append(letra)
        print("⛔ Letra incorreta.")
    
    # Verifica se todas as letras foram descobert5as
    if "_" not in letras_descobertas:
        print("\n Parabéns! Você acertou a palavra:" , palavra)
        break
else:
    # Se o jogador não acertar após todas as tentativas, perde o jogo
    print("\n Você perdeu! A palavra era: " , palavra)