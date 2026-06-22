# busca.py
# Responsável pelos algoritmos de busca na lista de alunos.


def busca_linear_nome(alunos, nome_buscado):
    """
    Percorre a lista do início ao fim procurando um aluno pelo nome.
    Algoritmo: BUSCA LINEAR (O(n)) — não precisa de lista ordenada.

    O que fazer:
        1. Usar um laço for para percorrer cada aluno da lista.
        2. Comparar aluno["nome"] com nome_buscado.
           Dica: use .lower() nos dois lados para ignorar maiúsculas/minúsculas.
        3. Se encontrar, retornar o dicionário do aluno.
        4. Se o laço terminar sem encontrar, retornar None.

    Parâmetros:
        alunos       (list): Lista de dicionários de alunos.
        nome_buscado (str) : Nome a ser buscado.

    Retorno:
        dict | None: Dicionário do aluno encontrado, ou None se não existir.
    """
    pass


def busca_linear_matricula(alunos, matricula_buscada):
    """
    Percorre a lista procurando um aluno pela matrícula.
    Algoritmo: BUSCA LINEAR (O(n)).

    O que fazer:
        1. Usar um laço for percorrendo cada aluno.
        2. Comparar aluno["matricula"] com matricula_buscada.
        3. Se encontrar, retornar o dicionário do aluno.
        4. Se não encontrar, retornar None.

    Parâmetros:
        alunos            (list): Lista de dicionários de alunos.
        matricula_buscada (int) : Matrícula a ser buscada.

    Retorno:
        dict | None: Dicionário do aluno encontrado, ou None se não existir.
    """
    pass


def busca_binaria_matricula(alunos_ordenados, matricula_buscada):
    """
    Busca um aluno pela matrícula usando o algoritmo de busca binária.
    Algoritmo: BUSCA BINÁRIA (O(log n)) — EXIGE lista ordenada por matrícula.

    Como funciona a busca binária:
        - Define dois ponteiros: inicio = 0, fim = len(lista) - 1
        - Enquanto inicio <= fim:
            * Calcula o meio: meio = (inicio + fim) // 2
            * Se o valor do meio for igual ao buscado → encontrou!
            * Se o valor do meio for MENOR que o buscado → busca na metade direita (inicio = meio + 1)
            * Se o valor do meio for MAIOR que o buscado → busca na metade esquerda (fim = meio - 1)
        - Se sair do laço sem encontrar → retorna None

    O que fazer:
        1. Inicializar as variáveis inicio, fim e meio.
        2. Implementar o laço while com a lógica acima.
        3. Comparar alunos_ordenados[meio]["matricula"] com matricula_buscada.
        4. Retornar o aluno encontrado ou None.

    Parâmetros:
        alunos_ordenados  (list): Lista de alunos ORDENADA por matrícula.
        matricula_buscada (int) : Matrícula a ser buscada.

    Retorno:
        dict | None: Dicionário do aluno encontrado, ou None se não existir.
    """
    pass