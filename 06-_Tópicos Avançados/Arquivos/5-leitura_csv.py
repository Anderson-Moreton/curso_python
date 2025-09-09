with open("dados/curso.csv", "r", encoding="utf-8") as file:
    for line in file:
        # linha = line.rstrip().split(",")
        # print(linha)
        linguagem, categoria = line.rstrip().split(",")
        print(f"Linguagem: {linguagem} | Categoria: {categoria}")
        