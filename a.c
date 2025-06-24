#include <stdio.h>

struct complex{
    double real;
    double imag;
};
typedef struct complex Complex;

void mult(const Complex *z1, const Complex *z2, Complex *result){
    result->real = z1->real * z2->real - z1->imag * z2->imag;
    result->imag = z1->real * z2->imag + z1->imag * z2->real;
}

int main(void){
    Complex z1 = {2.0, -0.5};
    Complex z2 = {3.3, 1.8};
    Complex z3;

    mult(&z1, &z2, &z3);
    printf("z3 = %.2f + %.2fi\n", z3.real, z3.imag);
    return 0;
}
