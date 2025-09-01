filmList = ["Inception", "Harry Potter", "The Dark Knight", "Interstellar", "The Matrix"]

# Tamanho da lista
print(len(filmList))

# Recuperar um item da lista
print(filmList.index("Interstellar"))

# Adicionando um filme ao final da lista
filmList.append("O Senhor dos Anéis")
print(filmList)

# Ordenar a lista
filmList.sort()
print(filmList)

# Copiar os itens de uma lista para outra
filmList2 = filmList.copy()
print(filmList2)

# Removendo um filme
filmList.remove("Harry Potter")
print(filmList)

# Remover todos os itens da lista
filmList.clear()
print(filmList)
