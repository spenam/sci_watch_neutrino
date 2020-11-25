import numpy as np
import matplotlib.pyplot as plt
import matplotlib
fig, ax= plt.subplots()
for i in [100,150,200,250,300,350]:
	data=np.genfromtxt("data_test/counts_distance{}m.txt".format(i)).transpose()

	ax.plot(data[0],data[1],label=r"$d={}m$".format(i))

plt.xlabel(r"$cos\theta$")
plt.ylabel(r"Rate (Hz)")
ax.grid("True")
ax.set_yscale("log")
plt.ylim([10**(-2),10**8])
plt.xlim([-1,1])
locmaj=matplotlib.ticker.LogLocator(base=10,numticks=11)
ax.yaxis.set_major_locator(locmaj)
locmin = matplotlib.ticker.LogLocator(base=10.0,subs=(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9),numticks=11)
ax.yaxis.set_minor_locator(locmin)
ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.legend()
plt.tight_layout()
plt.savefig("test_rates.pdf")
plt.show()
