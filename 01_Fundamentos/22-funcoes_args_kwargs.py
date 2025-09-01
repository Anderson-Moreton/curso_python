"""
    *Args - Utilizamos ele quando não temos certeza de quantos argumentos queremos ter em uma função.
    Os argumentos são passados como uma Tupla.
    **Kwargs - Utilizamos ele quando queremos passar um número variável de argumentos nomeados.
    Os argumentos são passados como um dicionário.
"""

# Soma de números
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma total: {sum_total}")

sum(7)
sum(7, 3, 5, 8, 2)
sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Apresentação de Cursos
def presentation(**data):
    print("Cursos disponíveis:")
    for key, value in data.items():
        print(f"- {key}: {value}")

print("Lista de Cursos")
presentation(name="Python", duration="3 meses", level="Iniciante")
presentation(name="Java", duration="4 meses", level="Intermediário")
presentation(name="JavaScript", duration="5 meses", level="Avançado")
