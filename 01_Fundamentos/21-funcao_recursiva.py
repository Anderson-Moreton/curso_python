# Função recursiva para calcular fatorial
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
number = int(input("Digite um número para calcular o fatorial:\n"))
print(f"Fatorial de {number}: {factorial(number)}")

#  Soma total de um número
def total_sum(num):
    if num == 1:
        return 1 
    else:
        return num + total_sum(num-1)
number = int(input("Digite um número para calcular a soma total:\n"))
print(f"Soma total de {number}: {total_sum(number)}")