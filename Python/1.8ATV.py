# Sistema de login com até 3 tentativas
usuario_correto = "julio"
senha_correta = "1234"

tentativas = 3

while tentativas > 0:
    print("\n LOGIN")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login realizado com sucesso!")
        break
    else:
        tentativas -= 1
        print(f"Usuário ou senha incorretos. Tentativas restantes: {tentativas}")

if tentativas == 0:
    print("\nConta bloqueada. Número de tentativas excedido.")
    