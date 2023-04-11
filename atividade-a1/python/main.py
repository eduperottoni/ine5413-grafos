from grafo import Grafo
from vertice import Vertice
from busca import BuscaLargura

grafo = Grafo()

arquivo = "facebook_santiago.net"
grafo.ler(arquivo)

'''
Questão 01 - Representação
 - 102 "Giovane Santos" -> (102, 284), (102, 563) 
 - 222 "Rosana Domingos" -> (15 222)
 - 563 "Carlos Robledo Werner" -> (38 563), (54 563), (64 563),... (tem 32 conexões)
'''
print(grafo.qtdVertices) # 688
print(grafo.qtdArestas) #8725
print(grafo.grau(563)) # 32
print(grafo.rotulo(222)) # Rosana Domingos
print(grafo.vizinhos(102)) # {'283': 1.0, '562': 1.0}
# True - True - False
print(grafo.haAresta(38, 563),  "-", grafo.haAresta(563, 54), "-", grafo.haAresta(64, 563))
print(grafo.peso(222, 15)) # 1.0


'''
Questão 2 - Buscas
'''

# não sei como confirmir se está certo, e como fazer uma saída bonita (na verdade é só pensar mais, mas ñ tive tempo)
print(BuscaLargura(grafo, 222))