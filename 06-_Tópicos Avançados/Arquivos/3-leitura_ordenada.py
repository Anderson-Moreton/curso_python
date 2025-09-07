names = []
with open("dados/names.txt", "r", encoding="utf-8") as file:
    for line in file:
        names.append(line.strip())
names.sort()
for name in names:
    print(f"Olá, {name}")
