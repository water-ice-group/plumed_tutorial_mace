# Download PLUMED

Before doing anything, ensure that you have installed and compiled a working version of PLUMED. This will be important for later on during post analysis. Details on installation can be found here: https://www.plumed.org/doc-v2.9/user-doc/html/_installation.html

# Create MACE environment. 
Setting up the MACE-ASE-PLUMED interface is most easily achieved by using `conda` to create a new virtual environment. Follow the instructions below to create this environment and install the necessary modules for running our calculations. Ensure that you have `python3.9` or higher. 

```python
conda create env -n plumed_mace
conda activate plumed_mace
conda install pip

# install ase
pip install --upgrade ase

# install the python wrap of ase
conda install -c conda-forge py-plumed

# install mace
pip install mace-torch
```

And that's it. When performing the tutorial tasks, always ensure to activate the virtual environment: `conda activate plumed_mace`. 


