from ase import units
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md import MDLogger
from ase.io import read, write
import numpy as np
import time
import os

from mace.calculators import MACECalculator

calculator = MACECalculator(model_paths='../model/co2-h2o_swa.model', device='cpu')

init_conf = read('init.xyz', '0')
init_conf.pbc = True
init_conf.cell = [12.42, 12.42, 12.42]
init_conf.set_calculator(calculator)

MaxwellBoltzmannDistribution(init_conf, temperature_K=300)

dyn = Langevin(init_conf, 0.5*units.fs, temperature_K=300, friction=5e-2)
def write_frame():
            dyn.atoms.write('traj.xyz', append=True)
dyn.attach(write_frame, interval=10)
dyn.attach(MDLogger(dyn, init_conf, 'md.log', header=True, stress=False,
                           peratom=True, mode="a"), interval=1)
dyn.run(1000)
print("MD finished! Congratulations!")
