from estruturas.grafo import Grafo
from estruturas.conj_disjuntos import CDElemento

def kruskal(arquivo: str):
    """
    Implementação do algoritmo de Kruskal para encontrar árvore mínima do grafo
    A implementação utiliza estrutura de dados que com maior eficiência, para redução
    da complexidade
    """
    grafo = Grafo(arquivo)
    A = []
    S = []
    for _ in grafo.vertices:
        S.append(CDElemento())
    arestas_ordenadas = sorted(grafo.arestas, key=lambda x: x.peso, reverse=False)
    for aresta in arestas_ordenadas:
        index_v1 = aresta.vertice1.id - 1
        index_v2 = aresta.vertice2.id - 1
        if S[index_v1].CDEncontrar(S[index_v1]) != S[index_v1].CDEncontrar(S[index_v2]):
            A.append(aresta)
            S[index_v1].CDUniao(S[index_v1], S[index_v2])
    return A