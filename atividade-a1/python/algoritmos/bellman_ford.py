from estruturas.grafo import Grafo

'''
4. [Algoritmo de Bellman-Ford ou de Dijkstra] (2,0pts) Crie um programa que recebe um arquivo de grafo 
como argumento e um vértice s. O programa deverá executar o algoritmo de Bellman-Ford ou de Dijkstra e 
informar o caminho percorrido de s até todos os outros vértices do grafo e a distância necessária. A 
saı́da deverá ser impressa na tela de acordo com o exemplo abaixo. Cada linha representa o caminho 
realizado de s para o vértice da respectiva linha. Em cada linha, antes dos sı́mbolo “:” deverá estar o 
vértice destino. À direita de “:”, encontra-se o caminho percorrido de s até o vértice destino. Mais à 
direita encontram-se os sı́mbolos “d=” seguidos da distância necessária para percorrer o caminho.
'''

# atribuindo os valores iniciais
MAX_FLOAT = float('inf')

def bellman_ford(arquivo:str, v_inicial:int):
    # criando o grafo a partir das informações do arquivo
    grafo = Grafo(arquivo)

    qtd_vertices = grafo.qtdVertices

    D = [MAX_FLOAT for _ in range(qtd_vertices)]
    A = [None for _ in range(qtd_vertices)]
    
    D[v_inicial-1] = 0

    for _ in range(1, qtd_vertices-1):
        for aresta in grafo.arestas:
            u = aresta.vertice1.id - 1
            v = aresta.vertice2.id - 1

            #Precisamos olhar nas duas direções
            if D[v] > (D[u] + aresta.peso):
                D[v] = D[u] + aresta.peso
                A[v] = u + 1
            elif D[u] > (D[v] + aresta.peso):
                D[u] = D[v] + aresta.peso
                A[u] = v + 1

    for aresta in grafo.arestas:
        if D[aresta.vertice2.id - 1] > (D[aresta.vertice1.id - 1] + aresta.peso):
            return (False, None, None)

    return(True, D, A)