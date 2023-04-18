from estruturas.grafo import Grafo
from estruturas.vertice import Vertice
import time

def ciclo_euleriano(arquivo: str) -> list:
    grafo = Grafo(arquivo)
    Ce = [False for _ in range(grafo.qtdArestas)]   # marca todas as arestas como não percorridas

    v = grafo.vertices[0]           # seleciona um vertice qualquer

    (r, ciclo) = buscaCiclo(grafo, v, Ce)       # chama busca ciclo

    if r == False:
        return (False, None)

    else:
        if Ce == [True]*grafo.qtdArestas:
            return (True, ciclo)
        else:
            return (False, None)


def buscaCiclo(grafo: Grafo, v: Vertice, Ce: list) -> tuple[bool, list]:
    ciclo = [v]
    t = v
    while True:
        found = False
        for endereco in v.endereco_arestas:
            if Ce[endereco] == False:
                found = True
                address = endereco
                break

        if not found:
            return (False, None)
        else:
            Ce[address] = True
            if grafo.arestas[address].vertice1 == v:
                v = grafo.arestas[address].vertice2
            else:
                v = grafo.arestas[address].vertice1
            ciclo.append(v)

        if v == t:
            break

    for x in ciclo:
        for endereco in x.endereco_arestas:
            if Ce[endereco] == False:
                (r, novo_ciclo) = buscaCiclo(grafo, x, Ce)
                if r == False:
                    for k in range(len(ciclo)):
                        print(ciclo[k].id)
                    return (False, None)
                novo_ciclo.pop(0)
                ciclo = ciclo + novo_ciclo

    return (True, ciclo)