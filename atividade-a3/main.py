from estruturas.grafo import Grafo
# from algoritmos.edmonds_karp import edmonds_karp
from algoritmos.hopcroft_karp import hopcroft_karp
from algoritmos.edmonds_karp import edmonds_karp


# arquivos p/ teste
arquivo_emparelhamento = 'src/emparelhamento/pequeno.net'
teste_fluxo1 = 'src/fluxo_maximo/db4096.net'
teste_fluxo2 = 'src/fluxo_maximo/fluxo_maximo_aula.net'
teste_fluxo3 = 'src/fluxo_maximo/wiki.net'

def print_questao1(arquivo_fluxo_maximo, v_inicial, v_final):
    print('--- QUESTÃO 1 ---')
    grafo = Grafo(arquivo_fluxo_maximo)
    fluxo = edmonds_karp(grafo, v_inicial, v_final)
    print(f'O fluxo máximo de {v_inicial} para {v_final} é {fluxo}')
    # print(f"Fluxo máximo {v_inicial} -> {v_final}: {fluxo}")

# def print_questao2(arquarquivo_emparelhamentoivo):
#     print('--- QUESTÃO 2 ---')
#     grafo = Grafo(arquivo_emparelhamento)

#     print(hopcroft_karp(grafo))

# print_questao2(arquivo_emparelhamento)
print_questao1(teste_fluxo3, 1, 7)
print_questao1(teste_fluxo1, 1, 7)
print_questao1(teste_fluxo2, 1, 6)
