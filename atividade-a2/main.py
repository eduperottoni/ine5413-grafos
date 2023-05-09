from estruturas.grafo import Grafo
from algoritmos.kruskal import kruskal

# arquivos p/ teste
arquivo_grafo_orientado = "src/dirigido1.net"
arquivo_agm = 'src/agm_tiny.net'

grafo = Grafo(arquivo_grafo_orientado)

kruskal(arquivo_agm)