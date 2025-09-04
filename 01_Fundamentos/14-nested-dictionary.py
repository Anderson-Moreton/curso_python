import pprint

filmDict = {
    "inception":{
        "year": 2010,
        "rating": 8.8,
        "genre": ["Action", "Thriller", "Sci-fi"]
    },
    "interstellar": {
        "year": 2014,
        "rating": 8.6,
        "genre": ["Adventure", "Drama", "Sci-fi"]
    },
    "the_dark_knight": {
        "year": 2008,
        "rating": 9.0,
        "genre": ["Action", "Crime", "Drama"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmDict)

# Buscar uma informação dentro do dicionário
pp.pprint(filmDict["inception"]["genre"])

# Adicionar novo item
filmDict["inception"]["duration"] = 148
pp.pprint(filmDict)

# Excluir item
del filmDict["inception"]
pp.pprint(filmDict)

