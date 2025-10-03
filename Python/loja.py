ARQUIVO = "loja.txt"
def carregar_produtos():
    try:
        with open(ARQUIVO, "r", encoding= "utf-8") as file:
            return[linha.strip().split(" | ") for linha in file.readlines()]
    except FileNotFoundError:
        return []        

def salvar_produtos(produtos):
    with open(ARQUIVO, "w", encoding="utf-8") as file:
        for produto, status in produtos:
            file.write(f"{produto} | {status} \n")
         
def carrinho(produtos):
    descricao = input("Digite o produto desejado: ")
    produtos.append([descricao, "🫡 Analisando produto"])
    salvar_produtos(produtos)
    print(f"Produto '{descricao}'adicionado ao carrinho.\n")

def allproducts(produtos):
    if not produtos:
        print("Seu produto não está no carrinho. \n")
    else:
        for i, (descricao, status) in enumerate(produtos, start=1):
            print(f"{i}. {descricao} - {status}")
            print()

def concluir_compra(produtos):
    allproducts(produtos)
    try:
        indice = int(input("Digite o número do produto do produto comprado. \n")) - 1
        if 0 <= indice < len(produtos):
            print(f" Produto '{produtos[indice][0]}' comprado com sucesso! \n")
            del produtos[indice]
            salvar_produtos(produtos)
        else:
            print("Nú")





    
