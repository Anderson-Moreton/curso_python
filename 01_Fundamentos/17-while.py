# Lista de filmes
movieList = ["O Senhor dos Anéis", "Harry Potter", "Star Wars", "Matrix", "O Poderoso Chefão"]

# Iterando valores de uma lista com while
index = 0
while index < len(movieList):
    print(f"Filme: {movieList[index]}")
    index += 1

# Quando a condição for atendida, o loop será encerrado
index = 0
while index < len(movieList):
    if movieList[index] == "Star Wars":
        break
    print(f"Filme: {movieList[index]}")
    index += 1

# Quando a condição for atendida, o loop vai para a próxima iteração
index = 0
while index < len(movieList):
    if movieList[index] == "Star Wars":
        index += 1
        continue
    print(f"Filme: {movieList[index]}")
    index += 1

# Avaliação do filme com while
movieName = input("Digite o nome do filme:\n")
movieRating = float(input("Digite a avaliação do filme (0.0 a 10.0):\n"))

total = 0
count = 0

while count < movieRating:
    note = float(input(f"Digite a nota:\n"))
    total += note
    count += 1

if movieRating > 0:
    media = total / movieRating
    print(f"A média de avaliações para o filme {movieName} é {media:.1f}")
else:
    print("Nenhuma avaliação foi feita.")

print(f"Média de avaliações para o filme {movieName} é {media:.2f}")
