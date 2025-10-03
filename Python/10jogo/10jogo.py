import tkinter as tk # importa a biblioteca tkinter e a renomeia como tk para facilitar o uso
from tkinter import messagebox # importa o módulo messagebox do tkinter para exiir caixas de mensagens
from tkinter import PhotoImage # Importa a classe PhotoImage di tkinter da para exibir imagens
import random # importa o módulo random para gerar números aleatórios
import os # importa o módulo os para interagir com os sistema operacional

# Gera número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)
tentativas = 0 # Inicializia o contador de tentativas

def verificar_palpite():
    global tentativas # Permite que a função modifique a variável global tentativas
    try:
        palpite = int(entrada_palpite.get()) # Obtém o palpite do usuário e converte para inteiro
        tentativas += 1 # Incrementa o contador de tentativas

        if palpite < numero_secreto:
            resultado_label.config(text= "Muito baixo! Tente novamente.", fg= "blue") # Atualize o rótulo de resultado

        elif palpite > numero_secreto:
            resultado_label.config(text= "Muito alto! Tente novamente.", fg= "red") # Atualiza o rótulo de resultado
        else:
            messagebox.showinfo("Parabéns!" , f"Você aertou o número {numero_secreto} em {tentativas} tentativas.") # Exibe mensagem de parabéns
            janela.quit() # Fecha janela do jogo
    except ValueError:
        messagebox.showerror("Erro" , "Por favor, digite um número válido.") # Exibe mensagem de erro se o palpite não for um número válido.

# Janela Principal
janela = tk.Tk() # Cria a janela principal do jogo
janela.title("Jogo de adivinhação") # Define o título da janela
janela.geometry("700x1000") # Define o tamanho da janela

# Caminha absoluto para a imagem
caminhho_imagem = "C:/Users/1031223/Desktop/Python/10jogo/imagem.png"

# Verifica se a imagem existe
if os.path.exists(caminhho_imagem):
    tente_novamente_img = PhotoImage(file = caminhho_imagem) # Carrega a Imagem
    img_label = tk.Label(janela, image=tente_novamente_img) # Manter referência para evitar descarte da imagem
    img_label.pack(pady=10) # Adiciona o rótulo à janela
else:
    tk.Label(janela, text="[Imagem não encontrada]" , fg="red").pack(pady=10) # Exibe mensagem se a imagem não for encontrada

# Elementos da interface gráfica
tk.Label(janela, text=" Bem vindo ao jogo da adivinhação!\n Tente adivinhar o número entre 1 e 100" , fg="green", font=("Comic_Sans_MS" , 24)).pack(pady=10) # Adiciona um rótulo com instruções

entrada_palpite = tk.Entry(janela) # Cria uma caixa de entrada para o palpite do usuário
entrada_palpite.pack(pady=5) # Adiciona a caixa de entrada à

botao_verificar = tk.Button(janela, text= "Verificar Palpite" , command=verificar_palpite) # Cria um botão para verificar o palpite
botao_verificar.pack(pady=10) # Adiciona o botão à janela
resultado_label = tk.Label(janela, text="", font=("Helvetica", 10)) # Cria um rótulo para exibir o resultado do palpite
resultado_label.pack(pady=10) # Adiciona o rótulo à janelça

# Iniciar loop principal da interface gráfica
janela.mainloop()
