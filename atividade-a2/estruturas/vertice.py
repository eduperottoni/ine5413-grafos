class Vertice:
    def __init__(self, id, rotulo):
        self.__id = id
        self.__rotulo = rotulo
        '''
        dicionário chave-valor para vizinhança:
        chave = id do vizinho
        valor = peso até esse vizinho
        '''
        self.__vizinhos = {}
        self.__endereco_arestas = []

    def add_endereco_aresta(self, endereco):
        self.__endereco_arestas.append(endereco)

    @property
    def id(self):
        return self.__id
    
    @property
    def rotulo(self):
        return self.__rotulo
    
    @property
    def vizinhos(self):
        return self.__vizinhos
    
    def add_vizinhos(self, vizinho):
        self.__vizinhos = vizinhos
    
    #ESTÁ FUNCIONANDO PARA GRAFOS NÃO DIRIGIDOS
    #PARA DIRIGIDOS, O GRAFO DEVE TER GRAU DE ENTRADA E GRAU DE SAÍDA
    @property
    def grau(self):
        return len(self.vizinhos.keys())

    @property
    def endereco_arestas(self):
        return self.__endereco_arestas


