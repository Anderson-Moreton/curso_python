from conexao_post import conn

cursor_obj = conn.cursor()

sql = """
    UPDATE games
    SET NAME = %s
    WHERE ID = %s
"""

cursor_obj.execute(sql, ("Dragon Ball Z", 3))
cursor_obj.execute(sql, ("Fifa Street", 4))
conn.commit()
print("Dados atualizados com sucesso")
conn.close()
