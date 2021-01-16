"""
Este código processa dados de conversas de whatsapp e os transforma em um
arquivo CSV estruturado. Isso permite análises no âmbito da mineração de
texto e de áreas afins.
"""
# %% Configurações iniciais
# importa bibiliotecas
import pandas as pd
import re
import os

# %% lê o arquivo da conversa
path_to_file = input('Insira o local do arquivo: ')
assert os.path.exists(path_to_file), \
    'Não é possível encontrar o arquivo em: .' + path_to_file
with open(path_to_file, 'r', encoding='utf-8') as f:
    txt = ''.join(f.readlines())

# %% processa o texto e o separa segundo data, hora, autor e conteúdo
pattern = r'(\d\d\/\d\d\/\d\d\d\d) (\d\d:\d\d) - (.*?): (.*)'
result = re.findall(pattern, txt)

# %% cria DataFrame
df = pd.DataFrame(result, columns=['data', 'hora', 'autor', 'conteudo'])

# %% exporta DataFrame com dados da conversa para CSV
df.to_csv(f'{os.path.dirname(__file__)}{os.sep}output{os.sep}conversa.csv', index=False)
