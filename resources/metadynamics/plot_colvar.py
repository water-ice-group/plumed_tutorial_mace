import matplotlib.pyplot as plt
import numpy as np

fin = np.loadtxt('./COLVAR')
time = fin[:,0]
colv_1 = fin[:,1]
colv_2 = fin[:,2]

# plot 
fin,ax=plt.subplots()
ax.plot(time,colv_1,label=r'$\phi$')
ax.plot(time,colv_2,label=r'$\theta$') 

ax.set_xlabel('Time  (ps)')
ax.set_ylabel('Angle  (degrees)')

plt.show()
