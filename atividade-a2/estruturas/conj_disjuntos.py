class CDElemento:
    """
    Classe que implementa uma estrutura de dados mais eficiente para ser utilizada
    no algoritmo de Kruskal. Essa estrutura reduz a complexidade da solução, uma 
    vez que a mesma depende da eficiência da estrutura de dados para conjuntos.
    """
    def __init__(self):
        self.pai = self
        self.rank = 1
    
    def CDLigar(self, x, y):
        if x.rank > y.rank:
            y.pai = x
        else:
            x.pai = y
            if x.rank == y.rank:
                y.rank = y.rank + 1
    
    def CDEncontrar(self, x):
        if x != x.pai:
            x.pai = self.CDEncontrar(x.pai)
        return x.pai

    def CDUniao(self, x, y):
        self.CDLigar(self.CDEncontrar(x), self.CDEncontrar(y))