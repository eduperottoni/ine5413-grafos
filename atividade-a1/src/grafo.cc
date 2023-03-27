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

char Grafo::rotulo(Nodo v) {
    return v.rotulo();
}

// lista
int vizinhos(Nodo v) {

}

// matriz
bool haAresta(Nodo v, Nodo u) {
    
}

// matriz
int peso(Nodo v, Nodo u) {
    
}

void Grafo::ler(char nome_do_arquivo) {
    fstream arquivo;
    arquivo.open(nome_do_arquivo);
    string conteudo;
    int linha = 0;
    while (!arquivo.eof()) {
        linha++;
        arquivo >> conteudo;
        string tag = "";
        for (int i = 0; i < conteudo.size(); i++) {
            tag += conteudos[i];
            printf(tag);
        }
    }

    arquivo.close();

}