import pandas as pd

series_objeto = pd.Series([1,7,9,13,17,99])

disciplinas = {'cursos': ['TCC', 'Python', 'Data Science', 'Machine Learning'],
               'carga_horaria': [120, 80, 200, 150],
               'requisito': [True, False, True, False]}

data = pd.DataFrame(disciplinas)

nome_cidade = pd.Series(['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba'])
populacao = pd.Series([12300000, 6748000, 2527000, 1960000])

pd.DataFrame({'nome_cidade': nome_cidade, 'populacao': populacao})
