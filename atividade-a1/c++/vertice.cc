#include "vertice.h"

int Vertice::getId() {
    return _id;
}

int Vertice::getGrau() {
    return _grau;
}

std::string Vertice::getRotulo() {
    return _rotulo;
}

ListaEncadeada<Vertice> Vertice::getVizinhos() {
    return _vizinhos;
}
