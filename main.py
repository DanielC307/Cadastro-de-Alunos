import aluno
import notas
import busca
import ordenacao
import relatorios
import utils


def exibir_menu():
    utils.exibir_separador()
    print("1. Cadastrar aluno")
    print("2. Listar alunos")
    print("3. Cadastrar notas")
    print("4. Buscar aluno por nome")
    print("5. Buscar aluno por matrícula")
    print("6. Ordenar por nome")
    print("7. Ordenar por nota")
    print("8. Relatório geral")
    print("9. Relatório aprovados / reprovados")
    print("10. Ranking")
    print("0. Sair")
    utils.exibir_separador()


def executar_opcao(opcao):
    if opcao == "1":
        nome = input("Digite o nome do aluno: ").strip()
        curso = input("Digite o curso do aluno: ").strip()
        if nome and curso:
            aluno.cadastrar_aluno(nome, curso)
            notas.inicializar_notas(1)
            print("Aluno cadastrado com sucesso!")
        else:
            print("Erro: Nome e curso não podem ser vazios.")

    elif opcao == "2":
        lista = aluno.listar_alunos()
        if not lista:
            print("Nenhum aluno cadastrado.")
        for a in lista:
            print(f"Matrícula: {a['matricula']} | Nome: {a['nome']} | Curso: {a['curso']}")

    elif opcao == "3":
        if not aluno.listar_alunos():
            print("Erro: Não há alunos cadastrados para registrar notas.")
        else:
            max_aluno = len(aluno.listar_alunos()) - 1
            ind_aluno = utils.ler_inteiro(
                f"Digite o índice do aluno (0 a {max_aluno}): ",
                minimo=0,
                maximo=max_aluno
            )
            ind_prova = utils.ler_inteiro(
                f"Digite o índice da prova (0 a {notas.NUM_PROVAS - 1}): ",
                minimo=0,
                maximo=notas.NUM_PROVAS - 1
            )
            nota = utils.ler_float("Digite o valor da nota (0.0 a 10.0): ", minimo=0.0, maximo=10.0)
            notas.cadastrar_nota(ind_aluno, ind_prova, nota)

    elif opcao == "4":
        termo = input("Digite o nome (ou parte dele) para buscar: ")
        resultados = busca.busca_linear_nome(termo)
        if resultados:
            for a in resultados:
                print(f"Matrícula: {a['matricula']} | Nome: {a['nome']}")
        else:
            print("Nenhum aluno encontrado.")

    elif opcao == "5":
        mat = input("Digite a matrícula do aluno: ")
        resultado = busca.busca_linear_matricula(mat)
        if resultado:
            print(f"Matrícula: {resultado['matricula']} | Nome: {resultado['nome']} | Curso: {resultado['curso']}")
        else:
            print("Nenhum aluno encontrado.")

    elif opcao == "6":
        lista = aluno.listar_alunos()
        if not lista:
            print("Nenhum aluno cadastrado.")
        else:
            ordenados = ordenacao.ordenar_por_nome(lista[:])
            for a in ordenados:
                print(f"Matrícula: {a['matricula']} | Nome: {a['nome']}")

    elif opcao == "7":
        lista = aluno.listar_alunos()
        if not lista:
            print("Nenhum aluno cadastrado.")
        else:
            ordenados = ordenacao.ordenar_por_nota(lista[:], notas.matriz_notas)
            for a in ordenados:
                for i, original in enumerate(lista):
                    if original["matricula"] == a["matricula"]:
                        media = notas.calcular_media(i)
                        break
                print(f"Nome: {a['nome']} | Média: {media:.1f}")

    elif opcao == "8":
        relatorios.relatorio_geral(aluno.listar_alunos(), notas.matriz_notas)

    elif opcao == "9":
        relatorios.relatorio_aprovados(aluno.listar_alunos(), notas.matriz_notas)
        print()
        relatorios.relatorio_reprovados(aluno.listar_alunos(), notas.matriz_notas)

    elif opcao == "10":
        relatorios.relatorio_ranking(aluno.listar_alunos(), notas.matriz_notas)

    elif opcao == "0":
        print("Encerrando o sistema. Até logo!")
        return False

    else:
        print("Opção inválida. Tente novamente.")

    utils.pausar()
    return True


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if not executar_opcao(opcao):
            break


if __name__ == "__main__":
    main()
