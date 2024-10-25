import matplotlib.pyplot as plt
import numpy as np

fin = np.loadtxt('./md.log',skiprows=1)

time  = fin[:,0]
e_tot = fin[:,1]
e_pot = fin[:,2]
e_kin = fin[:,3]
temp  = fin[:,4]


# plotting 
fin,ax=plt.subplots(4,1,figsize=(10,8))

ax[0].plot(time,e_tot)
ax[0].set_xlabel('Time  (ps)')
ax[0].set_ylabel('Total Energy  (eV)')


ax[1].plot(time,e_pot)
ax[1].set_xlabel('Time  (ps)')
ax[1].set_ylabel('Pot. Energy  (eV)')


ax[2].plot(time,e_kin)
ax[2].set_xlabel('Time  (ps)')
ax[2].set_ylabel('Kin. Energy  (eV)')


ax[3].plot(time,temp)
ax[3].set_xlabel('Time  (ps)')
ax[3].set_ylabel('Temp  (K)')


plt.show()
