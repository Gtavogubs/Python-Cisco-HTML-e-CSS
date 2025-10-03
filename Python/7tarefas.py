# Gerenciador de Tarefas - Manipulação de arquivos
ARQUIVO =  "tarefas.txt"

# Função para carregar as tarefas
def carregar_tarefas():
    try:
        with open(ARQUIVO, "r", encoding= "utf-8") as file:
            return[linha.strip().split(" | ") for linha in file.readlines()]
    except FileNotFoundError:
        return []
    
# Função para salvar as tarefas
def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as file:
        for tarefa, status in tarefas:
            file.write(f"{tarefa} | {status} \n")

# Função para adicionar uma nova tarefa
def adicionar_tarefa(tarefas):
    descricao = input("digite a descrição da tarefa: ")
    tarefas.append([descricao, "⛔ Pendente"])
    salvar_tarefas(tarefas)
    print(f"Tarefa '{descricao}' adicionada com sucesso!\n")

# Função para listar todas as tarefas
def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada. \n")
    else:
        for i, (descricao, status) in enumerate(tarefas,start=1):
            print(f"{i}. {descricao} - {status}")
            print()

# Função para marcar uma tarefa concluída
def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa concluída e removida!\n")) - 1
        if 0 <= indice < len(tarefas):
            print(f"Tarefa '{tarefas[indice][0]} marcada como cluida e removida!\n")
            del tarefas[indice] #Remove a tarefa automaticamente
            salvar_tarefas(tarefas)
        else:
            print("Número inválido. \n")
    except ValueError:
        print("Por favor, digite um número válido \n")

# Funcção para excluir uma tarefa manualmente
def excluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número de tarefa que deseja excluir: ")) - 1
        if 0 <= indice  < len(tarefas):
            print(f"Tarefa '{tarefas[indice][0]}' excluida com sucesso! \n")
            del tarefas[indice]
            salvar_tarefas(tarefas)
        else:
            print("Número inválido. \n")
    except ValueError:
        print("por favor, digite um número válido \n")

# Menu Principal
def main():
    tarefas = carregar_tarefas()

    while True:
        print("1, adicionar tarefa")
        print("2, Listar tarefas")
        print("3, marcar tarefa como concluída")
        print("4, Excluir tarefa")
        print("5, Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa(tarefas)
        elif escolha == "2":
            listar_tarefas(tarefas)
        elif escolha == "3":
            concluir_tarefa(tarefas)
        elif escolha == "4":
            excluir_tarefa(tarefas)
        elif escolha == "5":
            print("Programa encerrado. Até mais!")
            break
        else:
            print("Opção inválida burrão.")

if __name__ == "__main__":
    main()            
