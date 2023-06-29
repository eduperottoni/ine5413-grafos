from estruturas.grafo import Grafo
# from algoritmos.edmonds_karp import edmonds_karp
from algoritmos.hopcroft_karp import hopcroft_karp
from algoritmos.edmonds_karp import edmonds_karp


# arquivos p/ teste
arquivo_emparelhamento = 'src/emparelhamento/pequeno.net'
teste_fluxo1 = 'src/fluxo_maximo/db4096.net'
teste_fluxo2 = 'src/fluxo_maximo/fluxo_maximo_aula.net'
teste_fluxo3 = 'src/fluxo_maximo/wiki.net'

# def print_questao1(arquivo_emparelhamento):
#     print('--- QUESTÃO 1 ---')
#     grafo = Grafo(arquivo_emparelhamento)

#     print(edmonds_karp(grafo, 4, 5, grafo.rede_residual()))

def print_questao1(arquivo_fluxo_maximo):
    print('--- QUESTÃO 1 ---')
    grafo = Grafo(arquivo_fluxo_maximo)
    edmonds_karp(grafo, 1, 5)

# def print_questao2(arquarquivo_emparelhamentoivo):
#     print('--- QUESTÃO 2 ---')
#     grafo = Grafo(arquivo_emparelhamento)

#     print(hopcroft_karp(grafo))

# print_questao2(arquivo_emparelhamento)
print_questao1(teste_fluxo3)
