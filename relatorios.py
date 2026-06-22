# relatorios.py
# Gera os relatórios do sistema acadêmico.


def relatorio_geral(alunos, matriz_notas):
    """
    Exibe um relatório completo com todos os alunos, suas médias e situação.

    O que fazer:
        1. Imprimir um cabeçalho formatado (ex: "=== RELATÓRIO GERAL ===").
        2. Verificar se há alunos cadastrados; se não, avisar e retornar.
        3. Usar um laço for com enumerate(alunos) para percorrer a lista.
           O enumerate fornece índice (i) e o dicionário do aluno.
        4. Para cada aluno:
           a. Exibir matrícula e nome.
           b. Exibir cada nota (acessando matriz_notas[i]).
           c. Calcular e exibir a média (importe de notas.py).
           d. Exibir situação: "APROVADO" se média >= 6, senão "REPROVADO".
        5. Ao final, imprimir um rodapé com o total de alunos.

    Parâmetros:
        alunos       (list): Lista de dicionários de alunos.
        matriz_notas (list): Matriz com as notas.

    Retorno:
        None
    """
    pass


def relatorio_aprovados(alunos, matriz_notas):
    """
    Exibe apenas os alunos com média >= 6.0 (aprovados).

    O que fazer:
        1. Imprimir cabeçalho "=== ALUNOS APROVADOS ===".
        2. Criar um contador de aprovados (começa em 0).
        3. Percorrer os alunos com enumerate.
        4. Para cada aluno, calcular a média.
           Se média >= 6.0, exibir os dados e incrementar o contador.
        5. Ao final, exibir o total de aprovados.
           Se nenhum foi aprovado, exibir mensagem adequada.

    Parâmetros:
        alunos       (list): Lista de dicionários de alunos.
        matriz_notas (list): Matriz com as notas.

    Retorno:
        None
    """
    pass


def relatorio_reprovados(alunos, matriz_notas):
    """
    Exibe apenas os alunos com média < 6.0 (reprovados).

    O que fazer:
        Mesma lógica de relatorio_aprovados(), mas filtrando média < 6.0.

    Parâmetros:
        alunos       (list): Lista de dicionários de alunos.
        matriz_notas (list): Matriz com as notas.

    Retorno:
        None
    """
    pass


def relatorio_ranking(alunos, matriz_notas):
    """
    Exibe os alunos ordenados do maior para o menor desempenho (ranking).

    O que fazer:
        1. Imprimir cabeçalho "=== RANKING DE DESEMPENHO ===".
        2. Chamar ordenar_por_nota() de ordenacao.py para obter lista ordenada.
        3. Percorrer a lista ordenada e exibir posição, nome e média.
           Ex: "1º - Ana Silva - Média: 9.2"
        4. Use enumerate(lista, start=1) para começar a contagem em 1.

    Parâmetros:
        alunos       (list): Lista de dicionários de alunos.
        matriz_notas (list): Matriz com as notas.

    Retorno:
        None
    """
    pass