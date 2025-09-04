filmInception = {
    "title": "Inception",
    "year": 2010,
    "rating": 8.8,
    "genre": ["Action", "Thriller", "Sci-fi"]
}

print(filmInception)
print(len(filmInception))
print(type(filmInception))

# Recuperar elemento do dicionário
print(filmInception["genre"])
print(filmInception.get("imdbRating"))

#Buscar apenas as chaves
print(filmInception.keys())

# Buscar apenas os valores
print(filmInception.values())       

# Buscar apenas os itens
print(filmInception.items())

# Adicionar itens
filmInception["director"] = "Christopher Nolan"
print(filmInception)

# Atualizar itens
filmInception.update({"rating": 9.0})
print(filmInception)

# Remover itens
filmInception.pop("imdbRating")
print(filmInception)