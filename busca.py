import aluno as _aluno


def busca_linear_nome(termo):
    termo = termo.strip().lower()
    resultados = []
    for aluno in _aluno.alunos:
        if termo in aluno["nome"].lower():
            resultados.append(aluno)
    return resultados


def busca_linear_matricula(matricula):
    try:
        mat_int = int(matricula)
    except ValueError:
        return None
    for aluno in _aluno.alunos:
        if aluno["matricula"] == mat_int:
            return aluno
    return None


def busca_binaria_matricula(lista_ordenada, matricula):
    try:
        mat_int = int(str(matricula).strip())
    except ValueError:
        return -1

    esquerda, direita = 0, len(lista_ordenada) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        mat_meio = lista_ordenada[meio]["matricula"]

        if mat_meio == mat_int:
            return meio
        elif mat_meio < mat_int:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1
