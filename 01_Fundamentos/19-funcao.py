def welcome():
    print("Welcome to Python Course!")

welcome()

# Função para calcular a média de notas
def calculate_average():
    num_ratings = int(input("Digite o número de avaliações que deseja fazer:\n "))
    total = 0
    for i in range(num_ratings):
        note = float(input(f"Digite a nota {i + 1}: "))
        total += note
    
    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0

print(f"A média das notas é: {calculate_average():.2f}")

# Função para cadastrar um filme

def create_movie():
    movie_name = input("Digite o nome do filme: ")
    movie_year = input("Digite o ano de lançamento: ")
    print(f"Filme cadastrado: {movie_name} ({movie_year})")

create_movie()  
create_movie()