firstName = "Anderson"
lastName = "Moreton"

fullName = f"{lastName}, {firstName}"

print(fullName)

# Inverter ordem do texto
text = "Python é muito interessante"
words = text.split()
invertedText = " ".join(words[::-1])
print(invertedText)

text1 = "arara"
text2 = "carro"

# Remove espaço e deixa nome em minusculo
text1 = text1.strip().lower()
text2 = text2.strip().lower()   

# Verifica se text1 é um palíndromo
if text1 == text1[::-1]:
    print(f"{text1} é um palíndromo.")
else:
    print(f"{text1} não é um palíndromo.")

# Verifica se text2 é um palíndromo
if text2 == text2[::-1]:
    print(f"{text2} é um palíndromo.")
else:
    print(f"{text2} não é um palíndromo.")
