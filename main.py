import pandas as pd

# Lê o arquivo CSV com o separador correto (ponto e vírgula)
df = pd.read_csv('C:/Users/itarg/Desktop/Organiza_matricula/funcionariosUruoca.xls', sep=';')

# Extrai a coluna 'MATRICULA'
matriculas = df['MATRICULA']

# Formata as matrículas entre aspas simples e separadas por vírgula
matriculas_formatadas = ["'{}'".format(matricula) for matricula in matriculas]

# Cria um arquivo TXT e escreve as matrículas formatadas nele
with open('matriculas.txt', 'w') as arquivo_txt:
    arquivo_txt.write(','.join(matriculas_formatadas))

print("Matrículas formatadas foram salvas em 'matriculas.txt'")
