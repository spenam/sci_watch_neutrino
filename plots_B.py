import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size':14})

xang=np.genfromtxt("PMT_ang_acc.txt").transpose()[0]
yang=np.genfromtxt("PMT_ang_acc.txt").transpose()[1]

xQE=np.genfromtxt("QEpmt.txt").transpose()[0]
yQE=np.genfromtxt("QEpmt.txt").transpose()[1]

xwater=np.genfromtxt("water_len.txt").transpose()[0]
ywater=np.genfromtxt("water_len.txt").transpose()[1]
ywater2=np.genfromtxt("water_len.txt").transpose()[2]

plt.plot(xang,yang)
plt.grid(True)
plt.xlabel(r"$cos\alpha$")
plt.ylabel(r"Acceptance")
plt.tight_layout()
plt.savefig("ang_acc.pdf")
plt.show()

plt.plot(xQE,yQE)
plt.grid(True)
plt.xlabel(r"$\lambda$ [nm]")
plt.ylabel(r"$QE(\%)$")
plt.tight_layout()
plt.savefig("qe.pdf")
plt.show()

plt.plot(xwater,ywater)
plt.grid(True)
plt.xlabel(r"$\lambda$ [nm]")
plt.ylabel(r"$\lambda_{abs}$ [nm]")
plt.tight_layout()
plt.savefig("water_abs.pdf")
plt.show()

plt.plot(xwater,ywater2)
plt.grid(True)
plt.xlabel(r"$\lambda$ [nm]")
plt.ylabel(r"$\lambda_{sca}$ [m]")
plt.tight_layout()
plt.savefig("water_sca.pdf")
plt.show()
