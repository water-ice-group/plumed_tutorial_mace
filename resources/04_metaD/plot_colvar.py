import matplotlib.pyplot as plt
import numpy as np

fin = np.loadtxt('./COLVAR')
time = fin[:,0]
colv_1 = np.degrees(fin[:,1])
colv_2 = np.degrees(fin[:,2])
colv_1[colv_1 < -90] += 360
colv_2[colv_2 < -90] += 360
block_size = 10 # change depending on how much time has elapsed
colv_1_blocks = np.mean(colv_1[:len(colv_1)//block_size*block_size].reshape(-1, block_size), axis=1)
colv_2_blocks = np.mean(colv_2[:len(colv_2)//block_size*block_size].reshape(-1, block_size), axis=1)

# plot 
fig,ax=plt.subplots()
ax.plot(time[2::block_size],colv_1_blocks,label=r'$\phi$')
ax.plot(time[2::block_size],colv_2_blocks,label=r'$\theta$')

ax.set_xlabel('Time  (ps)',size=12)
ax.set_ylabel('Angle  (degrees)',size=12)

ax.legend()
plt.show()
