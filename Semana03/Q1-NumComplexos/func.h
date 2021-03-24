#ifndef _FUNC_H_
#define _FUNC_H_

#include <iostream>
#include <string.h>

namespace op
{
    struct Complex
    {
        double re, im;
    };
    class Op
    {
    public:
        std::string soma(double re1, double im1, double re2, double im2);
        std::string sub(double re1, double im1, double re2, double im2);
        std::string mult(double re1, double im1, double re2, double im2);
        std::string div(double re1, double im1, double re2, double im2);
        std::string polarToret(double mod, double fase);
        std::string retTopolar(double re, double im);
    };
}

#endif