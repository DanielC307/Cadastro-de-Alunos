# ordenacao.py
# Responsável pelos algoritmos de ordenação da lista de alunos.


def ordenar_por_nome(alunos):
    """
    Ordena a lista de alunos em ordem alfabética pelo nome.
    Algoritmo sugerido: BUBBLE SORT — simples de implementar e entender.

    Como funciona o Bubble Sort:
        - Percorre a lista várias vezes comparando pares de elementos adjacentes.
        - Se o elemento da esquerda for "maior" que o da direita, troca os dois.
        - A cada passagem completa, o maior elemento "borbulha" para o final.
        - Repete até não precisar mais trocar (lista ordenada).

    O que fazer:
        1. Usar dois laços aninhados (for externo + for interno).
           - Externo: controla quantas passagens fazemos (range(len(alunos))).
           - Interno: compara pares adjacentes (range(len(alunos) - i - 1)).
        2. Comparar alunos[j]["nome"] com alunos[j+1]["nome"] usando < ou >.
           Dica: strings em Python já comparam alfabeticamente com > e <.
           Use .lower() para evitar problemas com maiúsculas.
        3. Se estiver fora de ordem, trocar as posições:
               alunos[j], alunos[j+1] = alunos[j+1], alunos[j]
        4. Retornar a lista ordenada.

    Parâmetros:
        alunos (list): Lista de dicionários de alunos.

    Retorno:
        list: A mesma lista, agora ordenada por nome.
    """
    pass


def ordenar_por_nota(alunos, matriz_notas):
    """
    Ordena a lista de alunos em ordem DECRESCENTE pela média das notas.
    (Do maior para o menor — ranking de desempenho)

    O que fazer:
        1. Primeiro, calcular a média de cada aluno.
           Dica: importe a função calcular_media de notas.py e use o índice
           do aluno na lista para acessar a linha correta da matriz.
        2. Criar uma lista auxiliar de tuplas: [(media, aluno), ...].
           Isso facilita a ordenação mantendo a média junto ao aluno.
        3. Aplicar Bubble Sort nessa lista auxiliar, comparando pelo
           primeiro elemento da tupla (a média).
           Lembre-se: decrescente = o MAIOR vem primeiro.
        4. Extrair apenas os dicionários de alunos da lista ordenada.
        5. Retornar a nova lista ordenada.

    Parâmetros:
        alunos       (list): Lista de dicionários de alunos.
        matriz_notas (list): Matriz com as notas de todos os alunos.

    Retorno:
        list: Lista de alunos ordenada pela média (maior para menor).
    """
    pass