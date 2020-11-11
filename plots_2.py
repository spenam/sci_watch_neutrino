import numpy as np
import matplotlib.pyplot as plt
for i in [350,400,450,500,550,600]:
	data=np.genfromtxt("counts_lambda{}nm.txt".format(i)).transpose()

	plt.plot(data[0],data[1],label=r"$\lambda={}nm$".format(i))

plt.xlabel(r"$Distance\qquad [m]$")
plt.ylabel(r"Rate (Hz)")
plt.grid("True")
plt.yscale("log")
plt.ylim([0.01,10**8])
plt.xlim([100,350])
plt.legend()
plt.tight_layout()
plt.savefig("second_rates.pdf")
plt.show()