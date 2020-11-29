#include "W_Abs.h"

W_Abs::W_Abs(string fname)
{

 int nmax=100;
 int nr=0;
 double lam[nmax];
 double abs[nmax];
 double sca[nmax];
 string fab("Abs.txt");
 if (!fname.empty()) fab = fname;
 ifstream fAB;
 fAB.open(fab.c_str());
 if (fAB.is_open())
 {
    while ( ! fAB.eof() )
    {
      fAB >> lam[nr] >> abs[nr] >> sca[nr];
      nr++;
      if (nr == nmax) break;
    }
    fAB.close();
    nr--;
 }
 grAbs = new TGraph(nr,lam,abs);

}

double W_Abs::Get(double lam) {
 double x = grAbs->Eval(lam);
 if (x<0) x = 0;
 return x;
}
