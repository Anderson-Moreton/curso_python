name = input("Digite o nome do aluno: \n")

# # Implementação 1
# file = open("dados/names.txt", "a", encoding="utf-8")
# file.write(f"{name}\n")
# file.close()

# Implementação 2
with open("dados/names.txt", "a", encoding="utf-8") as file:
    file.write(f"{name}\n")

