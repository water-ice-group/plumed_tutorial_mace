from ase import units
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md import MDLogger
from ase.io import read, write
import numpy as np
import time
import os

from mace.calculators import MACECalculator
from ase.calculators.plumed import Plumed


timestep = 0.0005
ps = 1000*units.fs

calculator = MACECalculator(model_paths='../../model/co2-h2o_swa.model', device='cpu')

setup = [f"UNITS LENGTH=A TIME={1/ps} ENERGY={units.mol/units.kcal}",
          "t1: TORSION ATOMS=1,6,4,5",
          "t2: TORSION ATOMS=2,3,4,5",
          "mtd: METAD ARG=t1,t2 SIGMA=0.25,0.25 HEIGHT=0.6 PACE=100 FILE=HILLS" +
                " BIASFACTOR=5 TEMP=300",
          "PRINT ARG=t1.*,t2.*,mtd.* STRIDE=100 FILE=COLVAR"]

init_conf = read('init.xyz', '0')
init_conf.pbc = True
init_conf.cell = [12.42, 12.42, 12.42]

init_conf.calc = Plumed(calc=calculator,
                    input=setup,
                    timestep=timestep,
                    atoms=init_conf,
                    kT=0.6)

dyn = Langevin(init_conf, 0.5*units.fs, temperature_K=300, friction=5e-2)
def write_frame():
            dyn.atoms.write('traj.xyz', append=True)
dyn.attach(write_frame, interval=500)
dyn.attach(MDLogger(dyn, init_conf, 'md.log', header=True, stress=False,
                           peratom=True, mode="a"), interval=1)

dyn.run(2000000)
print("MD finished! Congratulations!")
