movieName = "Top Gun"
#String[início:fim] - Indíce começa em 0 | Indíce termina em 1 a menos que o fim seja omitido

# 1 - Buscar toda a string a partir do índice 0
print(movieName[0:])  # "Top Gun"

# 2 - Buscar a partir do índice 4
print(movieName[4:])  # "Gun"

# 3 - Buscar até o índice 3
print(movieName[:3])  # "Top"

# 4 - Buscar a string inteira
print(movieName[:])   # "Top Gun"

# 5 - Buscar com índices negativos
print(movieName[-4:]) # "Gun"

"""
String[inicio:fim:passo]
Indíce começa em 0 | Indíce termina em 1 a menos que o fim seja omitido
passo - determina o incremento.Por padrão esse número é 1
"""

# 6 - Buscar toda a string de 2 em 2 caracteres
print(movieName[::2])  # "TpGn"

# 7 - Buscar toda a string de trás para frente
print(movieName[::-1]) # "nuG poT"

# 8 - Buscar toda a string nos indices impares
print(movieName[1::2]) # "o n"  