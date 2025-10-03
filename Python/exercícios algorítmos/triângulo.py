print("Quero três lados de um triângulo. Vou te falar como ele é.")
b = int(input("Qual é a área de base? \n"))
l = int(input("Qual é o primeiro lado? \n"))
l2 = int(input("Qual é o segundo lado? \n"))
if b == l and b == l2:
    print("Esse é um triângulo equilátero.")
elif l == l2 or l == b or b == l2:
    print("Esse é um triângulo isóceles")
else:
    print("Esse é um triângulo escaleno.")