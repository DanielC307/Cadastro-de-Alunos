from notas import calcular_media, matriz_notas
from ordenacao import ordenar_por_nota


def relatorio_geral(alunos, mtr_notas):
    print("=== RELATÓRIO GERAL ===")

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for i, aluno in enumerate(alunos):
        notas = mtr_notas[i]
        media = calcular_media(i)
        situacao = "APROVADO" if media >= 6.0 else "REPROVADO"

        print(f"Matrícula: {aluno['matricula']} | Nome: {aluno['nome']}")
        print(f"Notas: {notas} | Média: {media:.1f} | Situação: {situacao}")
        print("-" * 30)

    print(f"Total de alunos: {len(alunos)}")


def relatorio_aprovados(alunos, mtr_notas):
    print("=== ALUNOS APROVADOS ===")

    contador_aprovados = 0
    for i, aluno in enumerate(alunos):
        media = calcular_media(i)
        if media >= 6.0:
            print(
                f"Matrícula: {aluno['matricula']} | Nome: {aluno['nome']} | Média: {media:.1f}"
            )
            contador_aprovados += 1

    if contador_aprovados == 0:
        print("Nenhum aluno foi aprovado.")
    else:
        print(f"Total de aprovados: {contador_aprovados}")


def relatorio_reprovados(alunos, mtr_notas):
    print("=== ALUNOS REPROVADOS ===")

    contador_reprovados = 0
    for i, aluno in enumerate(alunos):
        media = calcular_media(i)
        if media < 6.0:
            print(
                f"Matrícula: {aluno['matricula']} | Nome: {aluno['nome']} | Média: {media:.1f}"
            )
            contador_reprovados += 1

    if contador_reprovados == 0:
        print("Nenhum aluno foi reprovado.")
    else:
        print(f"Total de reprovados: {contador_reprovados}")


def relatorio_ranking(alunos, mtr_notas):
    print("=== RANKING DE DESEMPENHO ===")

    if not alunos:
        print("Nenhum aluno cadastrado para o ranking.")
        return

    alunos_com_media = []
    for i, aluno in enumerate(alunos):
        media = calcular_media(i)
        alunos_com_media.append((media, aluno))

    n = len(alunos_com_media)
    for i in range(n):
        for j in range(0, n - i - 1):
            if alunos_com_media[j][0] < alunos_com_media[j + 1][0]:
                alunos_com_media[j], alunos_com_media[j + 1] = alunos_com_media[j + 1], alunos_com_media[j]

    for posicao, (media, aluno) in enumerate(alunos_com_media, start=1):
        print(f"{posicao}º - {aluno['nome']} - Média: {media:.1f}")
