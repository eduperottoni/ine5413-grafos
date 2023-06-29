
# Crie um programa que receba um grafo dirigido e ponderado como argumento. Ao final, 
# imprima na tela o valor do fluxo máximo resultante da execução do algoritmo de Edmonds-Karp.
from collections import deque
from estruturas.grafo import Grafo
from estruturas.aresta import Aresta

def edmonds_karp(grafo, v_inicial, v_final):
    fluxo = 0
    F = [[0 for _ in range(grafo.qtdVertices + 1)] for _ in range(grafo.qtdVertices + 1)]
    fila = None
    while True:
        c_aumentante = [-1 for _ in range(grafo.qtdVertices + 1)]
        c_aumentante[v_inicial] = -1
        cap_residual = [0 for _ in range(grafo.qtdVertices + 1)]
        cap_residual[v_inicial] = float('inf')
        fila = deque([v_inicial])

        fluxoCaminho, c_aumentante = BFS(
            grafo, F, fila, c_aumentante, cap_residual, v_final
        )

        if fluxoCaminho == 0: break

        fluxo += fluxoCaminho
        v_atual = v_final

        while v_atual != v_inicial:
            vizinho = c_aumentante[v_atual]
            F[vizinho][v_atual] += fluxoCaminho
            F[v_atual][vizinho] -= fluxoCaminho
            v_atual = vizinho

    print(f"Fluxo máximo {v_inicial} -> {v_final}: {fluxo}")
            
    # C = [False for _ in range(grafo.qtdVertices)]
    # A = [None for _ in range(grafo.qtdVertices)]

    # C[v_inicial.id - 1] = True
    
    # Q = deque([v_inicial])

    # while len(Q):
    #     u = Q.popleft()

    #     for v in v_inicial.vizinhos.keys():
    #         if C[v.id - 1] == False and grafo_f.peso(u, v) > 0:
    #             C[v.id - 1] = True
    #             A[v.id - 1] = u

    #             if v == v_final:
    #                 p = [v_final]
    #                 w = v_final

    #                 while w != v_inicial:
    #                     w = A[w.id - 1]
    #                     p.append(w)
    #                 return p
    #             Q.deque(v)
    
#     return None

def BFS(grafo, grafo_residual, fila, caminhoAumentante, capacidadeResidual, final):
    while len(fila) > 0:
        verticeAtual = fila.popleft()

        for vizinho in grafo.vizinhos(int(verticeAtual)).keys():
            residual = (
                grafo.peso(int(verticeAtual), int(vizinho))
                - grafo_residual[int(verticeAtual)][int(vizinho)]
            )
            
            if residual > 0 and caminhoAumentante[int(vizinho)] == -1:
                caminhoAumentante[int(vizinho)] = verticeAtual
                capacidadeResidual[int(vizinho)] = min(
                    capacidadeResidual[int(verticeAtual)],
                    residual
                )
                
                if vizinho is not final:
                    fila.append(vizinho)
                else:
                    return capacidadeResidual[final], caminhoAumentante
    return 0, caminhoAumentante




# from collections import (
#     deque,
# )  # https://docs.python.org/3/library/collections.html#collections.deque
# from Grafo.Grafo import Grafo


# class EdmondsKarp:
#     def __init__(self, grafo: Grafo, inicial: int, final: int):
#         self.__grafo = grafo
#         self.__inicial = inicial
#         self.__final = final

#         self.__fluxo = -0
#         self.__F = [
#             [0 for _ in range(self.__grafo.qtdVertices() + 1)]
#             for _ in range(self.__grafo.qtdVertices() + 1)
#         ]

#     def run(self):
#         while True:
#             A = [-1 for _ in range(self.__grafo.qtdVertices() + 1)]
#             caminhoAumentante[self.__inicial] = -1

#             C = [0 for _ in range(self.__grafo.qtdVertices() + 1)]
#             capacidadeResidual[self.__inicial] = float("inf")
            
#             self.__fila = deque([self.__inicial])

#             fluxoCaminho, caminhoAumentante = self.BFS(
#                 caminhoAumentante, capacidadeResidual
#             )
            
#             if fluxoCaminho == 0:
#                 break
        
#             self.__fluxo += fluxoCaminho
#             verticeAtual = self.__final
            
#             while verticeAtual != self.__inicial:
#                 vizinho = caminhoAumentante[verticeAtual]
#                 self.__F[vizinho][verticeAtual] += fluxoCaminho
#                 self.__F[verticeAtual][vizinho] -= fluxoCaminho
#                 verticeAtual = vizinho
    
#         print(f"Fluxo máximo {self.__inicial} -> {self.__final}: {self.__fluxo}")

    
        
#         return 0, caminhoAumentante

