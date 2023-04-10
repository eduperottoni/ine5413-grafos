from vertice import Vertice

class Grafo:

    def __init__(self):
        self.__qtdVertices = 0
        self.__qtdArestas = 0
        self.__vertices = []
        self.__matriz = []


    def peso(self, vertice1, vertice2):
        pass

    def vizinhos(self, value):
        for vertice in self.__vertices:
            if vertice.id == value:
                return list(vertice.vizinhos.keys())

    def haAresta(self, vertice1, vertice2):
        pass

    def grau(self, vertice):
        pass

    def ler(self, txt):
        arquivo = open(txt, 'r')
        primeira_linha = arquivo.readline().split()
        for i in range(int(primeira_linha[1])):
            linha = arquivo.readline()
            linha = linha.split()
            print(linha)
            
            
            nome = ""
            for j in range(1, len(linha)-1):
                nome = nome + linha[j]
                nome = nome + ' '

            
            nome = nome + linha[len(linha)-1]
            nome = nome.replace('"', "")
            self.__vertices.append(Vertice(int(linha[0]), nome))
        arquivo.readline()
        for linha in arquivo:
            linha = linha.split()
            vert_u = int(linha[0])
            vert_v = int(linha[1])
            weight_u_v = float(linha[2])
            self.__vertices[vert_u].vizinhos[vert_v] = weight_u_v
            self.__vertices[vert_v].vizinhos[vert_u] = weight_u_v
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