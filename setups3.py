import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--wavelength", type=float, help="Insert wavelength of the source in nm, default is 500nm", default=500)
args=parser.parse_args()
wl=args.wavelength

def find_nearest_index(array, value):
	array = np.asarray(array)
	idx = (np.abs(array - value)).argmin()
	return idx
	    

b=0.835 # parameter b of the scattering
f=(1./(4.*np.pi))*(3./(3.+b))
if wl<451:
	Cl=20.
elif wl >649:
	Cl=20.
elif wl==500:
	Cl=2.
elif wl==550:
	Cl=1.
elif wl==600:
	Cl=2.
elif wl==525:
	Cl=1.5

Apmt=45.36*10.**-4.
C0=4.11*10.**15.
ang=np.loadtxt("pmt_ang_interp.txt").transpose()
qe=np.loadtxt("pmt_qe_interp.txt").transpose()
wabs=np.loadtxt("water_abs_interp.txt").transpose()
wscatt=np.loadtxt("water_scatt_rayleight.txt").transpose()
QE=qe[1][find_nearest_index(qe[0],wl)]*0.01
Lscat=wscatt[1][find_nearest_index(wscatt[0],wl)]
Labs=wabs[1][find_nearest_index(wabs[0],wl)]
print(QE, Lscat, Labs, Cl)

def count_rate(lambda0, d0, x0, delta0, alfa0, beta0, b0):
    """
    Function that returns the integral
    of the photon count rates as a function of the
    wavelength lambda0, the distance d of the source
    and the detector, and delta0 which is the angle of
    the detector and the source as a function of the scattering
    location
    """
    #s=symbols("s")
    return integrate.quad(lambda s: Pabs(lambda0,s,x0)*dPsca(lambda0,s)*Ppmt(alfa0)*dpsca(beta0,b0)*Apmt/x0**2.,0,+inf)


def Lsca(lambda0):
    """
    Function that computes the rayleigh scattering in its
    wavelength dependency. The dimension of the floats
    is in nanometers, as well as the lambda0.
    """
    if lambda0<0.01:
        lambda0=lambda0*10.**9.
    return (lambda0/550.0)**4.32 *667.0

#lambdas=np.linspace(350,650,10000)
#ray_scate=Lsca(lambdas)


def dpsca(beta0,b0):
    """
    Function that computes the rayleigh scattering in its
    angular probability profile dp_{sca}/d\Omega.
    """
    return (1./4. *np.pi)*(3./(3.+b0))*(1+b0*np.cos(beta0)**2.)

def dPsca(lambda0,s0):
    """
    Function that computes the differential probability of
    scattering process at point s.
    """
    return (np.exp(-s/Lsca(lambda0)))/Lsca(lambda0)

def Pabs(lambda0,s0,x0):
    """
    Function that computes the probability for a photon to arrive
    unabsorbed at the PMT after a distance s0+x0.
    """
    return(np.exp(-(s0+x0)/Labs(lambda0)))

def integrand_s1(s0,d0,delta0):
	coslaw=np.sqrt(s0**2.+d0**2.+2.*s0*d0*np.cos(delta0))
	return (np.exp(-(s0+coslaw)/Labs)
		*(np.exp(-s0/Lscat)/Lscat)*ang[1][find_nearest_index(ang[0],np.cos(np.arcsin(s0*np.sin(delta0)/coslaw)))]
		*f*(1.+b*np.cos(d0*np.sin(delta0)/coslaw)**2.)*1./coslaw**2.)
def integrand_s2(s0,delta0,d0):
	coslaw=np.sqrt(s0**2.+d0**2.+2.*s0*d0*np.cos(delta0))
	return (np.exp(-(s0+coslaw)/Labs)
		*(np.exp(-s0/Lscat)/Lscat)*ang[1][find_nearest_index(ang[0],np.cos(np.arcsin(s0*np.sin(delta0)/coslaw)))]
		*f*(1.+b*np.cos(d0*np.sin(delta0)/coslaw)**2.)*1./coslaw**2.)
def integral_s1(d0,delta0):
	return integrate.quad(integrand_s1, 0., 500., args=(d0, delta0))[0]
def integral_s2(d0):
	return integrate.nquad(integrand_s2, [[0.,500.],[0., np.pi/2.]], args=[d0])[0]

def integrand_s3(d0):
	return (np.exp(-(d0)/Labs)*ang[1][find_nearest_index(ang[0],np.cos(0))]*1./d0**2./(4.*np.pi))


vecintegra=np.vectorize(integral_s2)
deltas=np.linspace(-np.pi+0.01,np.pi-0.01,100)
ds=np.linspace(100,350,100)
#print("#for d=350m lambda=500nm")
#print("#cos(delta)	rate")
#for i in deltas:
#	print (np.cos(i), integral(350.0,i))

const=QE*C0*Cl*Apmt
header="#for lambda={}nm\n#Distance	rate".format(wl)
fil = open("data_setup3/counts_lambda{}nm.txt".format(int(wl)),"wb")
np.savetxt(fil, [], header=header)
for i in ds:
	data=np.column_stack((i,const*integrand_s3(i)))
	np.savetxt(fil, data)
fil.close()
