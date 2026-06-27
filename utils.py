def ler_float(mensagem, minimo=0.0, maximo=10.0):
    while True:
        try:
            valor = float(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Erro: O valor deve estar entre {minimo} e {maximo}.")
        except ValueError:
            print("Erro: Valor inválido. Digite um número decimal.")


def ler_inteiro(mensagem, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"Erro: O valor deve ser no mínimo {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Erro: O valor deve ser no máximo {maximo}.")
                continue
            return valor
        except ValueError:
            print("Erro: Valor inválido. Digite um número inteiro.")


def exibir_separador(caractere="-", tamanho=40):
    print(caractere * tamanho)


def pausar():
    input("\nPressione Enter para continuar...")
