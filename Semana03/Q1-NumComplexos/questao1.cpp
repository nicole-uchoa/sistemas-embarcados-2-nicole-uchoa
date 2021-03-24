#include <iostream>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include "func.h"

using namespace std;
using namespace op;

int main(int argc, char *argv[])
{
    Op operacao;
    Complex num[2];
    int x;

    cout << "Escolha: 1-soma, 2-subtração, 3-divisão, 4-multiplicação, 5-polar para retangular 6-retangular para polar ";
    cin >> x;
    
    if (x == 1 || x == 2 || x == 3 || x == 4)
    {
        cout << "Parte real do primeiro número: ";
        cin >> num[0].re;
        cout << "Parte imaginária: ";
        cin >> num[0].im;
        cout << "Parte real do segundo número: ";
        cin >> num[1].re;
        cout << "Parte imaginária: ";
        cin >> num[1].im;

        switch (x)
        {
        case 1:
            cout << operacao.soma(num[0].re, num[0].im, num[1].re, num[1].im) << endl;
            break;
        case 2:
            cout << operacao.sub(num[0].re, num[0].im, num[1].re, num[1].im) << endl;
            break;
        case 3:
            cout << operacao.div(num[0].re, num[0].im, num[1].re, num[1].im) << endl;
            break;
        case 4:
            cout << operacao.mult(num[0].re, num[0].im, num[1].re, num[1].im) << endl;
            break;
        }
    }
    else if (x == 5)
    {
        cout << "Módulo: ";
        cin >> num[0].re;
        cout << "Fase: ";
        cin >> num[0].im;
        cout << operacao.polarToret(num[0].re, num[0].im) << endl;
    }
    else if (x == 6)
    {
        cout << "Parte Real: ";
        cin >> num[0].re;
        cout << "Parte Imaginária: ";
        cin >> num[0].im;
        cout << operacao.retTopolar(num[0].re, num[0].im) << endl;
    }
    else
    {
        cout << "Comando inválido" << endl;
    }
}