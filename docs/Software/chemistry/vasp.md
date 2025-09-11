---
title: VASP
---
VASP (Vienna Ab initio Simulation Package) is a commercial software package for performing first-principles quantum mechanical calculations in materials science, chemistry, and physics. It is based primarily on density functional theory (DFT), with extensions for time-dependent DFT and many-body perturbation theory (e.g., GW and RPA).

VASP is particularly known for its efficient and accurate implementation of the projector augmented-wave (PAW) method, enabling precise electronic structure calculations. It supports geometry optimizations, molecular dynamics, phonon calculations, and band structure analysis, making it a powerful tool for studying molecules, solids, surfaces, and interfaces.

The code is optimized for massively parallel supercomputers and includes advanced iterative diagonalization and charge-density mixing algorithms for large-scale simulations. Although VASP itself does not include a GUI, it integrates seamlessly with a wide range of external tools for input generation and visualization of results.

## Availability

Since VASP is **licensed software**, access is restricted to the cluster. If your research group has a valid VASP license and wants to use it, please ask your advisor/PI to email [mailto:hpc@njit.edu](hpc@njit.edu) with the following details

1. UCIDs of the students who need access to VASP 
2. Licensed VASP version (e.g., 6.x or 5.x)
3. Proof of license (license confirmation/contract)


## Application Information, Documentation
The documentation of CP2K is available at [VASP Documentation](https://vasp.at/wiki/The_VASP_Manual). For any issues in VASP simulation, users can contact at [VASP Forum](https://www.vasp.at/forum/). 

## Using VASP

CP2K MPI/OpenMP-hybrid Execution (PSMP), CP2K with Population Analysis capabilities- CP2K-popt

??? example "Sample Batch Script to Run CP2K : cp2k.submit.sh"

    ```slurm
    #!/bin/bash -l
    #SBATCH -J VASP
    #SBATCH -o vasp.out
    #SBATCH -e vasp.err
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=16
    #SBATCH --mem-per-cpu=4G
    #SBATCH --qos=standard
    #SBATCH --partition=general
    #SBATCH --account=PI_ucid # Replace PI_ucid which the NJIT UCID of PI
    #SBATCH -t 72:00:00
    
    #module load command

    module purge > /dev/null 2>&1
    module load wulver
    module load intel/2025a HDF5 VASP
    
    srun --mpi=pmix vasp_std > vasp.log
    ```
    
## Related Applications

* [Gaussian](gaussian.md)
* [ORCA](orca.md)

## User Contributed Information

!!! info "Please help us improve this page"

    Users are invited to contribute helpful information and corrections through our [Github repository](https://github.com/arcs-njit-edu/Docs/issues).


