# Scripts Básicos para Sociologia Digital (sdbase)
Esse repositório guarda uma série de scripts básicos para o auxílio à pesquisa em Sociologia Digital. O objetivo dessa iniciativa é facilitar o acesso às técnicas computacionais a pesquisadores não familiarizados com essas técnicas, a iniciantes, assim como a usuários avançados que queiram construir técnicas mais complexas em cima das mais básicas aqui disponíveis. O foco do `sdbase` é o auxílio computacional à pesquisa qualitativa, mineração de texto para as humanidades e áreas relacionadas.

## Raspador do Reddit para a Análise Qualitativa e Codificação
Por enquanto, contamos com um único script de raspagem, formatação e exportação de dados da rede social Reddit para a análise qualitativa e a codificação. O formato de saída dos dados privilegia, portanto, a fidelidade à forma como os dados são exibidos na rede social, aproximando a experiência da codificação ao uso da plataforma no browser. Recomendamos ao usuário que clone o repositório para usá-lo, tal como explicado abaixo, na seção de instalação.

## Requisitos para a instalação
* Python 3.8
* pandas (biblioteca para manipulação de dados via DataFrames)
* PRAW (biblioteca que facilita o acesso à API do Reddit)

O arquivo `requirements.txt` contém todas essas informações, o que permite uma instalação fácil, como indicado na seção abaixo. 

## Instalação e modo de uso
Basta clonar o repositório, criar um ambiente virtual, instalar as bibliotecas indicadas acima com o `pip` e rodar os scripts com o Python, como no exemplo abaixo:
```
cd diretorio-de-instalacao 
git clone https://github.com/vmussa/sdbase.git
cd sdbase
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Para o usar módulo do Reddit:
```
python reddit\submissions_para_txt.py
```
Para o usar módulo do WhatsApp:
```
python whatsapp\conversas_para_csv.py
```

## Agradecimentos
Esse repositório está sendo desenvolvido no contexto de uma pesquisa de mestrado financiada pela Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (CAPES) realizada no Programa de Pós-Graduação em Sociologia e Antropologia (PPGSA) da Universidade Federal do Rio de Janeiro (UFRJ). O desenvolvimento desse pacote deve muito ao apoio dessas instituições.
