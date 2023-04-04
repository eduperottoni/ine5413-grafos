#ifndef grafo_h
#define grafo_h

#include <string>
#include "vertice.h"
#include "matriz.h" 
#include <fstream>

template<typename T>
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
        int grau(Vertice v); 
		// retorna o rotulo do vertice
        char rotulo(Vertice v); 
		// retorna os vizinhos do vertice
        int vizinhos(Vertice v); 
		//se {u, v} ∈ E, retorna verdadeiro; se nao existir, retorna falso
        bool haAresta(Vertice v, Vertice u); 
		// se {u, v} ∈ E, retorna o peso da aresta {u, v}; se nao existir, retorna um valor infinito positivo
        int peso(Vertice v, Vertice u); 
		// deve carregar um grafo a partir de um arquivo no formato especificado ao final deste documento
        void ler(string nome_do_arquivo); 

    private:
		// Número de vértices
        int _vertices;
		// Número de arestas
        int _arestas;
		// Matriz que representa o grafo
		Matriz<T> * _matriz;
		// Lista de adjacências que representa o grafo
        Vertice ** _listaAdj = nullptr;
		//ListaEncadeada<T> * _listaAdj;
};

#endif

template<typename T>
Grafo<T>::Grafo() {
    _vertices = 0;
    _arestas = 0;
    //_matriz = nullptr;
}

template<typename T>
int Grafo<T>::qtdVertices() {
    return _vertices;
}

template<typename T>
int Grafo<T>::qtdArestas() {
    return _arestas;
}

// lista
template<typename T>
int Grafo<T>::grau(Vertice v) {

}

// char Grafo::rotulo(Vertice v) {
//     return v.rotulo();
// }

// lista
template<typename T>
int Grafo<T>::vizinhos(Vertice v) {

}

// matriz
template<typename T>
bool Grafo<T>::haAresta(Vertice v, Vertice u) {
    
}

// matriz
template<typename T>
int Grafo<T>::peso(Vertice v, Vertice u) {
    
}

template<typename T>
void Grafo<T>::ler(string nome_arquivo) {
    fstream arquivo;
    arquivo.open(nome_arquivo);

    string conteudo;
    int linha = 0;
    string conteudo_linha;

    linha++;
    getline(arquivo, conteudo_linha);
    string teste = "*vertices";
    string quantidade = conteudo_linha.substr(teste.length(), conteudo_linha.length());
    _listaAdj = new Vertice*[stoi(quantidade)];

    while (linha < stoi(quantidade) + 1) {
        linha++;
        string id = "";
        int caracter = 0;
        getline(arquivo, conteudo_linha);
        while (conteudo_linha[caracter] != ' ') {
            id = id + conteudo_linha[caracter];
            caracter++;
        }
        string nome = "";
        caracter = caracter + 2;
        while (conteudo_linha[caracter] != '"') {
            nome = nome + conteudo_linha[caracter];
            caracter++;
        }
        Vertice * vertice = new Vertice(stoi(id), nome);
        _listaAdj[stoi(id)-1] = vertice;
        cout << _listaAdj[stoi(id)-1]->getRotulo() << endl;
        //cout << vertice.getId() << " + " << vertice.getRotulo() << endl;
    }

    // while (!arquivo.eof()) {
    //     linha++;

    // }

    arquivo.close();
}