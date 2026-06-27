alunos = []
_proximo_id = 1


def criar_aluno(nome, curso):
    global _proximo_id
    aluno = {
        "matricula": _proximo_id,
        "nome": nome,
        "curso": curso
    }
    _proximo_id += 1
    return aluno


def cadastrar_aluno(nome, curso):
    aluno = criar_aluno(nome, curso)
    alunos.append(aluno)
    return aluno


def listar_alunos():
    return alunos


def remover_aluno(matricula):
    for i, aluno in enumerate(alunos):
        if aluno["matricula"] == matricula:
            alunos.pop(i)
            return True
    return False
