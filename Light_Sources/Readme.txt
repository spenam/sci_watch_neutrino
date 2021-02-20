libPMT.so - shared library with PMT and water repsonse functions below
----------------
PMT_QE - PMT quantum efficiency as function of wavelength
PMT_Ang - PMT angular acceptance as fucntion of PMT-photon angle
W_Abs - water absorption length as function of wavelength
W_Sca - water Raleigh scattering length as function of wavelength
----------------
Rates for an PMT pointing towards the light source
Rate_head - calculates PMT rate from an isotropic light source ignoring scattering (Fig. 4a, Fig. 6b)
Rate_back - calculates PMT rate from an semi-isotropic light source pointing away from PMT (Fig. 4b, Fig. 6a)
Rate  - calculates PMT rate from an unidirectional light source (Fig. 4a, Fig.5)

all programs need as input 
---
a) wave length (nm)
b) human conversion factor 
c) brightness (lm)
d) distance (m)
e) angle between light direction and PMt axis (only Rate)
