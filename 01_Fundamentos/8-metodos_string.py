movieName = "Top Gun"
movieDescription = "Um filme sobre pilotos de caça."

print(movieName.upper())  # Converte para maiúsculas
print(movieDescription.lower())  # Converte para minúsculas
print(movieName.title())  # Converte para maiúsculas as iniciais de cada palavra
print(movieDescription.capitalize())  # Converte para maiúscula a primeira letra
print(movieName.replace("Gun", "Guns"))  # Substitui parte da string
print(movieDescription.find("pilotos"))  # Encontra a posição de uma substring
print(movieDescription.count("o"))  # Conta quantas vezes a letra "o" aparece
print(movieDescription.index("pilotos"))  # Encontra a posição de uma substring (levanta erro se não encontrar)
print(movieDescription.startswith("Um"))  # Verifica se a string começa com "Um"
print(movieDescription.endswith("caça."))  # Verifica se a string termina com "caça."
print(movieDescription.split(" "))  # Divide a string em uma lista de palavras
print(movieDescription.strip())  # Remove espaços em branco do início e do fim
