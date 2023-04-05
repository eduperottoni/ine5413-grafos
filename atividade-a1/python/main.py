from grafo import Grafo
from vertice import Vertice

grafo = Grafo()

arquivo = "facebook_santiago.net"
grafo.ler(arquivo)

print(grafo.vizinhos(1))