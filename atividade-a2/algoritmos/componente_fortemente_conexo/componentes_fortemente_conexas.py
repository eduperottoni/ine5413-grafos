from estruturas.grafo import Grafo
from estruturas.aresta import Aresta

# atribuindo os valores iniciais
MAX_FLOAT = float('inf')

def componente_fortemente_conexo(grafo):
    T, P, F = DFS(grafo)
    A = {}

    for aresta in grafo.arestas:
        aresta_transp = Aresta(aresta.vertice2, aresta.vertice1, aresta.peso)
        A.update({aresta_transp})

    grafo_transp = Grafo()
    grafo_transp.arestas(A)
    grafo_transp.vertices(grafo.vertices)

    Tt, Pt, Ft = DFS_adaptado(grafo_transp, F)

    return Pt

def DFS(grafo):
    C = [False for _ in range(qtd_vertices)]
    T = [MAX_FLOAT for _ in range(qtd_vertices)]
    F = [MAX_FLOAT for _ in range(qtd_vertices)]
    P = [None for _ in range(qtd_vertices)]

    tempo = 0

    for vertice in grafo.vertices():
        if C[vertice] == False:
            grafo, vertice, C, T, P, F, tempo = DFS_visit(grafo, vertice, C, T, P, F, tempo)
    
    return T, P, F

def DFS_visit(grafo, vertice, C, T, P, F, tempo):
    C[vertice] = True
    tempo += 1
    T[vertice] = tempo

    for u in grafo.aresta_saida(vertice):
        if C[u] == False:
            P[u] = vertice
            grafo, vertice, C, T, P, F, tempo = DFS_visit(grafo, vertice, C, T, P, F, tempo)

    tempo += 1
    F[vertice] = tempo

    return grafo, vertice, C, T, P, F, tempo