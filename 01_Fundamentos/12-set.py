filmsSet = {"Inception", 
            "Interstellar", 
            "Dunkirk", 
            "Tenet", 
            "Oppenheimer"}

print(filmsSet)

# Tamanho do set
print(len(filmsSet))

# True e 1 são considerados o mesmo valor
exempleSet = {"Titanic", True, 1, 8.7}
print(exempleSet)

# Adicionar item a outro set
filmsSet.update(exempleSet)
print(filmsSet)

# Remover item de um set
filmsSet.remove("Titanic")
filmsSet.remove(8.7)
print(filmsSet)

