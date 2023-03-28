#include "grafo.h"
#include <fstream>
#include <string>
#include <iostream>


using namespace std;

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

    while (!arquivo.eof()) {
        linha++;
        arquivo >> conteudo;
        string tag = "";
        for (int i = 0; i < conteudo.size(); i++) {
            tag += conteudo[i];
            cout << tag;
        }
    }

    arquivo.close();

}