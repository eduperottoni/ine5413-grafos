from collections import deque
from estruturas.grafo import Grafo

'''
[Buscas] (2,0pts) Crie um programa que receba um arquivo de grafo e o índice do 
vértice s como argumentos. O programa deve fazer uma busca em largura a partir 
de s e deverá imprimir a saída na tela, onde cada linha deverá conter o nível 
seguido de “:” e a listagem de vértices encontrados naquele nível. O exemplo abaixo 
trata de uma saída, na qual a busca se iniciou pelo vértice s no nível 0, depois 
prosseguiu nos vértices 3, 4 e 5 para o próximo nível. No nível seguinte, a busca 
encontrou os vértices 1, 2, 6 e 7.

C -> se o vértice já foi visitado
D -> distância até o vértice
A -> ancestral direto no caminho
'''

# atribuindo os valores iniciais
MAX_FLOAT = float('inf')

# os ids dos vértices precisam sempre ter o -1
def busca_largura(arquivo:str, v_inicial:int) -> dict:
    # criando o grafo a partir das informações do arquivo
    grafo = Grafo(arquivo)

    qtd_vertices = grafo.qtdVertices
   
    C = [False for _ in range(qtd_vertices)]
    D = [MAX_FLOAT for _ in range(qtd_vertices)]
    A = [None for _ in range(qtd_vertices)]

    C[v_inicial-1] = True
    D[v_inicial-1] = 0
    
    fila = deque([v_inicial])
    while len(fila) != 0:
        u = fila.popleft()

        for vizinho in grafo.vizinhos(u):
            vizinho = int(vizinho)
            
            if C[vizinho-1] == False:

                C[vizinho-1] = True
                D[vizinho-1] = D[u-1] + 1
                A[vizinho-1] = u
                fila.append(vizinho)
        
    return (D, A)