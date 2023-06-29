# Crie um programa que receba um arquivo de grafo bipartido, não-dirigido, não-ponderado e informe qual o 
# valor do emparelhamento máximo e quais arestas pertencem a ele. Utilize o algoritmo de Hopcroft-Karp.
from collections import deque

from estruturas.grafo import Grafo
from estruturas.aresta import Aresta

MAX_FLOAT = float('inf')


def X(grafo):
    cor = {}  # Dicionário para armazenar as cores dos vértices
    conjunto1 = set()  # Conjunto 1
    conjunto2 = set()  # Conjunto 2
    
    def teste(v, c):
        print(f'vertice v: {v}')
        cor[v.id - 1] = c  # Atribui a cor c ao vértice v
        if c == 1:
            conjunto1.add(v)
        else:
            conjunto2.add(v)

        for u in v.vizinhos.keys():
            print(f'u: {u}')
            if u not in cor:
                teste(u, 1 - c)  # Chama a função recursivamente para os vizinhos de v
    
    print(grafo.vertices)
    for v in grafo.vertices:
        print(f'vertice v: {v}')
        if v not in cor:
            teste(v, 0)  # Inicia uma busca em profundidade com a cor 0
            
    if len(conjunto1) == 0 or len(conjunto2) == 0:
        return None  # O grafo não é bipartido
    
    print(conjunto1)
    print(conjunto2)
    return conjunto1 if len(conjunto1) < len(conjunto2) else conjunto2


def hopcroft_karp(grafo):
    D = [MAX_FLOAT for _ in range(grafo.qtdVertices)]
    mate =  [None for _ in range(grafo.qtdVertices)]

    m = 0

    while BFS(grafo, mate, D):
        for x in X(grafo): #TODO: esse conjunto X precisa ser implementado no grafo
            if mate[x.id - 1] == None:
                if DFS(grafo, mate, x, D):
                    m += 1
    
    return (m, mate)

def BFS(grafo, mate, D):
    Q = deque()

    for x in X(grafo):
        if mate[x.id - 1] == None:
            D[x.id - 1] = 0
            Q.deque(x)
        else:
            D[x.id - 1] = MAX_FLOAT
    
    Dnull = MAX_FLOAT

    while len(Q):
        x = Q.popleft()

        if D[x.id - 1] < Dnull:
            for y in x.vizinhos.keys():
                if D[mate[y.id - 1]] == MAX_FLOAT:
                    D[mate[y.id - 1]] = D[x.id - 1] + 1
                    Q.deque(mate[y.id - 1])
    
    return (Dnull != MAX_FLOAT)