from estruturas.grafo import Grafo
from algoritmos.kruskal import kruskal
from algoritmos.ordenacao_topologica import ordenacao_topologica

# arquivos p/ teste
arquivo_grafo_orientado = "src/dirigido1.net"
arquivo_agm = 'src/agm_tiny.net'
arquivo_manha = "src/manha.net"


#kruskal(arquivo_agm)



def print_questao2(arquivo_manha):
    grafo = Grafo(arquivo_manha)
    lista_ordenada = ordenacao_topologica(grafo)
    for i in range(0, len(lista_ordenada)-1):
        print(lista_ordenada[i].rotulo, end = ' ')
        print("->", end = ' ')
    print(lista_ordenada[len(lista_ordenada) - 1].rotulo)



print("Questão 02:")
print_questao2(arquivo_manha)