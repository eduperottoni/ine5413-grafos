#include "grafo.h"
#include "constantes.h"

int main(void) {

    Grafo grafo = Grafo();
    grafo.ler(NOME_ARQUIVO_LEITURA);

    Matriz<unsigned int> mat = Matriz<unsigned int>(5);

    return 0;
}
