import numpy as np
import matplotlib.pyplot as plt
a=1
if a==1:
	data100=np.genfromtxt("inte100.txt").transpose()
	data150=np.genfromtxt("inte150.txt").transpose()
	data200=np.genfromtxt("inte200.txt").transpose()
	data250=np.genfromtxt("inte250.txt").transpose()
	data300=np.genfromtxt("inte300.txt").transpose()
	data350=np.genfromtxt("inte350.txt").transpose()
else:
	data100=np.genfromtxt("inte1002.txt").transpose()
	data150=np.genfromtxt("inte1502.txt").transpose()
	data200=np.genfromtxt("inte2002.txt").transpose()
	data250=np.genfromtxt("inte2502.txt").transpose()
	data300=np.genfromtxt("inte3002.txt").transpose()
	data350=np.genfromtxt("inte3502.txt").transpose()

QE=0.1527
C0=4.11*10.**15.
Cl=2.
Apmt=45.36*10.**-4.
const=QE*C0*Cl*Apmt
print(const)
plt.plot(data100[0],const*data100[1],label=r"$d=100m$")
plt.plot(data150[0],const*data150[1],label=r"$d=150m$")
plt.plot(data200[0],const*data200[1],label=r"$d=200m$")
plt.plot(data250[0],const*data250[1],label=r"$d=250m$")
plt.plot(data300[0],const*data300[1],label=r"$d=300m$")
plt.plot(data350[0],const*data350[1],label=r"$d=350m$")

plt.xlabel(r"$\cos \delta$")
plt.ylabel(r"Rate (Hz)")
plt.grid("True")
plt.yscale("log")
plt.legend()
plt.tight_layout()
plt.savefig("rates{}.pdf".format(a))
plt.show()
