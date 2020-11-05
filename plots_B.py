import numpy as np
import matplotlib.pyplot as plt

xang=np.genfromtxt("PMT_ang_acc.txt").transpose()[0]
yang=np.genfromtxt("PMT_ang_acc.txt").transpose()[1]

xQE=np.genfromtxt("QEpmt.txt").transpose()[0]
yQE=np.genfromtxt("QEpmt.txt").transpose()[1]

xwater=np.genfromtxt("water_len.txt").transpose()[0]
ywater=np.genfromtxt("water_len.txt").transpose()[1]
ywater2=np.genfromtxt("water_len.txt").transpose()[2]


plt.plot(xang,yang)
plt.show()

plt.plot(xQE,yQE)
plt.show()

plt.plot(xwater,ywater)
plt.show()

plt.plot(xwater,ywater2)
plt.show()
