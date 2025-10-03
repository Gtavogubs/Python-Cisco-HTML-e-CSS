print("Bom dia, vamos calcular o seu IMC para saber se você é uma pessoa saudável.")
print("Primeiro, sabemos que o IMC é feito pelo peso x altura². Dependendo do número sobressalente saberemos se você está saudável.")
peso = float(input("Qual é o seu peso? \n"))
altura = float(input("Interessante, e qual é a sua altura? \n"))
imc = peso / (altura * altura)
if imc <= 18.50:
    print(f"Seu IMC é de {imc}, o que quer dizer que você está abaixo do peso. ")
elif imc <= 24.90:
    print(f"Você está com um IMC de {imc} saudável. Pratique exercícios e beba água.")
elif imc <= 29.90:
    print(f"Seu IMC é {imc}. Você está com sobrepeso, talvez seja melhor fazer um regime.")
elif imc <= 34.90:
    print(f"Seu IMC é de {imc}, que categoriza obesidade grau 1. Você deveria buscar um nutricionista.")
elif imc <= 39.90:
    print(f"Irmão teu IMC é de {imc}, se você não parar de comer seu coração é quem vai parar.")
else:
    print(f"PARA DE COMER SEU IMENSO")