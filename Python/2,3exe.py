print("Vamos converter de Fahrenheit para Celsius")
temperatura = float(input("Digite a temperatura em Fahrenheit para convertermos em Celsius: ")) # Solicita ao usuário um número e converte para float 

conversao = (temperatura - 32) * 5 / 9 
print(f"O Resultado da conversão é: {conversao}F°")