#include"modulo.h"
#include<iostream>

using namespace aux;

void Aux::move_disco(int d, char ori, char dest, char aux)
{
    if (d == 1)
    {
        std::cout << "Mover disco " << d << " de " << ori << " para " << dest << std::endl;
    }
    else
    {
        move_disco(d - 1, ori, dest, aux);
        std::cout << "Mover disco " << d << " de " << ori << " para " << dest << std::endl;
        move_disco(d-1,aux,dest,ori);
    }
}