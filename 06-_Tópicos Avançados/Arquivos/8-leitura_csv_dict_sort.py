cursos = []

with open("dados/curso.csv", "r", encoding="utf-8") as file:
    for line in file:
        linguagem, categoria = line.rstrip().split(",")
        curso = {}
        curso["language"] = linguagem
        curso["category"] = categoria
        cursos.append(curso)

# def get_language(course):
#     return course["language"]

# def get_category(course):
#     return course["category"]



for curso in sorted(cursos, key=lambda curso: curso["language"]):
    print(f"{curso['language']} - {curso['category']}")

