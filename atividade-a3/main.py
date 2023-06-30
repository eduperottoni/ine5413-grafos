from estruturas.grafo import Grafo
# from algoritmos.edmonds_karp import edmonds_karp
from algoritmos.hopcroft_karp import hopcroft_karp
from algoritmos.edmonds_karp import edmonds_karp
from algoritmos.coloracao import coloracao

# arquivos p/ teste
teste_fluxo1 = 'src/fluxo_maximo/db4096.net'
teste_fluxo2 = 'src/fluxo_maximo/fluxo_maximo_aula.net'
teste_fluxo3 = 'src/fluxo_maximo/wiki.net'

teste_emparelhamento1 = 'src/emparelhamento/pequeno.net'
teste_emparelhamento2 = 'src/emparelhamento/gr128_10.net'
teste_emparelhamento3 = 'src/emparelhamento/grafo_bipartido.net'

teste_coloracao1 = 'src/coloracao/cor3.net'

def print_questao1(arquivo_fluxo_maximo, v_inicial, v_final):
    print('--- QUESTÃO 1 ---')
    grafo = Grafo(arquivo_fluxo_maximo)
    fluxo = edmonds_karp(grafo, v_inicial, v_final)
    print(f'O fluxo máximo de {v_inicial} para {v_final} é {fluxo}')

def print_questao2(arquivo_emparelhamento):
    print('\n--- QUESTÃO 2 ---')
    grafo = Grafo(arquivo_emparelhamento)

    m, mate = hopcroft_karp(grafo)

    print("Emparelhamento máximo = ", m, end = ".\n")
    print("Arestas do emparelhamento = ", end = "")
    
    i = 0
    for aresta in mate:
        if(i != len(mate) - 1):
            print(aresta, end = ", ")
        else:
            print(aresta, end = ".\n\n")
        i += 1

def print_questao3(arquivo_coloracao):
    print('--- QUESTÃO 3 ---')

    grafo = Grafo(arquivo_coloracao)

    qtd_cores, cores = coloracao(grafo)
    print("sao necessarias", qtd_cores, "cores")
    for vertice in grafo.vertices:
        print("vertice", str(vertice.id), "pintado com a cor", str(cores[vertice.id-1]))

# chama os prints
print_questao1(teste_fluxo3, 1, 7)
print_questao2(teste_emparelhamento1)
print_questao3(teste_coloracao1)

