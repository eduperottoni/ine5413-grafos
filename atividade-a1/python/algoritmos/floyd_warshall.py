from estruturas.grafo import Grafo

MAX_FLOAT = float('inf')

'''
[Algoritmo de Floyd-Warshall] (2,0pts) Crie um programa que recebe um arquivo de grafo como argumento. O
programa deverá exercutar o algoritmo de Floyd-Warshall e mostrar as distâncias para cada par de vértices na tela
utilizando o formato do exemplo abaixo. Na saída, cada linha tería as distâncias para vértice na ordem crescente
dos índices informados no arquivo de entrada.
'''
def floyd_warshall(arquivo: str) -> tuple:
    grafo = Grafo(arquivo)

    # Matriz de adjacências para o algoritmo
    D = [[] for _ in range(grafo.qtdVertices)]
    # Inicializando a matriz (operação W(G))
    for vert_u in grafo.vertices:
        index_u = vert_u.id - 1
        for vert_v in grafo.vertices:
            index_v = vert_v.id - 1
            if vert_u.id == vert_v.id:
                D[index_u].append(0)
            else:
                if grafo.haAresta(vert_u.id, vert_v.id):
                    D[index_u].append(grafo.peso(vert_u.id, vert_v.id))
                else:
                    D[index_u].append(MAX_FLOAT)

    '''
    Uma das vantagens do nosso algoritmo é que ele não cria novas matrizes,
    gerando economia de memória.
    Logo, analisa a matriz D e atualiza os valores nela mesma
    '''
    for vert_k in grafo.vertices:
        index_k = vert_k.id - 1
        for vert_u in grafo.vertices:
            index_u = vert_u.id - 1
            for vert_v in grafo.vertices:
                index_v = vert_v.id - 1
                D[index_u][index_v] = min(D[index_u][index_v], D[index_u][index_k] + D[index_k][index_v])
    
    print(len(D))
    


