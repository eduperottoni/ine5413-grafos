from estruturas.grafo import Grafo
from estruturas.aresta import Aresta

# atribuindo os valores iniciais
MAX_FLOAT = float('inf')

def componente_fortemente_conexa(grafo):
    T, P, F = DFS(grafo, False)
    
    # a --> b
    # a <-- b
    new_neighbors = [{} for _ in range (grafo.qtdVertices)]
    for vertice in grafo.vertices:
        for vizinho in vertice.vizinhos.keys():
            new_neighbors[int(vizinho) - 1][vertice.id] = vertice.vizinhos[vizinho]
    
    for i in range(grafo.qtdVertices):
        grafo.vertices[i].vizinhos = new_neighbors[i]

    Tt, Pt, Ft = DFS(grafo, True, F)

    return Pt

def DFS(grafo, adaptado, F=None):
    C = [False for _ in range(grafo.qtdVertices)]
    T = [MAX_FLOAT for _ in range(grafo.qtdVertices)]
    F = [MAX_FLOAT for _ in range(grafo.qtdVertices)]
    P = [None for _ in range(grafo.qtdVertices)]

    tempo = 0

    if adaptado:
        tempo_vertice = []
        for u in range(grafo.qtdVertices):
            tempo_vertice.append((F[u], u))
        tempo_vertice.sort(reverse=True)
    
        for t, vertice in tempo_vertice:
            if C[vertice] == False:
                DFS_visit(grafo, grafo.vertices[vertice], C, T, P, F, tempo)
                tempo = F[vertice]
    else:
        for vertice in grafo.vertices:
            if C[vertice.id - 1] == False:
                DFS_visit(grafo, vertice, C, T, P, F, tempo)
                tempo = F[vertice.id - 1]
    
    return T, P, F

def DFS_visit(grafo, vertice, C, T, P, F, tempo):
    C[vertice.id - 1] = True
    tempo += 1
    T[vertice.id - 1] = tempo

    for u in vertice.vizinhos.keys():
        u = int(u)
        if C[u-1] == False:
            P[u-1] = vertice.id
            DFS_visit(grafo, grafo.vertices[u - 1], C, T, P, F, tempo)
            tempo = F[u-1]

    tempo += 1
    F[vertice.id - 1] = tempo