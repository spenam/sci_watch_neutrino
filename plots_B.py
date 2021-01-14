import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size':18})

xang=np.genfromtxt("PMT_ang_acc.txt").transpose()[0]
yang=np.genfromtxt("PMT_ang_acc.txt").transpose()[1]

xQE=np.genfromtxt("QEpmt.txt").transpose()[0]
yQE=np.genfromtxt("QEpmt.txt").transpose()[1]

xwater=np.genfromtxt("water_len.txt").transpose()[0]
ywater=np.genfromtxt("water_len.txt").transpose()[1]
xwater2=np.genfromtxt("water_scatt_rayleight.txt").transpose()[0]
ywater2=np.genfromtxt("water_scatt_rayleight.txt").transpose()[1]

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
plt.ylabel(r"$\lambda_{abs}$ [m]")
plt.tight_layout()
plt.savefig("water_abs.pdf")
plt.show()

plt.plot(xwater2,ywater2)
plt.grid(True)
plt.xlabel(r"$\lambda$ [nm]")
plt.ylabel(r"$\lambda_{sca}$ [m]")
plt.tight_layout()
plt.savefig("water_sca.pdf")
plt.show()
