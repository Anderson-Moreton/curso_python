class Game:
    name = ""
    yearLaunch = 0
    multiplayer = False
    note = 0


# Primeiro jogo
game1 = Game()
game1.name = "The Legend of Zelda: Breath of the Wild"
game1.yearLaunch = 2017
game1.multiplayer = False
game1.note = 9.5

# Segundo jogo
game2 = Game()
game2.name = "Fortnite"
game2.yearLaunch = 2017
game2.multiplayer = True
game2.note = 8.0

# Terceiro Jogo
game3 = Game()
game3.name = "Mario World"
game3.yearLaunch = 1990
game3.multiplayer = True
game3.note = 10.0

# Quarto Jogo
game4 = Game()
game4.name = "Fifa 26"
game4.yearLaunch = 2025
game4.multiplayer = True
game4.note = 9.4

print("###Dados do Jogo###")
print(f"\nNome do jogo: {game1.name}\nAno de Lançamento: {game1.yearLaunch}")
print(f"\nNome do jogo: {game2.name}\nAno de Lançamento: {game2.yearLaunch}")
