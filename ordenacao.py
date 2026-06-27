from notas import calcular_media


def ordenar_por_nome(alunos):
    n = len(alunos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if alunos[j]["nome"].lower() > alunos[j + 1]["nome"].lower():
                alunos[j], alunos[j + 1] = alunos[j + 1], alunos[j]
    return alunos


def ordenar_por_nota(alunos, matriz_notas):
    auxiliar = []
    for i in range(len(alunos)):
        media = calcular_media(i)
        auxiliar.append((media, alunos[i]))

    n = len(auxiliar)
    for i in range(n):
        for j in range(0, n - i - 1):
            if auxiliar[j][0] < auxiliar[j + 1][0]:
                auxiliar[j], auxiliar[j + 1] = auxiliar[j + 1], auxiliar[j]

    alunos_ordenados = []
    for par in auxiliar:
        alunos_ordenados.append(par[1])

    return alunos_ordenados
