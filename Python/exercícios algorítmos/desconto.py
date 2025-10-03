print("Bem-vindo ao calculador de descontos.")
preco = int(input(" Qual é o preço do produto que você quer descontar 10%?\n"))
desconto = preco * 10 / 100
total = preco - desconto
print(f"O preço do produto após o desconto é de {total} R$.\n")