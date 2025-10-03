print("Vamos criar uma operação aritmética.")
n = int(input("Escolha o primeiro número. \n"))
n2 = int(input("Escolha o segundo número. \n"))
print("A seguir, temos 4 opções de operações para você realizar.")
print("a) Soma")
print("b) subtração ")
print("c) divisão")
print("d) multiplicação")
opcao = str(input("Qual opção você vai escolher? \n"))
if opcao == 'a':
    print(f"O Resultado da operação é: {n + n2}")
elif opcao == 'b':
    print(f"O Resultado da opreção é: {n - n2}")
elif opcao == 'c':
    print(f"O Resultado da opreção é: {n / n2}")
elif opcao == 'd':
    print(f"O Resultado da opreção é: {n * n2}")
else:
    print("Opção inválida.")