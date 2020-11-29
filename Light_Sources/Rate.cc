#include "W_Abs.h"
#include "W_Sca.h"
#include "PMT_QE.h"
#include "PMT_Ang.h"

// photon rate for uni-directional light source, Fig. 4a , Fig.5

int main(int argc, char *argv[]){

// one Lumen at 555 nm = 4,11·10^15 Photons per second       

 double pi = 3.14159265359;
 double Aeff3inch = 0.004536; // effective area 3inch PMT [m^2]
 double ratdef = 4.11e15; // photon rate 1 lumen

 W_Abs* xAbs;
 xAbs = new W_Abs("Water_2018.txt");
 W_Sca* xSca;
 xSca = new W_Sca();
 PMT_QE* xQE;
 xQE = new PMT_QE("QE_2018.txt");
 PMT_Ang* xAng;
 xAng = new PMT_Ang();

 double lam;
 cout << "Wavelength (nm) ? " << endl;
 cin >> lam;
 double human;
 cout << "Human eye conversion factor ? " << endl;
 cin >> human;
 double lum;
 cout << "Brightness (lm) ? " << endl;
 cin >> lum;
 double ct;
 cout << "cos(angle) ? " << endl;
 cin >> ct;
 double dist;
 cout << "Distance (m) ? " << endl;
 cin >> dist;

 double xa = xAbs->Get(lam); // absorption length
 double xs = xSca->Get(lam); // scattering length
 double Pq = xQE->Get(lam); // quantum efficiency

   // loop over distance bins
   int ndist = 50000; // steps over 500m 
   double nmet  = 0.01; // step width (m)

   double rate = 0;
   double part = 0;
   for (int j=0;j<ndist;j++) {
    double xm = (j+0.5)*nmet; // mean distance of bin
    double Psca = nmet/xs*exp(-xm/xs); // probability of scattering inside bin
    double y = sqrt(dist*dist+xm*xm+2.*dist*xm*ct);// distance from scattering to PMT
    double Pabs = exp(-(y+xm)/xa); // probability of non-absorption on full photon path
    double cosa  = (-dist*dist + xm*xm + y*y)/(2.*xm*y); // scattering angle
    double cosb  = (-xm*xm + y*y + dist*dist)/(2.*y*dist);// PMT-photon angle
    // sanity check on angles
    if (abs((acos(-ct)+acos(cosa)+acos(cosb))/pi-1)>1e-6) cout << ct << " " << cosa << " " << cosb << endl;
    double PSAng  = xSca->PAng(cosa); // probability for angular scattering [1/sr]
    double PxAng  = xAng->Get(cosb); // probability for photon on PMT
    rate += ratdef * human * lum * Aeff3inch/y/y * Pabs * Psca * PSAng * PxAng * Pq;
    part +=y;
   }
 cout << "Rate " << rate << " Hz " << endl;
 cout << "part " << part  << endl;
 //cout << "part " << rate/(ratdef*human*lum*Aeff3inch*Pq)  << endl;
}
