# Using MACE to run umbrella sampling over a single CV

Now that we've run some simple MD, let us move on to the main task for this tutorial. In this section, we will be using PLUMED to drive a conformational change in our carbonic acid molecule. This molecule exists in three main conformations: cis-cis (CC), cis-trans (CT), and trans-trans (TT). It's up to you to determine which of these conformers is most stable, and which is least stable. 

---

Like in the previous task, we have a configuration file `init.xyz` and our ase file `mace.py`. Looking at the latter, you should see some noticeable changes to the code. The code below gives the PLUMED input needed to perform our enhanced sampling:

```
setup = [f"UNITS LENGTH=A TIME={1/ps} ENERGY={units.mol/units.kcal}",
          "t1: TORSION ATOMS=1,6,4,5",
          "t2: TORSION ATOMS=2,3,4,5",
          "mtd: METAD ARG=t1,t2 SIGMA=0.25,0.25 HEIGHT=0.6 PACE=100 FILE=HILLS" +
                " BIASFACTOR=10 TEMP=300",
          "PRINT ARG=t1.*,t2.*,mtd.* STRIDE=100 FILE=COLVAR"]
```
Line 1 gives the units used by PLUMED. Lines 2 and 3 define the collective variables (torsion) that we will use to probe the conformation change. Line 4 is used to define the parameters used in running metadynamics, including gaussian heights, widths, and the rate at which they are deposited. 


This block contains the input parameters for our umbrella sampling run. 
