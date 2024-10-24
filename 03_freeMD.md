# Running Free MD

Having now set up your MACE-ASE-PLUMED environment, let's start running some MD. 

Open the file `mace.py`. You should see the following code:

```python
from ase import units
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md import MDLogger
from ase.io import read, write
import numpy as np
import time
import os

# A - define the calculator
from mace.calculators import MACECalculator
calculator = MACECalculator(model_paths='../model/co2-h2o_swa.model', device='cpu')

# B - load the initial configuration
init_conf = read('init.xyz', '0')
init_conf.set_calculator(calculator)

# C - set dynamics variables
MaxwellBoltzmannDistribution(init_conf, temperature_K=300)
dyn = Langevin(init_conf, 0.5*units.fs, temperature_K=300, friction=5e-2)

# D - output details
def write_frame():
            dyn.atoms.write('traj.xyz', append=True)
dyn.attach(write_frame, interval=10)
dyn.attach(MDLogger(dyn, init_conf, 'md.log', header=True, stress=False,
                           peratom=True, mode="a"), interval=1)

# E - run the simulation!
dyn.run(1000)
print("MD finished! Congratulations!")
```

In the above script, we first import the necessary modules to run our MD. In section A, we define the calculator for this simulation, i.e., the MACE model which will calculate the forces and energies needed to propagate the system. In section B, we load the initial configuration with periodic boundary conditions and defined box lengths. In C, we set the initial distribution of velocities and define the integrator needed to perform dynamics. In our case, we opt for a Maxwell Boltzmann distribution initial moment. Our _NVT_ simulations are run using Langevin dynamics, meaning that each atom is coupled to a heat bath through use of both a force and friction term. Section D dictates the nature of our output and how frequently it occurs, while in E we set the whole thing going. 

Now, once you have familiarised yourself with the `mace.py` file, run the following command: `python mace.py`. This will start the simulation. You should notice an output file `traj.xyz`, which contains the coordinates of the generated trajectory. The file `md.log` should also appear, containing the time, temperature, energy, etc. of each step. You can use the python file `plot.py` to visualise these properties as a function of time. Running this simulation should require no more than a minute or so of computational time, though you are free to increase the number of steps if you would like to acquire more statistics. 
