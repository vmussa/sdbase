"""
Este código coleta dados de múltiplas discussões (submissions) de subreddits 
a partir de uma consulta (query) à API do Reddit e, então, os exporta em um
formato que busca conservar sua forma de apresentação original da web. Isso
permite a análise qualitativa e a codificação dos dados em softwares como
RQDA e QualCoder.
"""

# %% Configurações iniciais
# importa as bibliotecas
import os
import io
import praw
from praw.models import MoreComments
from textwrap import dedent

# %% Acessa a API do Reddit
client_id = input('Insira seu client_id: ')
client_secret = input('Insira seu client_secret: ')
username = input('Insira seu usuário do reddit: ')
password = input('Insira sua senha do reddit: ')
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent="<Python/praw>:<ScriptsBasicosParaSociologiaDigital (sdbase)>:<v0.0.1> (by /u/vmtgomes)",
    username=username,
    password=password
)

# %% Obtém lista de objetos Submission através da search query de interesse
query = input('Insira sua consulta: ') # ver https://www.reddit.com/wiki/search
sub = input('Insira o subreddit a ser raspado: ')
submissions = [submission for submission in reddit.subreddit(sub).search(query)]

# %% Função que itera a CommentForest recursivamente
def parse_comments(top_comment):
    # conteúdo dos comentários
    content = f'<{top_comment.parent_id}>: {top_comment.body} <{top_comment.id}>\n\n\n'
    for comment in top_comment.replies:
        content += '\t' + parse_comments(comment) # elemento recursivo
    return content

# %% Função que escreve txt legível a partir de objeto Submission
def submission_to_txt(submission, filename):
    with io.open(filename, "w", encoding="utf-8") as f:
        header = dedent(f"""\
                        ***SUBMISSION***\n
                        URL: {submission.url}\n
                        TITLE: {submission.title}\n
                        SELFTEXT: {submission.selftext}\n\n\n\n"""
        )
        body = '***COMMENTS***\n\n'
        submission.comments.replace_more(limit=0)
        for comment in submission.comments:
            body += parse_comments(comment)
        f.write(header+body)

# %% Escreve txt's para cada objeto Submission
for s in submissions:
    submission_to_txt(
        s, f'{os.path.dirname(__file__)}{os.sep}output{os.sep}subreddit_{sub}_submission_{s.id}.txt'
        )
