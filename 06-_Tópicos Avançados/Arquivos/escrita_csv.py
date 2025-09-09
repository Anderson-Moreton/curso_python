import csv

linguagem = input("Informe a linguagem: \n")
categoria = input("Informe a categoria: \n")

with open("dados/curso.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerow([linguagem, categoria])
