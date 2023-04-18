from estruturas.vertice import Vertice

class Aresta:
    def __init__(self, vertice1: Vertice, vertice2: Vertice, peso):
        self.__vertice1 = vertice1
        self.__vertice2 = vertice2
        self.__peso = peso
    
    @property
    def vertice1(self):
        return self.__vertice1
    
    @property
    def vertice2(self):
        return self.__vertice2

    @property
    def peso(self):
        return self.__peso

    