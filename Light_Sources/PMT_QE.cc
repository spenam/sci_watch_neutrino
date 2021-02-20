#include "PMT_QE.h"

PMT_QE::PMT_QE(string fname)
{

 int nmax=100;
 int nr=0;
 double lam[nmax];
 double qe[nmax];
 string fqe("QE.txt");
 if (!fname.empty()) fqe = fname;
 ifstream fQE;
 fQE.open(fqe.c_str());
 if (fQE.is_open())
 {
    while ( ! fQE.eof() )
    {
      fQE >> lam[nr] >> qe[nr];
      nr++;
      if (nr == nmax) break;
    }
    fQE.close();
    nr--;
 }
 grQE = new TGraph(nr,lam,qe);

}

double PMT_QE::Get(double lam) {
 double x = grQE->Eval(lam);
 if (x<0) x = 0;
 return x/100.;
}
