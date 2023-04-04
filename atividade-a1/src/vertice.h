#ifndef Vertice_h
#define Vertice_h

#include <string>
#include "listaEncadeada.h"



class Vertice
{
    public:

        Vertice(int id, std::string rotulo) {
            _id = id;
            _rotulo = rotulo;
            _grau = 0;
        }
        // retorna o ID do Vertice
        int getId();
        
        // retorna o grau do Vertice
        int getGrau();
        
        // retorna o rotulo do Vertice
        std::string getRotulo();

        // retorna os vizinhos
        ListaEncadeada<Vertice> getVizinhos();

    private:
        std::string _rotulo;
        int _id;
        int _grau;
        ListaEncadeada<Vertice> _vizinhos;
};

#endif