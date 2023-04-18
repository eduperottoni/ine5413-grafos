from estruturas.vertice import Vertice
from estruturas.aresta import Aresta

#Por enquanto, aceita ambos os tipos de grafo, com matriz inteira
class Grafo:

    def __init__(self, arquivo: str):
        self.__qtdVertices = 0
        self.__qtdArestas = 0
        self.__arestas = []
        self.__ler(arquivo)

    def rotulo(self, id_vertice: int):
        return self.__vertices[id_vertice - 1].rotulo

    def grau(self, id_vertice: int):
        return self.__vertices[id_vertice - 1].grau
    
    def vizinhos(self, id_vertice: int) -> dict:
        return self.__vertices[id_vertice - 1].vizinhos
    
    def peso(self, id_vertice1: int, id_vertice2: int) -> float:
        return self.__matriz[id_vertice1 - 1][id_vertice2 - 1]

    # se for dirigido -> matriz inteira
    # se não for -> matriz triangular
    # TODO VER O CASO EM QUE O GRAFO É DIRIGIDO (ORDEM IMPORTA)
    def haAresta(self, id_vertice1: float, id_vertice2: float) -> bool:
        id_max, id_min = max(id_vertice1, id_vertice2), min(id_vertice1, id_vertice2)
        return self.__matriz[id_max-1][id_min-1] != float('inf')

    def __ler(self, nome_arquivo: str):
        # leitura do arquivo
        arquivo = open(nome_arquivo, 'r')
        primeira_linha = arquivo.readline().split()
        qtd_vertices = int(primeira_linha[1])
        self.__qtdVertices += qtd_vertices

        # atribuindo o valor de "infinito"
        max_type = float('inf')
        self.__vertices = [max_type for i in range(qtd_vertices)]
        self.__matriz = [[max_type for i in range(qtd_vertices)] for j in range(qtd_vertices)]

        # posição na lista é id - 1
        for i in range(qtd_vertices):
            linha = arquivo.readline()
            linha = linha.replace('"', "").replace('\n', '').split(' ', 1)
            nome = linha[1]
            id = int(linha[0])
            self.__vertices[id - 1] = Vertice(int(linha[0]), nome)
        arquivo.readline()
        
        # preenche lista de adj. e matriz
        for linha in arquivo:
            linha = linha.split()
            vert_u_index = int(linha[0]) - 1
            vert_v_index = int(linha[1]) - 1
            weight_u_v = float(linha[2])
            self.__vertices[vert_u_index].vizinhos[str(vert_v_index + 1)] = weight_u_v
            self.__vertices[vert_v_index].vizinhos[str(vert_u_index + 1)] = weight_u_v
            self.__matriz[vert_u_index][vert_v_index] = weight_u_v
            self.__matriz[vert_v_index][vert_u_index] = weight_u_v
            self.__arestas.append(Aresta(self.__vertices[vert_u_index], self.__vertices[vert_v_index], weight_u_v))
            self.__qtdArestas += 1
        arquivo.close()

    @property
    def qtdVertices(self):
        return self.__qtdVertices

    @property
    def qtdArestas(self):
        return self.__qtdArestas
    
    @property
    def vertices(self):
        return self.__vertices

    @property
    def arestas(self):
        return self.__arestas
