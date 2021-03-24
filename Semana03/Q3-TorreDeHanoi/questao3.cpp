#include "modulo.h"
#include <iostream>

using namespace std;
using namespace aux;

int main(int argc, char *argv[])
{
    Aux f;
    int discos;
    
    cout << "Escreva a quantidade de discos: ";
    cin >> discos;

    f.move_disco(discos, 'A', 'B', 'C');

    return 0;
}