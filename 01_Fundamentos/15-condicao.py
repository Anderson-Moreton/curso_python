# Informações sobre o filme

name = input("Digite o nome do filme:\n")
year = int(input("Digite o ano de lançamento do filme:\n"))
rating = float(input("Digite a avaliação do filme (0.0 a 10.0):\n"))

# Verifica se filme é recomendado
if rating >= 7.0 and year >= 2015:
    print(f"O filme '{name}' ({year}) é recomendado.")
else:
    print(f"O filme '{name}' ({year}) não é recomendado.")

num1 = float(input("Digite o primeiro número:\n"))
num2 = float(input("Digite o segundo número:\n"))
operation = input("Digite a operação (+, -, *, /):\n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Erro: Divisão por zero não é permitida."
else:
    result = "Operação inválida."

print(f"O resultado da operação é: {result}")
