from estruturas.grafo import Grafo
from estruturas.vertice import Vertice
from algoritmos.busca_largura import busca_largura
from algoritmos.floyd_warshall import floyd_warshall
from algoritmos.bellman_ford import bellman_ford
# from algoritmos.ciclo_euleriano import ciclo_euleriano

# arquivo = "src/facebook_santiago.net"
arquivo = "src/fln_pequena.net"
'''
Questão 01 - Representação
 - 102 "Giovane Santos" -> (102, 284), (102, 563) 
 - 222 "Rosana Domingos" -> (15 222)
 - 563 "Carlos Robledo Werner" -> (38 563), (54 563), (64 563),... (tem 32 conexões)
'''
# TESTES
# print(grafo.qtdVertices) # 688
# print(grafo.qtdArestas) #8725
# print(grafo.grau(563)) # 32
# print(grafo.rotulo(222)) # Rosana Domingos
# print(grafo.vizinhos(102)) # {'283': 1.0, '562': 1.0}
# # True - True - False
# print(grafo.haAresta(38, 563),  "-", grafo.haAresta(563, 54), "-", grafo.haAresta(64, 563))
# print(grafo.peso(222, 15)) # 1.0
def print_questao1():
    grafo = Grafo(arquivo)
    pass

'''
Questão 2 - Buscas
'''
def print_questao2():
    d = busca_largura(arquivo, 8)[0]
    arvore = {}
    for v_index, level in enumerate(d):
        if level != float('inf'):
            if f'{level}' in arvore.keys():
                arvore[f'{level}'].append(v_index + 1)
            else:
                arvore[f'{level}'] = [v_index + 1]
    
    for i in range(len(arvore.keys())):
        print(f'{i}:{arvore[str(i)]}')

# def print_questao3():
#     haCiclo, ciclo = ciclo_euleriano(arquivo)
#     print(haCiclo, ciclo)


def print_questao4():
    valido, d, a = bellman_ford(arquivo, 8)
    print(valido, d, a)

def print_questao5():
    d = floyd_warshall(arquivo)
    
    for index, linha in enumerate(d):
        string = str(linha)
        print(f"{index + 1}:{string.replace('[', '').replace(']','')}")


print_questao1()
print_questao2()
#print_questao3()
print_questao4()
print_questao5()