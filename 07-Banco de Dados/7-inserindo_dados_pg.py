from conexao_post import conn

cursor_obj = conn.cursor()

games = [
    ('Fifa', 2025, 9.2),
    ('GTA', 2025, 10.0)
]

for game in games:
    cursor_obj.execute(
        """
            INSERT INTO games(name, year, score)
            VALUES (%s, %s, %s)
        """, game
        
    )
conn.commit()
print("Dados inseridos com sucesso!")
conn.close()