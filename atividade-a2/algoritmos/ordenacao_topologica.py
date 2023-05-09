from estruturas.grafo import Grafo
from estruturas.vertice import Vertice


MAX_FLOAT = float('inf')


def ordenacao_topologica(grafo : Grafo):
    C = [False for _ in range(grafo.qtdVertices)]
    T = [MAX_FLOAT for _ in range (grafo.qtdVertices)]
    F = [MAX_FLOAT for _ in range(grafo.qtdVertices)]

    tempo = 0
    O = []

    for vertice in grafo.vertices:
        if C[vertice.id - 1] == False:
            DFS_Visit_OT(grafo, vertice, C, T, F, tempo, O)
    return O

def DFS_Visit_OT(grafo : Grafo, vertice_inicial : Vertice, C : list[bool], T : list[float], F : list[float], tempo : int, O : list):
    C[vertice_inicial.id - 1] = True
    tempo += 1
    T[vertice_inicial.id - 1] = tempo
    for vertice in grafo.vertices:
        if C[vertice.id - 1] == False:
            DFS_Visit_OT(grafo, vertice, C, T, F, tempo, O)
    tempo = tempo + 1
    F[vertice_inicial.id - 1] = tempo
    O.insert(0, vertice_inicial)
