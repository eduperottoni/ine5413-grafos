#include "grafo.h"
#include <fstream>
#include <string>
#include <iostream>


using namespace std;

Grafo::Grafo() {
    _vertices = 0;
    _arestas = 0;
    // _matriz = nullptr;
}

int Grafo::qtdVertices() {
    return _vertices;
}

int Grafo::qtdArestas() {
    return _arestas;
}

// lista
int grau(Nodo v) {

}

// char Grafo::rotulo(Nodo v) {
//     return v.rotulo();
// }

// lista
int vizinhos(Nodo v) {

}

// matriz
bool haAresta(Nodo v, Nodo u) {
    
}

// matriz
int peso(Nodo v, Nodo u) {
    
}

void Grafo::ler(string nome_arquivo) {
    fstream arquivo;
    arquivo.open(nome_arquivo);

    string conteudo;
    int linha = 0;
    string conteudo_linha;

    while (!arquivo.eof()) {
        linha++;
        getline(arquivo, conteudo_linha);
        // cout << "ola" + conteudo_linha + "\n";
        string tag = conteudo_linha;
        cout << tag + "\n";
    }

    arquivo.close();
}