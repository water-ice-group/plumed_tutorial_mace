# Download PLUMED

Before proceeding, ensure that you have installed and compiled a working version of PLUMED. This will be important for later on during post analysis. Details on installation can be found here: https://www.plumed.org/doc-v2.9/user-doc/html/_installation.html

# Create MACE environment 
Setting up the MACE-ASE-PLUMED interface is most easily achieved by using `conda` to create a new virtual environment. Follow the instructions below to create this environment and install the necessary modules for running our calculations. Ensure that you have `python3.9` or higher. 

```python
# 1. Create a clean environment 
conda create -n plumed_mace_legacy python=3.9 

# 2. Activate it
conda activate plumed_mace_legacy

# 3. Install py-plumed and a compatible NumPy version first
conda install -c conda-forge py-plumed "numpy<2.0" 

# 4. Install ASE
pip install ase

# 5. Install MACE
pip install mace-torch
```

And that's it. When performing the tutorial tasks, always ensure to activate the virtual environment: `conda activate plumed_mace`. 


