# Lista de filmes
movieList = ["O Senhor dos Anéis", "Harry Potter", "Star Wars", "Matrix", "O Poderoso Chefão"]

# Iterando valores de uma lista
for movie in movieList:
    print(f"Filme: {movie}")

# Quando a condição for atendida, loop será encerrado
for movie in movieList:
    if movie == "Star Wars":
        break
    print(f"Filme: {movie}")

# Quando a condição for atendida, o loop vai para a próxima iteração
for movie in movieList:
    if movie == "Star Wars":
        continue
    print(f"Filme: {movie}")

# Avaliação do filme
movieName = input("Digite o nome do filme:\n")
movieRating = float(input("Digite a avaliação do filme (0.0 a 10.0):\n"))

total = 0
for i in range(movieRating):
    note = float(input(f"Digite a nota:\n"))
    total += note

if movieRating > 0:
    media = total / movieRating
    print(f"A média de avaliações para o filme {movieName} é {media:.1f}")
else:
    print("Nenhuma avaliação foi feita.")

print(f"Média de avaliações para o filme {movieName} é {media:.2f}")


