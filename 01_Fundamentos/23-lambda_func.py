# Função de potência de um número
def power(num): return num ** 2

# Função que verifica se um número é par


def is_even(num): return num % 2 == 0

# Função que divide um número por outro


def divide(x, y): return x / y if y != 0 else "Divisão por zero não permitida"

# Função que inverte uma string


def reverse_string(s): return s[::-1]


print(power(5))            # Saída: 25
print(is_even(10))         # Saída: True
print(divide(10, 2))      # Saída: 5.0
print(divide(10, 0))      # Saída: Divisão por zero não permitida
print(reverse_string("Python"))  # Saída: nohtyP

# Funcionalidades relacionadas aos filmes
movie_list = ["Os Vingadores", "Matrix", "O Senhor dos Anéis", "Star Wars"]
ratings = {
    "Os Vingadores": [8.0, 9.0, 7.5],
    "Matrix": [9.5, 9.0, 8.5],
    "O Senhor dos Anéis": [9.0, 9.5, 9.5],
    "Star Wars": [8.0, 8.5, 8.0]
}

# Função para calcular a média de avaliações de um filme


def average_rating(movie_name): return sum(
    ratings[movie_name]) / len(ratings[movie_name])

# Função que verifica se um filme está na lista


def check_movie(movie_name): return movie_name in movie_list

# Função para recomendar um filme com base na avaliação média


def recommend_movie(
): return f"Recomendamos '{max(ratings, key=average_rating)}' com uma avaliação média de {average_rating(max(ratings, key=average_rating)):.2f}"


print(
    f"Média de avaliação do filme The Matrix: {average_rating('Matrix'):.2f}")
print(f"O filme 'Inception' está na lista? {check_movie('Inception')}")
print(f"Recomendação de filme: {recommend_movie()}")
