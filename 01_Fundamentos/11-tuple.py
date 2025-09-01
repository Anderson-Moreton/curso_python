filmsTuple = ("Inception", "Harry Potter", "The Dark Knight",
              "Interstellar", "The Matrix")
print(type(filmsTuple))

# Buscar os dois primeiros filmes
print(filmsTuple[:2])

# Buscar o ultimo item da tuple
print(filmsTuple[-1])

# Buscar os filmes até uma determinada posição
print(filmsTuple[:3])

# Buscar os filmes a partir de uma determinada posição
print(filmsTuple[2:])

# Recuperar um item da tuple pelo nome
print(filmsTuple.index("Interstellar"))
