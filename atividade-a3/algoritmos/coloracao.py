

def lawler(grafo):
    X = [_ for _ in range(2**grafo.qtd_vertices())]
    X[0] = 0

    S = conjunto_potencia(grafo.arestas)


def conjunto_potencia(lista: list) -> list:
    # "lista_potencia" é uma lista de todas as combinações de elementos de "lista" com exceção do elemento vazio
    # "combinations(list, size)" retorna uma lista com todas as combinações de tamanho "size" na lista "list"
    lista_potencia = chain.from_iterable(combinations(lista, tamanho) for tamanho in range(len(lista) + 1))
    return lista_potencia



def coloracao(grafo):
    vertices_ordenados = []
    cores = []
    for v in grafo.vertices:
        qtd_vizinhos = len(v.vizinhos.keys())
        for i in range(len(vertices_ordenados)):
            if len(vertices_ordenados[i].vizinhos.keys()) > qtd_vizinhos:
                vertices_ordenados.insert(i, v)
        print(vertices_ordenados)