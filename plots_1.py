import numpy as np
import matplotlib.pyplot as plt
import matplotlib
fig, ax= plt.subplots()
for i in [100,150,200,250,300,350]:
	data=np.genfromtxt("data_setup1/counts_distance{}m.txt".format(i)).transpose()

	ax.plot(data[0],data[1],label=r"$d={}m$".format(i))

plt.xlabel(r"$\cos \delta$")
plt.ylabel(r"Rate (Hz)")
ax.grid("True")
ax.set_yscale("log")
plt.ylim([10,10**7])
plt.xlim([-1,1])
plt.xticks(np.arange(min(data[0]),max(data[0])+0.2,0.2))
ax.legend()
plt.tight_layout()
plt.savefig("first_rates.pdf")
plt.show()
