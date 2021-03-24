#include "func.h"
#include <iostream>
#include <string.h>
#include<math.h>

using namespace op;

Complex num[2];

std::string Op::soma(double re1, double im1, double re2, double im2)
{
    double r = re1 + re2;
    double i = im1 + im2;
    return std::to_string(r) + "+" + std::to_string(i) + "i";
}

std::string Op::sub(double re1, double im1, double re2, double im2)
{
    double r = re1 - re2;
    double i = im1 - im2;
    return std::to_string(r) + "+" + std::to_string(i) + "i";
}

std::string Op::mult(double re1, double im1, double re2, double im2)
{
    double r = (re1 * re2) - (im1 * im2);
    double i = (re1 * im2) + (im1 * re2);
    return std::to_string(r) + "+" + std::to_string(i) + "i";
}

std::string Op::div(double re1, double im1, double re2, double im2)
{
    double r = ((re1 * re2) + (im1 * im2))/(re2*re2 + im2*im2);
    double i = ((im1 * re2) - (re1 * im2))/((re2*re2) + (im2*im2));
    return std::to_string(r) + "+" + std::to_string(i) + "i";
}

std::string Op::polarToret(double mod, double fase)
{
    fase = fase*M_PI/180;
    double i = mod*sin(fase);
    double r = mod * cos(fase);
    return std::to_string(r) + "+" + std::to_string(i) + "i";
}

std::string Op::retTopolar(double re, double im)
{
    double mod = sqrt(re*re + im*im);
    double fase = (atan(im/re) * 180 / M_PI);
    return "Módulo: " + std::to_string(mod) + ", Fase: " + std::to_string(fase);
}