from estruturas.grafo import Grafo
from algoritmos.busca_largura import busca_largura
from algoritmos.floyd_warshall import floyd_warshall
from algoritmos.bellman_ford import bellman_ford
from algoritmos.hierholzer import hierholzer

# arquivos p/ teste
arquivo_ciclo_euleriano = "src/ContemCicloEuleriano.net"
arquivo_pequeno = "src/fln_pequena.net"
arquivo = "src/facebook_santiago.net"

# variável p/ teste
v_inicial = 8

'''
Questão 01 - Representação
 - 102 "Giovane Santos" -> (102, 284), (102, 563) 
 - 222 "Rosana Domingos" -> (15 222)
 - 563 "Carlos Robledo Werner" -> (38 563), (54 563), (64 563),... (tem 32 conexões)
'''

def print_questao1(arquivo:str):
    grafo = Grafo(arquivo)
    
    print(f'O grafo construído tem {grafo.qtdVertices} vértices' ) # 688
    print(f'O grafo construído tem {grafo.qtdArestas} arestas') #8725

'''
Questão 2 - Buscas
'''
def print_questao2(arquivo:str, v_inicial:int):
    d = busca_largura(arquivo, v_inicial)[0]
    arvore = {}
    for v_index, level in enumerate(d):
        if level != float('inf'):
            if f'{level}' in arvore.keys():
                arvore[f'{level}'].append(v_index + 1)
            else:
                arvore[f'{level}'] = [v_index + 1]
    
    for i in range(len(arvore.keys())):
        print(f"{i}: {str(arvore[str(i)]).replace('[', '').replace(']','')}")

def print_questao3(arquivo:str):
    haCiclo, ciclo = hierholzer(arquivo)
    if haCiclo:
        print("1")
        for i in range(len(ciclo)):
            if i != len(ciclo)-1:
                print(ciclo[i].id, end = ", ")
            else:
                print(ciclo[i].id)
    else:
        print("0")


def print_questao4(arquivo:str, v_inicial:int):
    valido, d, a = bellman_ford(arquivo=arquivo, v_inicial=v_inicial)

    if valido:
        for index, vertice in enumerate(a):
            lista = [index + 1]
            
            aux = index
            while a[aux] != v_inicial and a[aux] != None:
                lista.append(a[aux])
                aux = a[aux] - 1
            
            if lista[-1] != v_inicial:
                lista.append(v_inicial)
            
            lista.reverse()
            print(f"{index+1}: {str(lista).replace('[', '').replace(']','')}; d={d[index]}")
    else:
        print("O grafo possui um ciclo negativo!")

def print_questao5(arquivo:str):
    d = floyd_warshall(arquivo)
    
    for index, linha in enumerate(d):
        string = str(linha)
        print(f"{index + 1}:{string.replace('[', '').replace(']','')}")


print("Questão 01:")
print_questao1(arquivo_pequeno)
print("\nQuestão 02:")
print_questao2(arquivo, v_inicial)
print("\nQuestão 03: (sem ciclo)")
print_questao3(arquivo)
print("\nQuestão 03: (com ciclo)")
print_questao3(arquivo_ciclo_euleriano)
print("\nQuestão 04:")
print_questao4(arquivo, v_inicial)
print("\nQuestão 05:")
print_questao5(arquivo_pequeno)