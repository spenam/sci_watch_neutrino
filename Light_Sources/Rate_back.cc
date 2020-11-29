#include "W_Abs.h"
#include "W_Sca.h"
#include "PMT_QE.h"
#include "PMT_Ang.h"

// photon rate for 1 lumen uni-directional light source, angular average over backside (0,pi/2)
// dependency from distance for different wave lengths Fig. 4b , Fig. 6a

int main(int argc, char *argv[]){

// one Lumen at 555 nm = 4,11·10^15 Photons per second       

 double pi = 3.14159265359;
 double Aeff3inch = 0.004536; // effective area 3inch PMT [m^2]
 double ratdef = 4.11e15; // photon rate 1 lumen

 double ctmin = -1.;
 double ctmax =  0; 
 //double ctmax = -0.866; // 30deg 
 int Nbct = 1000;
 double delct=(ctmax-ctmin)/Nbct;

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
 double dist;
 cout << "Distance (m) ? " << endl;
 cin >> dist;

 double xa = xAbs->Get(lam); // absorption length
 double xs = xSca->Get(lam); // scattering length
 double Pq = xQE->Get(lam); // quantum efficiency

  // loop over distance bins
   int ndist = 500; // steps over 500m 
   int nmet  = 1; // step width (m)

   double rate = 0;
   double part = 0;
   for (int j=0;j<ndist;j++) {
    double xm = (j+0.05)*nmet; // mean distance of bin
    double Psca = nmet/xs*exp(-xm/xs); // probability of scattering inside bin
    for (int l=0;l<Nbct;l++) {
     double ct = ctmin + (l+0.5)*delct;
     double y = sqrt(dist*dist+xm*xm-2.*dist*xm*ct);// distance from scattering to PMT
     double Pabs = exp(-(y+xm)/xa); // probability of non-absorption on full photon path
     double cosa  = (-dist*dist + xm*xm + y*y)/(2.*xm*y); // scattering angle
     double cosb  = (-xm*xm + y*y + dist*dist)/(2.*y*dist);// PMT-photon angle
     // sanity check on angles
     if (abs((acos(ct)+acos(cosa)+acos(cosb))/pi-1)>1e-6) cout << ct << " " << cosa << " " << cosb << endl;
     double PSAng  = xSca->PAng(cosa); // probability for angular scattering [1/sr]
     double PxAng  = xAng->Get(cosb); // probability for photon on PMT
     rate   += ratdef * human * lum * Aeff3inch/y/y * Pabs * Psca * PSAng * PxAng * Pq / Nbct;
     part +=0;
    }
   }
 cout << "Rate " << rate << " Hz " << endl;
 cout << "part " << part << endl;
}
