import numpy as np
import matplotlib.pyplot as plt
for i in [100,150,200,250,300,350]:
	data=np.genfromtxt("counts_distance{}m.txt".format(i)).transpose()

	plt.plot(data[0],data[1],label=r"$d={}m$".format(i))

plt.xlabel(r"$\cos (\delta)$")
plt.ylabel(r"Rate (Hz)")
plt.ylim([10,10**7])
plt.xlim([-1,1])
plt.grid("True")
plt.yscale("log")
plt.legend()
plt.tight_layout()
plt.savefig("first_rates.pdf")
plt.show()
