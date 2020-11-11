import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

pmt_ang=np.genfromtxt("PMT_ang_acc.txt").transpose()
pmt_qe=np.genfromtxt("QEpmt.txt").transpose()
water_len=np.genfromtxt("water_len.txt").transpose()

f=interp1d(pmt_ang[0],pmt_ang[1])
newx=np.linspace(-0.25,1,1001)
np.savetxt("pmt_ang_interp.txt",np.c_[np.append(np.linspace(-1,-0.25,1001)[:-1],newx),np.append(np.zeros(1000),f(newx))],header="cosalfa	Acceptance")

f=interp1d(pmt_qe[0],pmt_qe[1])
newx=np.linspace(270,710,1001)
np.savetxt("pmt_qe_interp.txt",np.c_[newx,f(newx)],header="#lambda	QE(%)")

f=interp1d(water_len[0],water_len[1])
newx=np.linspace(290,720,1001)
np.savetxt("water_abs_interp.txt",np.c_[newx,f(newx)],header="#lambda	lambda_abs")

f=lambda x: (x/550)**(4.32)*667
newx=np.linspace(300,700,1001)
np.savetxt("water_scatt_rayleight.txt",np.c_[newx,f(newx)],header="#lambda	lambda_scatt")

data=np.loadtxt("water_scatt_rayleight.txt").transpose()
plt.plot(data[0],data[1])
plt.show()
