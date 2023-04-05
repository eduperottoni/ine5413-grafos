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
            primeiro_vertice = int(linha[0])
            for vertice in self.__vertices:
                if vertice.id == primeiro_vertice:
                    for vertice2 in self.__vertices:
                        if vertice2.id == int(linha[1]):
                            vertice.vizinhos[vertice2] = float(linha[2])
                            vertice2.vizinhos[vertice] = float(linha[2])

    @property
    def qtdVertices(self):
        return self.__qtdVertices

    @property
    def qtdArestas(self):
        return self.__qtdArestas
    
    @property
    def vertices(self):
        return self.__vertices