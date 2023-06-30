def coloracao(grafo):
    vertices_ordenados = []
    cores = []
    for v in grafo.vertices:
        qtd_vizinhos = len(v.vizinhos.keys())
        if len(vertices_ordenados) != 0:
            for i in range(len(vertices_ordenados)):
                if len(vertices_ordenados[i].vizinhos.keys()) <= qtd_vizinhos:
                    vertices_ordenados.insert(i, v)
                    break
        else:
            vertices_ordenados = [v]

    cores = [None for _ in range(len(vertices_ordenados))]
    cor = 1

    for vertice in vertices_ordenados:
        if cores[vertice.id-1] == None:
            cores[vertice.id-1] = cor
            found = False
            for vertice_2 in vertices_ordenados:
                if cores[vertice_2.id-1] == None:
                    if not grafo.haAresta(vertice.id, vertice_2.id):
                        for vizinho in vertice_2.vizinhos.keys():
                            if cores[int(vizinho)-1] == cor:
                                found = True
                                break
                        if found == False:
                            cores[vertice_2.id-1] = cor
            cor += 1


    return cor-1, cores