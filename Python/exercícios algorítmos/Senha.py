def login():
    s = "senac123"
    tentativas = 0
    max_tentativas = 3

    while tentativas < max_tentativas:
        palpite = input("Qual é a sua senha?")
        if palpite == s:
            print("Login efetuado com sucesso.")
            break
        else:
            tentativas += 1
            if tentativas < max_tentativas:
                print("Errou!")
            else:
                print("Acesso negado.")
    print(f"Tentativas: {tentativas}")
   