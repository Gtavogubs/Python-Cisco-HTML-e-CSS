# Tipos de dados em Python
# 1. Tipo None

nada = None
print("NoneType:", nada , type(nada))

#2. Tipo Booleano
verdadeiro = True
falso = False 
print("Boolean:" , verdadeiro , type(verdadeiro))

# 3. Tipos Numéricos
inteiro = 10
ponto_flutuante = 3.14
numero_complexo = 2 + 3j
print("int:" , inteiro , type(inteiro))
print("Float:" , ponto_flutuante , type(ponto_flutuante))
print("Complex:" , numero_complexo , type(numero_complexo))

# 4. Tipo String
texto = "Olá, Mundo!"
print("String" , texto , type(texto))

# 5. Tipo Lista (List)
lista = [1, 2, 3, "quatro" , 5.0]
print("List:" , lista , type(lista))

# 6. Tipo Tupla (tuple)
tupla = (1, 2, 3)
print("Tuple:" , tupla , type(tupla))

# 7. Tipo Conjusto (set)
conjunto =  {1, 2, 3, 2}
print("Set:" , conjunto, type(conjunto)) # elementos duplicados são removidos

# 8. Tipo Dicionário (dict)
dicionario = {"nome" : "João" , "idade" : 30}
print("Dict:" , dicionario , type(dicionario))