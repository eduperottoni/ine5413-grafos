#ifndef grafo_h
#define grafo_h

#include <string>
#include "nodo.h"
#include "matriz.h"

class Grafo
{
    public:
        // Construtor
        Grafo();
        // retorna a quantidade de vertices
        int qtdVertices(); 
		// retorna a quantidade de arestas
        int qtdArestas(); 
		// retorna o grau do vertice
        int grau(Nodo v); 
		// retorna o rotulo do vertice
        char rotulo(Nodo v); 
		// retorna os vizinhos do vertice
        int vizinhos(Nodo v); 
		//se {u, v} ∈ E, retorna verdadeiro; se nao existir, retorna falso
        bool haAresta(Nodo v, Nodo u); 
		// se {u, v} ∈ E, retorna o peso da aresta {u, v}; se nao existir, retorna um valor infinito positivo
        int peso(Nodo v, Nodo u); 
		// deve carregar um grafo a partir de um arquivo no formato especificado ao final deste documento
        void ler(string nome_do_arquivo); 

    private:
		// Número de vértices
        int _vertices;
		// Número de arestas
        int _arestas;
		// Matriz que representa o grafo
		// Matriz * _matriz;
		// Lista de adjacências que representa o grafo
		// ListaAdj * _listaAdj;

};

#endif