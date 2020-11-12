import numpy as np
import matplotlib.pyplot as plt
import matplotlib
fig, ax= plt.subplots()
for i in [350,400,450,500,525,550,600]:
	data=np.genfromtxt("data_setup3/counts_lambda{}nm.txt".format(i)).transpose()

	ax.plot(data[0],data[1],label=r"$\lambda={}nm$".format(i))

plt.xlabel(r"$Distance\qquad [m]$")
plt.ylabel(r"Rate (Hz)")
ax.grid("True")
ax.set_yscale("log")
ax.tick_params(axis="both", which="both")
plt.ylim([0.01,10**8])
plt.xlim([100,350])
locmaj=matplotlib.ticker.LogLocator(base=10,numticks=11)
ax.yaxis.set_major_locator(locmaj)
locmin = matplotlib.ticker.LogLocator(base=10.0,subs=(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9),numticks=11)
ax.yaxis.set_minor_locator(locmin)
ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.legend(loc="upper right")
plt.tight_layout()
plt.savefig("third_rates.pdf")
plt.show()
