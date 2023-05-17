from estruturas.grafo import Grafo
from estruturas.aresta import Aresta

# atribuindo os valores iniciais
MAX_FLOAT = float('inf')

def componente_fortemente_conexa(grafo):
    T, P, F = DFS(grafo)
    A = []

    for aresta in grafo.arestas:
        aresta_transp = Aresta(aresta.vertice2, aresta.vertice1, aresta.peso)
        A.append(aresta_transp)
    
    #TODO: aqui preciso inverter a ordem dos vertices
    # a --> b
    # a <-- b
    new_neighbors = [{} for _ in range (grafo.qtdVertices)]
    for vertice in grafo.vertices:
        for vizinho in vertice.vizinhos.keys():
            # vizinhos de a deleta b
            # vizinhos de b adiciona a
            new_neighbors[int(vizinho) - 1][vertice.id] = vertice.vizinhos[vizinho]
    
    for i in range(grafo.qtdVertices):
        grafo.vertices[i].vizinhos = new_neighbors[i]
    

    grafo_transp = grafo
    grafo_transp.arestas = A

    Tt, Pt, Ft = DFS(grafo_transp)

    return Pt

def DFS(grafo):
    C = [False for _ in range(grafo.qtdVertices)]
    T = [MAX_FLOAT for _ in range(grafo.qtdVertices)]
    F = [MAX_FLOAT for _ in range(grafo.qtdVertices)]
    P = [None for _ in range(grafo.qtdVertices)]

    tempo = 0

    for vertice in grafo.vertices:
        if C[vertice.id - 1] == False:
            DFS_visit(grafo, vertice, C, T, P, F, tempo)
    
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

    tempo += 1
    F[vertice.id - 1] = tempo