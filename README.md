# Scripts Básicos para Sociologia Digital (sdbase)
Esse repositório guarda uma série de scripts básicos para o auxílio à pesquisa em Sociologia Digital. O objetivo dessa iniciativa é facilitar o acesso às técnicas computacionais a pesquisadores não familiarizados com essas técnicas, a iniciantes, assim como a usuários avançados que queiram construir técnicas mais complexas em cima das mais básicas aqui disponíveis. O foco do `sdbase` é o auxílio computacional à pesquisa qualitativa, mineração de texto para as humanidades e áreas relacionadas.

## Raspador do Reddit para a Análise Qualitativa e Codificação
Por enquanto, contamos com um único script de raspagem, formatação e exportação de dados da rede social Reddit para a análise qualitativa e codificação. Recomendamos ao usuário que clone o repositório para usá-lo, tal como explicado abaixo, na sessão de instalação.

## Requisitos para a instalação
* Python 3.x
* PRAW (biblioteca facilitadora do acesso à API do Reddit)

## Instalação e modo de uso
Basta clonar o repositório, instalar as bibliotecas indicadas acima na sessão de requisitos e rodar os scripts com o Python:
```
cd diretorio-de-instalacao 
git clone https://github.com/vmussa/sdbase.git
cd sdbase
python .\reddit\submissions_para_txt.py