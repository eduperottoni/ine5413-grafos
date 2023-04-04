//! Copyright [year] <Copyright Owner>
#ifndef STRUCTURES_LISTAENCADEADA_H
#define STRUCTURES_LISTAENCADEADA_H

#include <cstdint>
#include <stdexcept>

template<typename T>
class ListaEncadeada {
 public:
    // Construtor
    ListaEncadeada();
    //! ...
    ~ListaEncadeada();  // destrutor
    //! ...
    void clear();  // limpar lista
    //! ...
    void push_back(const T& data);  // inserir no fim
    //! ...
    void push_front(const T& data);  // inserir no início
    //! ...
    void insert(const T& data, std::size_t index);  // inserir na posição
    //! ...
    void insert_sorted(const T& data);  // inserir em ordem
    //! ...
    T& at(std::size_t index);  // acessar um elemento na posição index
    //! ...
    T pop(std::size_t index);  // retirar da posição
    //! ...
    T pop_back();  // retirar do fim
    //! ...
    T pop_front();  // retirar do início
    //! ...
    void remove(const T& data);  // remover específico
    //! ...
    bool empty() const;  // lista vazia
    //! ...
    bool contains(const T& data) const;  // contém
    //! ...
    std::size_t find(const T& data) const;  // posição do dado
    //! ...
    std::size_t size() const;  // tamanho da lista

 private:
    class Node {  // Elemento
     public:
        explicit Node(const T& data):
            data_{data}
        {}

        Node(const T& data, Node* next):
            data_{data},
            next_{next}
        {}

        T& data() {  // getter: dado
            return data_;
        }

        const T& data() const {  // getter const: dado
            return data_;
        }

        Node* next() {  // getter: próximo
            return next_;
        }

        const Node* next() const {  // getter const: próximo
            return next_;
        }

        void next(Node* node) {  // setter: próximo
            next_ = node;
        }

     private:
        T data_;
        Node* next_{nullptr};
    };

    Node* end() {  // último nodo da lista
        auto it = head;
        for (auto i = 1u; i < size(); ++i) {
            it = it->next();
        }
        return it;
    }

    Node* head{nullptr};
    std::size_t size_{0u};
};

// namespace structures

#endif

template<typename T>
ListaEncadeada<T>::ListaEncadeada() {
    size_ = 0;
    head = nullptr;
}

template<typename T>
ListaEncadeada<T>::~ListaEncadeada() {
    clear();
}

template<typename T>
void ListaEncadeada<T>::clear() {
    while (!empty()) {
        pop_front();
    }
}

template<typename T>
void ListaEncadeada<T>::push_back(const T& data) {
    if (empty()) {
        push_front(data);
    } else {
        Node *p;
        p = head;
        while (p->next() != nullptr) {
            p = p->next();
        }
        Node *novo = new Node(data);
        novo->next(nullptr);
        p->next(novo);
        size_++;
    }
}

template<typename T>
void ListaEncadeada<T>::push_front(const T& data) {
    Node *novo = new Node(data);
    novo->next(head);
    head = novo;
    size_++;
}

template<typename T>
T ListaEncadeada<T>::pop_front() {
    if (empty())
        throw std::out_of_range("lista vazia");

    Node *p;
    p = head;

    head = p->next();

    T saida = p->data();
    delete p;

    size_--;

    return saida;
}

template<typename T>
void ListaEncadeada<T>::insert(const T& data, std::size_t index) {
    if (index > size_ || index < 0) {
        throw std::out_of_range("fora de alcance");
    } else if (index == 0) {
        return push_front(data);
    } else if (index == size_-1) {
        return push_back(data);
    } else {
        Node *p;
        p = head;
        for (int i = 1; (std::size_t)i < index; i++) {
            p = p->next();
        }
        Node *novo = new Node(data);
        novo->next(p->next());
        p->next(novo);

        size_++;
    }
}

template<typename T>
void ListaEncadeada<T>::insert_sorted(const T& data) {
    if (empty()) {
        return push_front(data);
    }

    Node *p;
    p = head;

    Node* q;
    q = nullptr;

    while (p != nullptr && data > p->data()) {
        q = p;
        p = p->next();
    }
    if (q != nullptr) {
        Node *novo = new Node(data);
        novo->next(p);
        q->next(novo);
    } else {
        return push_front(data);
    }
    size_++;
}

template<typename T>
T& ListaEncadeada<T>::at(std::size_t index) {
    if ((empty()) || (index > size_ - 1)) {
        throw std::out_of_range("pilha vazia");
    }
    Node *p;
    p = head;
    for (int i = 0; (std::size_t)i < index; i++) {
        p = p->next();
    }
    return p->data();
}

template<typename T>
T ListaEncadeada<T>::pop(std::size_t index) {
    if (empty())
        throw std::out_of_range("lista vazia");

    if (index > size_-1 || index < 0)
        throw std::out_of_range("fora de alcance");

    if (size_ == 1 || index == 0) {
        return pop_front();
    }
    if (index == size_-1) {
        return pop_back();
    }

    Node *p;
    p = head;

    for (int i = 1; (std::size_t)i < index; i++) {
        p = p->next();
    }

    Node *aux;
    aux = p->next();
    p->next(aux->next());

    T saida = aux->data();

    delete aux;

    size_--;

    return saida;
}

template<typename T>
T ListaEncadeada<T>::pop_back() {
    if (empty())
        throw std::out_of_range("lista vazia");

    if (size_ == 1)
        return pop_front();

    Node *p;
    p = head;

    for (int i = 1; (std::size_t)i < size_-1; i++) {
        p = p->next();
    }

    T saida = p->next()->data();

    delete p->next();
    p->next(nullptr);

    size_--;

    return saida;
}

template<typename T>
void  ListaEncadeada<T>::remove(const T& data) {
    if (empty())
        throw std::out_of_range("lista vazia");

    Node *p;
    p = head;

    for (int i = 0; (std::size_t)i < size_; i++) {
        if (p->data() == data) {
            pop(i);
            return;
        }
        p = p->next();
    }
}

template<typename T>
bool ListaEncadeada<T>::empty() const {
    return (size_ == 0);
}

template<typename T>
bool ListaEncadeada<T>::contains(const T& data) const {
    if (empty()) {
        throw std::out_of_range("lista vazia");
    }
    Node *p;
    p = head;
    while ((p->data() != data) && (p->next() != nullptr)) {
        p = p->next();
    }
    return (p->data() == data);
}

template<typename T>
std::size_t ListaEncadeada<T>::find(const T& data) const {
    if (empty()) {
        throw std::out_of_range("lista vazia");
    }
    Node *p;
    p = head;
    size_t index = 0;
    while ((p->data() != data) && (p->next() != nullptr)) {
        index++;
        p = p->next();
    }
    if (p->data() == data) {
        return index;
    } else {
        index = index + 1;
        return index;
    }
}

template<typename T>
std::size_t ListaEncadeada<T>::size() const {
    return size_;
}
