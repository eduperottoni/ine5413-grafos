from estruturas.grafo import Grafo
from algoritmos.kruskal import kruskal

# arquivos p/ teste
arquivo_grafo_orientado = "src/dirigido1.net"
arquivo_agm = 'src/agm_tiny.net'

grafo = Grafo(arquivo_grafo_orientado)


def print_questao1(arquivo: str) -> None:
    print('--- QUESTÃO 1 ---')
    arestas_agm = kruskal(arquivo)
    custo = 0
    arestas_formatadas = []
    for aresta in arestas_agm:
        custo += aresta.peso
        arestas_formatadas.append(f'{aresta.vertice1.id}-{aresta.vertice2.id}')     
    print(custo)
    print(str(arestas_formatadas).replace('[','').replace(']','').replace("'",''))

print_questao1(arquivo_agm)