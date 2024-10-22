# Running Free MD

Having now set up your MACE-ASE environment, let's start running some MD. 

Open the file `mace.py`. You should see the following code:

```python
from ase import units
from ase.md.langevin import Langevin
from ase.io import read, write
import numpy as np
import time

from mace.calculators import MACECalculator

calculator = MACECalculator(model_path='/content/checkpoints/MACE_model_run-123.model', device='cuda')
init_conf = read('BOTNet-datasets/dataset_3BPA/test_300K.xyz', '0')
init_conf.set_calculator(calculator)

dyn = Langevin(init_conf, 0.5*units.fs, temperature_K=310, friction=5e-3)
def write_frame():
        dyn.atoms.write('md_3bpa.xyz', append=True)
dyn.attach(write_frame, interval=50)
dyn.run(100)
print("MD finished!")
```

Here, we can see that we are running MD at 300 K with a 0.5 fs timestep for a total of 1000 steps. Feel free to change some of these parameters and see how this changes the resulting trajectory. Notice the use of the MACE calculator, which we use to compute the energies and forces during the MD runs of the generater structures. 

Now, once you have familiarised yourself with the `mace.py` file, run the following command: `python mace.py`. This should start the simulation. You should notice an output file `free_md.xyz`, which contains the coordinates of the generated trajectory. 
