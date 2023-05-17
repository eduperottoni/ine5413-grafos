from estruturas.grafo import Grafo
from algoritmos.kruskal import kruskal
from algoritmos.ordenacao_topologica import ordenacao_topologica
from algoritmos.componentes_fortemente_conexas import componente_fortemente_conexa

# arquivos p/ teste
arquivo_grafo_orientado = "src/teste.net"
arquivo_agm = 'src/agm_tiny.net'
arquivo_manha = "src/manha.net"

def print_questao1(arquivo_grafo_orientado):
    print('--- QUESTÃO 1 ---')
    grafo = Grafo(arquivo_grafo_orientado)

    Pt = componente_fortemente_conexa(grafo)

    print("1111111111111111111111111111")
    print(Pt)

    for i in Pt:
        if i != None:
            print(i.id)

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
