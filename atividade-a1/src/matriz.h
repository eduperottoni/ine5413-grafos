#ifndef matriz_h
#define matriz_h

#include <tuple>

class Matriz {
    public:
		// Construtor
		Matriz(const int tamanho);

		// Atribuir valor para determinada posição
		void setAresta(tuple<const int, const int> posicao, const int peso);

        // getter da dimensao da matriz
        int getDimensao();

		// Consulta posição
		int peso(tuple<const int, const int> posicao);

    private:
        int _dimensao;
        int ** _matriz;
};

#endif