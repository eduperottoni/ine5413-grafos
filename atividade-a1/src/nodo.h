#ifndef nodo_h
#define nodo_h

class Nodo 
{
    public:
        int getId();
        // retorna o ID do nodo
        int getGrau();
        // retorna o grau do nodo
        char getRotulo();
        // retorna o rotulo do nodo
    private:
        char _rotulo;
        int _id;
        int _grau;
};

#endif