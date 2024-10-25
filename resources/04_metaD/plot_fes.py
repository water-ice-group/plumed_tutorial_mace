import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from scipy.interpolate import griddata

# load 
fin = np.loadtxt('./fes.dat')
x = np.degrees(fin[:, 0])
y = np.degrees(fin[:, 1])
z = fin[:, 2] * 23.0609
x[x < -90] += 360
y[y < -90] += 360
xnew, ynew = np.meshgrid(np.linspace(-90, 270, num=len(np.unique(x))),
                         np.linspace(-90, 270, num=len(np.unique(y))))
znew = griddata((x, y), z, (xnew, ynew), method='linear')
znew -= np.nanmin(znew)

# plot
max_val = 10 # change to alter appearance of figure
fig, ax = plt.subplots()
levels = np.round(np.linspace(0, max_val, 2*int((max_val))),1)
cs = ax.contourf(xnew,ynew,znew,
                  vmin=0,vmax=max_val,
                  levels=levels,
                  cmap=cm.inferno)
cbar = fig.colorbar(cs)
cbar.ax.set_ylabel('Free Energy  (kcal/mol)')

ax.set_xlabel(r'$\phi$  (degrees)',size=12)
ax.set_ylabel(r'$\theta$  (degrees)',size=12)

plt.savefig('./conf_free_energy.png',dpi=400,bbox_inches='tight',transparent=False, edgecolor='none')
plt.show()
