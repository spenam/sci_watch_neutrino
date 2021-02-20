import numpy as np
import matplotlib.pyplot as plt
import matplotlib
fig, ax= plt.subplots()
#for i in [100,150,200,250,300,350]:
for i in [150,250,350]:
    levels=np.linspace(-3,5.5,101)
    data=np.genfromtxt("data_test/counts_azimuth_distance{}m_2pi.txt".format(i)).transpose()
    zdata=np.reshape(data[2][0:10000],(100,100))
    xdata=np.reshape(data[1][0:10000],(100,100))
    ydata=np.reshape(data[0][0:10000],(100,100))
    plt.contourf(xdata/np.pi,np.cos(ydata),np.log10(zdata),levels=levels,cmap="plasma",vmin=-2.)
#	plt.imshow(np.log10(zdata),origin="lower",cmap="inferno")

    plt.xlabel(r"$\phi$ $\pi rad$")
    plt.ylabel(r"$\cos\theta$")
    cbar=plt.colorbar()
    cbar.set_label("log10 Rates [Hz]")
    plt.tight_layout()
    plt.show()
#ax.set_yscale("log")
#plt.ylim([10**(-2),10**8])
#plt.xlim([-1,1])
#locmaj=matplotlib.ticker.LogLocator(base=10,numticks=11)
#ax.yaxis.set_major_locator(locmaj)
#locmin = matplotlib.ticker.LogLocator(base=10.0,subs=(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9),numticks=11)
#ax.yaxis.set_minor_locator(locmin)
#ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
#ax.legend()
#plt.tight_layout()
#plt.savefig("test_azimuth_rates.pdf")
#plt.show()
