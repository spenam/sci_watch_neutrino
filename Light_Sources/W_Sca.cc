#include "W_Sca.h"

W_Sca::W_Sca(){}

double W_Sca::Get(double lam) {
 if (lam <= 0.) return 0;
 double x = 550./lam;
 return 1./(0.0015*pow(x,4.32));
}
double W_Sca::PAng(double ct) {
 double pi = 3.14159265359;
 double b  = 0.835;
 double a  = 1/(2.*pi) * 3./2. /(3.+b);
 if (ct < -1. || ct > 1.) return 0;
 return a*(1.+b*ct*ct);
}
