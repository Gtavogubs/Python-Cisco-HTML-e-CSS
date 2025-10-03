# O While em Phyton é uma estrutura de repetição (loop) que executa um bloco de código enquanto uma condição for verdadeira.

import random # Importa a biblioteca random para gerar números aleatórios

# Gera um número aleatóro entre 1 e 100
numero_secreto = random.randint(1, 100)

# Inicializa a variável para contar as tentativas
tentativas = 0

# Inicializa a variável de palpite do jogador
palpite = 0

# Exibe uma mensagem inicial para o jogador
print(" Bem vindo ao jogo de adivinhação!")
print("😊 Tente adivinhar o número entre 1 e 100")

# Inicia um loop que continua até o jogador acertar o número
while palpite != numero_secreto:
    # Solicita ao usuário um número e converte para o inteiro
    palpite = int(input("Digite seu palpite: "))
    # Incrementa o contator de tentativas
    tentativas += 1

    # Verifica se o palpite é o menor que o número secreto
    if palpite < numero_secreto:
        print(" Muito baixo! Tente novamente.")  # Dá uma dica ao jogador.
    # Verifica se o palpite é maior que o número secreto
    elif palpite > numero_secreto:
        print(" Muito Alto! Tente novamente.") # Dá uma dica ao jogador

# Sai do loop quando o palpite for igual ao número secreto
print(f" Parabéns, você acertou o número {numero_secreto} em {tentativas} tentativas.")