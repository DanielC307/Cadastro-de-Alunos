# main.py
# Ponto de entrada do sistema. Contém o menu principal e o fluxo do programa.
# Importa e orquestra todos os outros módulos.

import aluno
import notas
import busca
import ordenacao
import relatorios
import utils


def exibir_menu():
    """
    Exibe as opções do menu principal na tela.

    O que fazer:
        1. Usar print() para exibir cada opção numerada.
        2. Chamar utils.exibir_separador() antes e depois das opções.

    Sugestão de opções:
        1. Cadastrar aluno
        2. Listar alunos
        3. Cadastrar notas
        4. Buscar aluno por nome
        5. Buscar aluno por matrícula
        6. Ordenar por nome
        7. Ordenar por nota
        8. Relatório geral
        9. Relatório aprovados / reprovados
        10. Ranking
        0. Sair

    Retorno:
        None
    """
    pass


def executar_opcao(opcao):
    """
    Executa a ação correspondente à opção escolhida no menu.

    O que fazer:
        1. Usar if/elif/else para tratar cada opção.
        2. Para cada caso, chamar a função correspondente dos módulos.
        3. Sempre chamar utils.pausar() ao final de cada ação,
           para o usuário ler o resultado antes de voltar ao menu.

    Parâmetros:
        opcao (str): String com o número digitado pelo usuário.

    Retorno:
        bool: Retornar False se opcao == "0" (sair), True nos demais casos.
    """
    pass


def main():
    """
    Função principal. Controla o loop do menu.

    O que fazer:
        1. Usar um laço while True.
        2. Dentro do laço:
           a. Chamar exibir_menu().
           b. Ler a opção com input().
           c. Chamar executar_opcao(opcao).
           d. Se executar_opcao retornar False, sair do laço com break.
        3. Exibir mensagem de encerramento ao sair.

    Retorno:
        None
    """
    pass


# Ponto de entrada do script
# O bloco abaixo garante que main() só rode quando você executar este arquivo
# diretamente (não quando for importado por outro módulo).
if __name__ == "__main__":
    main()