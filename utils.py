# utils.py
# Funções utilitárias reutilizadas em todo o projeto.


def ler_float(mensagem, minimo=0.0, maximo=10.0):
    """
    Lê um número decimal do usuário com validação de intervalo.

    O que fazer:
        1. Usar um laço while True para ficar pedindo até receber um valor válido.
        2. Dentro do laço, usar input() para ler a entrada do usuário.
        3. Tentar converter para float com try/except ValueError.
           Se der erro de conversão, exibir mensagem de "valor inválido".
        4. Verificar se o float está entre `minimo` e `maximo`.
           Se não estiver, avisar o usuário e continuar o laço.
        5. Se for válido, retornar o valor.

    Parâmetros:
        mensagem (str)  : Texto exibido ao pedir o input.
        minimo   (float): Valor mínimo aceito (padrão 0.0).
        maximo   (float): Valor máximo aceito (padrão 10.0).

    Retorno:
        float: Valor válido inserido pelo usuário.
    """
    pass


def ler_inteiro(mensagem, minimo=None, maximo=None):
    """
    Lê um número inteiro do usuário com validação opcional de intervalo.

    O que fazer:
        1. Laço while True para repetir enquanto a entrada for inválida.
        2. Usar input() + int() com try/except ValueError.
        3. Se `minimo` for informado, checar se valor >= minimo.
        4. Se `maximo` for informado, checar se valor <= maximo.
        5. Retornar o inteiro válido.

    Parâmetros:
        mensagem (str)       : Texto do input.
        minimo   (int | None): Limite inferior (opcional).
        maximo   (int | None): Limite superior (opcional).

    Retorno:
        int: Valor inteiro válido.
    """
    pass


def exibir_separador(caractere="-", tamanho=40):
    """
    Imprime uma linha separadora para organizar o visual do menu.

    O que fazer:
        1. Multiplicar o `caractere` pelo `tamanho`.
           Dica: "-" * 40 gera "----------------------------------------"
        2. Usar print() para exibir a linha.

    Parâmetros:
        caractere (str): Caractere usado na linha (padrão "-").
        tamanho   (int): Quantas vezes repetir o caractere (padrão 40).

    Retorno:
        None
    """
    pass


def pausar():
    """
    Pausa a execução até o usuário pressionar Enter.
    Útil para o usuário ter tempo de ler o resultado antes de voltar ao menu.

    O que fazer:
        1. Chamar input() com a mensagem "\nPressione Enter para continuar...".
           Não precisa guardar o retorno.

    Retorno:
        None
    """
    pass