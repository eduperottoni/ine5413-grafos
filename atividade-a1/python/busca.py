from collections import deque
from grafo import Grafo

'''
[Buscas] (2,0pts) Crie um programa que receba um arquivo de grafo e o índice do 
vértice s como argumentos3 . O programa deve fazer uma busca em largura4 a partir 
de s e deverá imprimir a saída na tela, onde cada linha deverá conter o nível 
seguido de “:” e a listagem de vértices encontrados naquele nível. O exemplo abaixo 
trata de uma saída, na qual a busca se iniciou pelo vértice s no nível 0, depois 
prosseguiu nos vértices 3, 4 e 5 para o próximo nível. No nível seguinte, a busca 
encontrou os vértices 1, 2, 6 e 7.

Cv -> se o vértice já foi visitado
Dv -> distância até o vértice
Av -> ancestral direto no caminho
'''

# os ids dos vértices precisam sempre ter o -1
def BuscaLargura(arquivo, v_inicial):
    # criando o grafo a partir das informações do arquivo
    grafo = Grafo()
    grafo.ler(arquivo)

    qtd_vertices = grafo.qtdVertices

    # atribuindo os valores iniciais
    max_type = float('inf')
    Cv = [False for i in range(qtd_vertices)]
    Dv = [max_type for i in range(qtd_vertices)]
    Av = [None for i in range(qtd_vertices)]

    Cv[v_inicial-1] = True
    Dv[v_inicial-1] = 0

    arvore = {0: [v_inicial]}

    fila = deque([v_inicial])

    #TODO eu achei esse len(fila) ridículo, mas a lib não tem um size (os que testei não funcionou)
    while len(fila) != 0:
        u = fila.popleft()

        lista_vizinhos = []
        for vizinho in grafo.vizinhos(u):
            vizinho = int(vizinho)
            
            if Cv[vizinho-1] == False:
                Cv[vizinho-1] = True
                Dv[vizinho-1] = Dv[u-1] + 1
                Av[vizinho-1] = u

                lista_vizinhos.append(vizinho)
                fila.append(vizinho)
        
        arvore[Dv[u-1] + 1] = lista_vizinhos
        
    return (arvore)