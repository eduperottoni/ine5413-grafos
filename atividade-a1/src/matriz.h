#ifndef matriz_h
#define matriz_h

#include <iostream>
#include <tuple>
#include "constantes.h"


using namespace std;

/**
* Usando templates (pesos podem ser de diferentes tipos)
*/
template<typename T>
class Matriz {
    public:
		// Construtor
		Matriz(const int tamanho);

		// Atribuir valor para determinada posição
		void setAresta(tuple<const int, const int> posicao, const T &peso);

        // getter da dimensao da matriz
        int getDimensao();

		// Consulta posição
		int peso(tuple<const int, const int> posicao);

    private:
        int _dimensao;
        T ** _matriz;
};

#endif

// Definido no .h, por conta do template
//@TODO fazer teste para definição do infinito do tipo
/*

CHAR_MAX, SCHAR_MAX, UCHAR_MAX, SHRT_MAX, USHRT_MAX, INT_MAX, UINT_MAX, LONG_MAX, ULONG_MAX, LLONG_MAX, ULLONG_MAX, UINT_LEAST16_MAX, UINT_LEAST32_MAX, FLT_MAX, DBL_MAX or LDBL_MAX

Usar:

#include <iostream>
#include <limits>

using namespace std;

template<typename T>
void showMinMax() {
   cout << "min: " << numeric_limits<T>::min() << endl;
   cout << "max: " << numeric_limits<T>::max() << endl;
   cout << endl;
}

int main() {

   cout << "short:" << endl;
   showMinMax<short>();
   cout << "int:" << endl;
   showMinMax<int>();
   cout << "long:" << endl;
   showMinMax<long>();
   cout << "float:" << endl;
   showMinMax<float>();
   cout << "double:" << endl;
   showMinMax<double>();
   cout << "long double:" << endl;
   showMinMax<long double>();
   cout << "unsigned short:" << endl;
   showMinMax<unsigned short>();
   cout << "unsigned int:" << endl;
   showMinMax<unsigned int>();
   cout << "unsigned long:" << endl;
   showMinMax<unsigned long>();
}
*/

template<typename T>
Matriz<T>::Matriz(const int tamanho) {
	_dimensao = tamanho;
	_matriz = new T* [tamanho];
	string tipo = typeid(T).name();
	cout << tipo;
    // adicionando as colunas para cada linha
	for (int i = 0; i < tamanho; i++) {
		_matriz[i] = new T[tamanho];
	// populando a matriz com o maior ponto flutuante possível
		for (int x = 0; x < tamanho; x++) {
			_matriz[i][x] = MAX_INT;
			cout << to_string(_matriz[i][x]) + "\n";
		}
	}
}