"""
Este código processa dados de conversas de whatsapp e os transforma em um
arquivo CSV estruturado. Isso permite análises no âmbito da mineração de
texto e de áreas afins.
"""
import pandas as pd
import re
import os

def parse_chat(txt):
    """Transforma txt bruto em objeto processado pelo modulo re,
    separando os dados por data, hora, autor e conteudo da mensagem."""
    pattern = r'(\d\d\/\d\d\/\d\d\d\d) (\d\d:\d\d) - (.*?): (.*)'
    result = re.findall(pattern, txt)
    return result


if __name__ == '__main__':
    # lê o arquivo da conversa
    path_to_file = input('Insira o local do arquivo de conversa do WhatsApp: ')
    assert os.path.exists(path_to_file), \
        'Não é possível encontrar o arquivo em: .' + path_to_file
    with open(path_to_file, 'r', encoding='utf-8') as f:
        txt = ''.join(f.readlines())

    # processa texto da conversa
    data = parse_chat(txt)

    # cria DataFrame
    df = pd.DataFrame(data, columns=['data', 'hora', 'autor', 'conteudo'])

    # exporta DataFrame com dados da conversa para CSV
    df.to_csv(
        f'{os.path.dirname(__file__)}{os.sep}output{os.sep}conversa.csv',
        index=False
        )
