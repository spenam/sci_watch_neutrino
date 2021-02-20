import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate


def find_nearest_index(array, value):
	array = np.asarray(array)
	idx = (np.abs(array - value)).argmin()
	return idx
	    

b=0.835 # parameter b of the scattering
f=(1./4.*np.pi)*(3./(3.+b))
#Lscat=813.709090
Lscat=441.8851

ang=np.load("ang_interp.npy")


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

def integrand(s0,d0,delta0):
	coslaw=np.sqrt(s0**2.+d0**2.+2.*s0*d0*np.cos(delta0))
	return (np.exp(-(s0+coslaw)/39.281818)
		*(np.exp(-s0/Lscat)/Lscat)*ang[1][find_nearest_index(ang[0],np.cos(np.arcsin(s0*np.sin(delta0)/coslaw)))]
		*f*(1.+b*np.cos(d0*np.sin(delta0)/coslaw)**2.)*1./coslaw**2.)
def integral(d0,delta0):
	return integrate.quad(integrand, 0., 500., args=(d0, delta0))[0]

vecintegra=np.vectorize(integral)
deltas=np.linspace(-np.pi+0.01,np.pi-0.01,100)
#resu=vecintegra(100.0,deltas)
#plt.plot(deltas,resu)
#plt.show()
print("#for d=350m lambda=500nm")
print("#cos(delta)	rate")
for i in deltas:
	print (np.cos(i), integral(350.0,i))
#print(np.cos(-np.pi),integral(150.0,-np.pi))

