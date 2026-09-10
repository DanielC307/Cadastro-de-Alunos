# Sistema de Cadastro Acadêmico — Algoritmos de Busca e Ordenação

Aplicação de linha de comando em Python para cadastro de alunos, lançamento de notas e emissão de relatórios acadêmicos. O foco do projeto é a **implementação manual de algoritmos de busca e ordenação**, sem recorrer aos métodos prontos da linguagem.

## Por que implementar na mão

`sorted()` resolveria a ordenação em uma linha. O exercício aqui é outro: entender o custo e o funcionamento de cada algoritmo por dentro. Todos foram escritos do zero:

| Algoritmo | Onde está | Complexidade |
| --- | --- | --- |
| Busca linear por nome (substring) | `busca.busca_linear_nome` | O(n) |
| Busca linear por matrícula | `busca.busca_linear_matricula` | O(n) |
| Busca binária por matrícula | `busca.busca_binaria_matricula` | O(log n) |
| Bubble sort por nome | `ordenacao.ordenar_por_nome` | O(n²) |
| Bubble sort por média (decrescente) | `ordenacao.ordenar_por_nota` | O(n²) |

A busca binária exige lista previamente ordenada por matrícula — a mesma restrição que um índice de banco de dados impõe, o que torna o exercício uma boa introdução ao motivo pelo qual índices existem.

## Funcionalidades

- Cadastro de alunos com matrícula gerada automaticamente
- Lançamento de notas em 3 provas, com validação de faixa (0 a 10)
- Cálculo de média e situação (aprovado a partir de 6,0)
- Busca por nome (parcial, ignorando maiúsculas) e por matrícula
- Ordenação alfabética e por desempenho
- Relatório geral, relatório de aprovados/reprovados e ranking

## Arquitetura

O projeto é dividido por responsabilidade, cada módulo com um papel único:

```
.
├── main.py         # Menu e roteamento das opções (camada de interface)
├── aluno.py        # Entidade aluno: criação, cadastro, listagem, remoção
├── notas.py        # Matriz de notas, validação e cálculo de médias
├── busca.py        # Buscas linear e binária
├── ordenacao.py    # Ordenação por nome e por média
├── relatorios.py   # Geração dos relatórios e ranking
└── utils.py        # Leitura validada de entrada e formatação do terminal
```

As notas são armazenadas em uma **matriz** (`matriz_notas`), em que a linha corresponde ao índice do aluno e a coluna à prova — estrutura escolhida para praticar acesso bidimensional em vez de simplesmente aninhar dicionários.

O módulo `utils.py` concentra a leitura de entrada com validação em laço, de forma que entrada inválida nunca quebra o programa nem propaga tipo errado para as camadas de baixo.

## Como executar

Sem dependências externas — apenas Python 3.

```bash
git clone https://github.com/DanielC307/Cadastro-de-Alunos.git
cd Cadastro-de-Alunos
python main.py
```

Navegue pelo menu digitando o número da opção desejada. A opção `0` encerra.

## Conceitos praticados

- Estruturas de dados: listas, dicionários e matrizes
- Algoritmos de busca e ordenação implementados do zero, com análise de complexidade
- Modularização por responsabilidade e separação entre interface e lógica
- Validação defensiva de entrada e tratamento de exceções
- Escopo de variáveis e uso controlado de estado global

## Próximos passos

- [ ] Persistir os dados em arquivo (JSON) ou banco (SQLite/SQL Server), hoje tudo é perdido ao encerrar
- [ ] Substituir o estado global por classes, encapsulando alunos e notas
- [ ] Implementar merge sort ou quick sort e comparar o desempenho com o bubble sort em volume maior
- [ ] Vincular a matriz de notas à matrícula em vez do índice posicional, para que a remoção de um aluno não desalinhe as notas
- [ ] Cobrir buscas e ordenações com testes automatizados
