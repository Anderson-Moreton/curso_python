movieName = "O Senhor dos Anéis"
movieName2 = "O senhor dos Anéis"
print(movieName == movieName2)  # False - Case Sensitive

movieDescription = """
    Uma épica 
    jornada pela 
    Terra Média.
"""
print(movieName)
# 1 - Multiplicação de Strings
line = "="
print(line * 50)
print(movieDescription)

# 2 - Procurar por uma palavra dentro de um texto
print("Top" in movieName) # False
print("Terra" in movieDescription)  # True
