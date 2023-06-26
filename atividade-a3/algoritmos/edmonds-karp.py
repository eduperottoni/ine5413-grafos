
# Crie um programa que receba um grafo dirigido e ponderado como argumento. Ao final, 
# imprima na tela o valor do fluxo máximo resultante da execução do algoritmo de Edmonds-Karp.
from collections import deque

from estruturas.grafo import Grafo
from estruturas.aresta import Aresta


def edmonds_karp(grafo, v_inicial, t, grafo_f):
    C = [False for _ in range(grafo.qtdVertices)]
    A = [None for _ in range(grafo.qtdVertices)]

    C[v_inicial.id - 1] = True
    
    Q = deque([v_inicial])

    while len(Q):
        u = Q.popleft()

        for v in vertice_inicial.vizinhos.keys():
            if C[v.id - 1] == False and grafo_f.peso(u, v) > 0:
                C[v.id - 1] = True
                A[v.id - 1] = u

                if v == t:
                    p = [t]
                    w = t

                    while w != v_inicial:
                        w = A[w.id - 1]
                        p.append(w)
                    return p
                Q.deque(v)
    
    return None


