NUM_PROVAS = 3

matriz_notas = []


def inicializar_notas(quantidade_alunos):
    global matriz_notas
    for _ in range(quantidade_alunos):
        matriz_notas.append([0] * NUM_PROVAS)


def cadastrar_nota(indice_aluno, indice_prova, valor_nota):
    if indice_aluno < 0 or indice_aluno >= len(matriz_notas):
        print("Erro: Índice do aluno inválido.")
        return

    if indice_prova < 0 or indice_prova >= NUM_PROVAS:
        print("Erro: Índice da prova inválido.")
        return

    if valor_nota < 0.0 or valor_nota > 10.0:
        print("Erro: A nota deve estar entre 0.0 e 10.0.")
        return

    matriz_notas[indice_aluno][indice_prova] = valor_nota
    print(
        f"Nota {valor_nota} cadastrada com sucesso para o aluno {indice_aluno}, prova {indice_prova}."
    )


def calcular_media(indice_aluno):
    notas_aluno = matriz_notas[indice_aluno]
    soma = sum(notas_aluno)
    media = soma / NUM_PROVAS
    return media


def exibir_notas_aluno(indice_aluno, nome_aluno):
    notas_aluno = matriz_notas[indice_aluno]

    print(f"\nAluno: {nome_aluno}")

    strings_notas = []
    for i in range(NUM_PROVAS):
        strings_notas.append(f"P{i+1}: {notas_aluno[i]}")

    resultado_notas = "  |  ".join(strings_notas)
    print(resultado_notas)

    media = calcular_media(indice_aluno)
    print(f"Média: {media:.1f}")

    if media >= 6.0:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")
