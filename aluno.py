# aluno.py
# Responsável por tudo que envolve o cadastro e listagem de alunos.

# Estrutura de cada aluno (dicionário):
# {
#   "matricula": int,
#   "nome": str,
#   "curso": str
# }

# Lista global que armazena todos os alunos cadastrados
alunos = []


def cadastrar_aluno(nome, curso):
    """
    Cadastra um novo aluno na lista global `alunos`.

    O que fazer:
        1. Gerar uma matrícula única para o aluno.
           Dica: pode ser o len(alunos) + 1, ou um número sequencial.
        2. Criar um dicionário com as chaves: "matricula", "nome", "curso".
        3. Adicionar esse dicionário à lista `alunos`.
        4. Exibir uma mensagem confirmando o cadastro.

    Parâmetros:
        nome  (str): Nome completo do aluno.
        curso (str): Nome do curso do aluno.

    Retorno:
        None
    """
    pass


def listar_alunos():
    """
    Exibe todos os alunos cadastrados de forma organizada.

    O que fazer:
        1. Verificar se a lista `alunos` está vazia.
           Se estiver, exibir uma mensagem avisando.
        2. Se não estiver vazia, percorrer a lista com um laço.
        3. Para cada aluno, imprimir: matrícula, nome e curso.
           Dica: use f-strings para formatar bem a saída.

    Parâmetros:
        Nenhum.

    Retorno:
        None
    """
    pass


def remover_aluno(matricula):
    """
    Remove um aluno da lista com base na matrícula informada.

    O que fazer:
        1. Percorrer a lista `alunos` procurando o aluno com a matrícula.
        2. Se encontrar, remover o aluno da lista (use .remove() ou del).
        3. Exibir mensagem de sucesso ou de "aluno não encontrado".

    Parâmetros:
        matricula (int): Matrícula do aluno a ser removido.

    Retorno:
        None
    """
    pass