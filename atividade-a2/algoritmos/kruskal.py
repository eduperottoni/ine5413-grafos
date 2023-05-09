from estruturas.grafo import Grafo
from estruturas.conj_disjuntos import CDElemento

def kruskal(arquivo: str):
    """
    Implementação do algoritmo de Kruskal para encontrar árvore mínima do grafo
    A implementação utiliza estrutura de dados que com maior eficiência, para redução
    da complexidade
    https://edisciplinas.usp.br/pluginfile.php/4627613/mod_resource/content/1/ACH2024-Aula10-ArvoreGeradoraMinima_AlgKruskal.pdf
    """
    grafo = Grafo(arquivo)
    A = []
    S = []
    for _ in grafo.vertices:
        S.append(CDElemento())
    arestas_ordenadas = sorted(grafo.arestas, key=lambda x: x.peso, reverse=False)
    for _, aresta in enumerate(arestas_ordenadas):
        print(aresta)
        if S[aresta.vertice1.id].CDEncontrar(S[aresta.vertice1.id]) != S[aresta.vertice1.id].CDEncontrar(S[aresta.vertice2.id]):
            A.append(aresta)
            S[aresta.vertice1.id].CDUniao(S[aresta.vertice1.id], S[aresta.vertice2.id])
    return A