# Using MACE to run umbrella sampling over a single CV

Now we can run some simple MD, let's add in some enhanced sampling. Specifically, in this section, we will be using PLUMED to drive a conformational change in our carbonic acid molecule. 

In the folder `task_2`, look at the file `mace.py` and notice the following addition: 

```python
setup = [f"UNITS LENGTH=A TIME={1/ps} ENERGY={units.mol/units.kcal}",
         "c1: COORDINATIONNUMBER SPECIES=1-7 MOMENTS=2-3" +
         " SWITCH={RATIONAL R_0=1.5 NN=8 MM=16}",
         "PRINT ARG=c1.* STRIDE=100 FILE=COLVAR",
         "FLUSH STRIDE=1000"]
```

This block contains the input parameters for our umbrella sampling run. 
