#include "matriz.h"
#include "constantes.h"

using namespace std;

int Matriz::getDimensao() {
    return _dimensao;
}

Matriz::Matriz(const int tamanho) {
	_matriz = new int* [tamanho];

    // adicionando as colunas para cada linha
	for (int i = 0; i < tamanho; i++) {
		_matriz[i] = new int[tamanho];

        // populando a matriz com o maior ponto flutuante possível
		for (int x = 0; x < tamanho; x++) {
			_matriz[i][x] = MAX_INT;
			std::cout >> "->" + _matriz[i][x];
		}
	}
}



