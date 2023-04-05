class Vertice:
    def __init__(self, id, rotulo):
        self.__id = id
        self.__rotulo = rotulo
        self.__vizinhos = {}
    
    @property
    def id(self):
        return self.__id
    
    @property
    def rotulo(self):
        return self.__rotulo
    
    @property
    def vizinhos(self):
        return self.__vizinhos

