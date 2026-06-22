# notas.py
# Responsável pelo cadastro de notas e cálculo de médias.
# As notas são armazenadas em uma MATRIZ (lista de listas):
#
# Exemplo visual da matriz:
#   [ [nota_p1, nota_p2, nota_p3],   <- notas do aluno de matrícula 1
#     [nota_p1, nota_p2, nota_p3],   <- notas do aluno de matrícula 2
#     ...
#   ]
#
# Índice da linha  = posição do aluno na lista `alunos` (de aluno.py)
# Índice da coluna = número da prova (0 = P1, 1 = P2, 2 = P3)

# Número de provas por aluno
NUM_PROVAS = 3

# Matriz global de notas (começa vazia, cresce conforme alunos são cadastrados)
matriz_notas = []


def inicializar_notas(quantidade_alunos):
    """
    Cria a estrutura inicial da matriz de notas, preenchida com zeros.

    O que fazer:
        1. Usar um laço que repita `quantidade_alunos` vezes.
        2. A cada iteração, adicionar à `matriz_notas` uma lista com
           NUM_PROVAS zeros (uma linha da matriz).
           Dica: [0] * NUM_PROVAS cria uma lista de zeros.

    Parâmetros:
        quantidade_alunos (int): Número de linhas (alunos) da matriz.

    Retorno:
        None
    """
    pass


def cadastrar_nota(indice_aluno, indice_prova, valor_nota):
    """
    Insere ou atualiza a nota de um aluno em uma prova específica.

    O que fazer:
        1. Validar se o índice do aluno existe na matriz.
        2. Validar se o índice da prova está entre 0 e NUM_PROVAS - 1.
        3. Validar se o valor da nota está entre 0.0 e 10.0.
        4. Se tudo válido, atribuir: matriz_notas[indice_aluno][indice_prova] = valor_nota
        5. Exibir mensagem de confirmação ou de erro.

    Parâmetros:
        indice_aluno (int): Linha da matriz (posição do aluno).
        indice_prova (int): Coluna da matriz (número da prova, começa em 0).
        valor_nota  (float): Nota a ser registrada (0.0 a 10.0).

    Retorno:
        None
    """
    pass


def calcular_media(indice_aluno):
    """
    Calcula e retorna a média aritmética das notas de um aluno.

    O que fazer:
        1. Acessar a linha do aluno em matriz_notas: matriz_notas[indice_aluno]
        2. Somar todas as notas dessa linha.
           Dica: use a função sum() ou um laço acumulador.
        3. Dividir a soma pelo número de provas (NUM_PROVAS).
        4. Retornar o resultado.

    Parâmetros:
        indice_aluno (int): Linha da matriz correspondente ao aluno.

    Retorno:
        float: Média aritmética das notas do aluno.
    """
    pass


def exibir_notas_aluno(indice_aluno, nome_aluno):
    """
    Exibe todas as notas e a média de um aluno específico.

    O que fazer:
        1. Acessar a linha do aluno na matriz.
        2. Exibir o nome do aluno.
        3. Usar um laço para mostrar cada nota com o número da prova.
           Ex: "P1: 7.5  |  P2: 8.0  |  P3: 6.5"
        4. Chamar calcular_media() e exibir o resultado.
        5. Exibir também a situação: "Aprovado" (média >= 6) ou "Reprovado".

    Parâmetros:
        indice_aluno (int): Posição do aluno na matriz.
        nome_aluno   (str): Nome do aluno para exibir no cabeçalho.

    Retorno:
        None
    """
    pass