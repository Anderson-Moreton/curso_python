name = input("Qual o nome do filme? ")
yearLaunch = int(input("Qual o ano de lançamento? "))
noteMovie = float(input("Qual a nota do filme? "))

print("Dados do Filme")
print("========================================")

print("Nome:", name)
print("Ano de Lançamento:", yearLaunch)
print("Nota:", noteMovie)

#Alternativa 2
print("Olá, o nome do filme é:", name, "ano do lançamento:", yearLaunch, "E a nota do filme é:", noteMovie)

#Alternativa 3  
print(f"Olá, o nome do filme é: {name}, ano do lançamento: {yearLaunch}, E a nota do filme é: {noteMovie}")