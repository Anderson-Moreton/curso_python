# Função para exibir o nome completo
def fullName(firstName, lastName):
    print(f"Nome completo: {firstName} {lastName}")

fullName("Anderson", "Moreton")

# Função para somar dois números
def sum_numbers(a, b):
    print(f"Soma: {a + b}")

sum_numbers(5, 10)

# Função com parâmetro default
def greet(name, message="Bem-vindo ao curso de Python!"):
    print(f"{message}, {name}")

greet("Anderson")
greet("Moreton", "Olá")

# Função para avaliar filme
def rate_movie(num_ratings, movie_name):
    total = 0
    for i in range(num_ratings):
        note = float(input(f"Digite a nota para o filme:\n"))
        total += note
    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0

    print(f"Média das notas para o filme: {movie_name} e: {average:.2f}")

rate_movie(2, "John Wick")
