from estruturas.grafo import Grafo
from algoritmos.kruskal import kruskal
from algoritmos.ordenacao_topologica import ordenacao_topologica
from algoritmos.componentes_fortemente_conexas import componente_fortemente_conexa

# arquivos p/ teste
arquivo_grafo_orientado = "src/dirigido2.net"
arquivo_agm = 'src/agm_tiny.net'
arquivo_manha = "src/manha.net"

def print_questao1(arquivo_grafo_orientado):
    print('--- QUESTÃO 1 ---')
    grafo = Grafo(arquivo_grafo_orientado)

    Pt = componente_fortemente_conexa(grafo)

    qtd_arvore = Pt.count(None)
    arvores = [[] for _ in range(qtd_arvore)]
    
    cont_arvores = 0
    for index, vertice in enumerate(Pt):
        if vertice == None:     
            arvores[cont_arvores].append(index+1)
            proximo = index+1
            while True:
                if proximo in Pt:
                    proximo = Pt.index(proximo) + 1
                    arvores[cont_arvores].append(proximo)
                else:
                    break
            
            cont_arvores += 1

    for arvore in arvores:
        print(', '.join(str(elemento) for elemento in arvore[::-1]))



def print_questao2(arquivo_manha):
    print('--- QUESTÃO 2 ---')
    grafo = Grafo(arquivo_manha)
    lista_ordenada = ordenacao_topologica(grafo)
    for i in range(0, len(lista_ordenada)-1):
        print(lista_ordenada[i].rotulo, end = ' ')
        print("->", end = ' ')
    print(lista_ordenada[len(lista_ordenada) - 1].rotulo)

def print_questao3(arquivo: str) -> None:
    print('--- QUESTÃO 3 ---')
    arestas_agm = kruskal(arquivo)
    custo = 0
    arestas_formatadas = []
    for aresta in arestas_agm:
        custo += aresta.peso
        arestas_formatadas.append(f'{aresta.vertice1.id}-{aresta.vertice2.id}')     
    print(custo)
    print(str(arestas_formatadas).replace('[','').replace(']','').replace("'",''))

print_questao1(arquivo_grafo_orientado)
print_questao2(arquivo_manha)
print_questao3(arquivo_agm)
