
# Crie um programa que receba um grafo dirigido e ponderado como argumento. Ao final, 
# imprima na tela o valor do fluxo máximo resultante da execução do algoritmo de Edmonds-Karp.
from collections import deque

def edmonds_karp(grafo, v_inicial, v_final):
    fluxo = 0
    F = [[0 for _ in range(grafo.qtdVertices + 1)] for _ in range(grafo.qtdVertices + 1)]
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

    return fluxo

def BFS(grafo, grafo_residual, fila, caminho_aumentante, cap_residual, final):
    while len(fila) > 0:
        vertice_atual = int(fila.popleft())
        for vizinho in list(grafo.vizinhos(vertice_atual).keys()):
            vizinho = int(vizinho)
            residual = (
                grafo.peso(vertice_atual, vizinho)
                - grafo_residual[vertice_atual][vizinho]
            )
            
            if residual > 0 and caminho_aumentante[vizinho] == -1:
                caminho_aumentante[vizinho] = vertice_atual
                cap_residual[vizinho] = min(
                    cap_residual[vertice_atual],
                    residual
                )
                
                if vizinho is not final:
                    fila.append(vizinho)
                else:
                    return cap_residual[final], caminho_aumentante
    return 0, caminho_aumentante

