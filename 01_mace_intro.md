# Machine-learned potentials for atomistic simulations

Over the last two decades, a drastic change has emerged in the way we simulate atomistic systems. Machine-learned potentials (MLPs) have enabled *ab-initio*-level accuracy in force and energy predictions for a fraction of the price associated with traditional methods. We can now access systems of a size and complexity that were previously inaccessible to accurate simulation. An overview of some of the major MLP developments and achievements can be found in this recent introductory review: [Introduction to machine learning potentials for atomistic simulations](https://arxiv.org/abs/2410.00626)

At the forefront of MLP development is the multi atomic cluster expansion (MACE) framework [1](https://arxiv.org/abs/2206.07697). Developed in 2022, this model combines a complete high body order polynomial basis, the so-called atomic cluster expansion, with a message-passing tensoral network. This architecture provides learnable representations of semi-local chemical environments to accurately reproduce reference *ab initio* energies and forces.

<img src="./img/mace.png" alt="drawing" width="400"/>
