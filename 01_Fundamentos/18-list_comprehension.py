# Listando valores de 0 a 10 que sejam menores do que 4

listNumbers= [i for i in range(10) if i < 4]
print(listNumbers)

# Lista de filmes
movieList = ["O Senhor dos Anéis", "Harry Potter", "Star Wars", "Matrix", "O Poderoso Chefão"]

# Filmes que possuem a letra "e" no titulo
moviesWithE = [movie for movie in movieList if "e" in movie.lower()]
print(moviesWithE)

# Filmes que eu assisti
movieWatched = [movie for movie in movieList if movie != "Star Wars"]
print(movieWatched) 

# Encontrando um filme pelo nome
while True:
    movieName = input("Digite o nome do filme que deseja encontrar: (ou sair para encerrar):\n")
    if movieName.lower() == "sair":
        print("Programa encerrado.")
        break
    foundMovies = [movie for movie in movieList if movieName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filmes encontrados: {foundMovies}")
        break
    else:
        print(f"Nenhum filme encontrado com o nome '{movieName}'. Tente novamente.")

