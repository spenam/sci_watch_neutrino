#include "W_Abs.h"
#include "W_Sca.h"
#include "PMT_QE.h"
#include "PMT_Ang.h"

// isotropic light source, scattering neglected Fig. 4c, Fig. 6b

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
 double dist;
 cout << "Distance (m) ? " << endl;
 cin >> dist;

 double PxAng  = xAng->Get(0.998); // probability for photon on PMT
 double xa = xAbs->Get(lam); // absorption length
 double Pq = xQE->Get(lam); // quantum efficiency
 double spher = 4.*pi*dist*dist;// surface sphere of radius dist (for sr calculation with PMT)
 double Pabs = exp(-(dist)/xa); // probability of non-absorption on full photon path
 double rate = ratdef * human * lum * Aeff3inch/spher * Pabs * PxAng * Pq;
 cout << "Rate " << rate << " Hz " << endl;
}
