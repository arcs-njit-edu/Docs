---
title: CP2K
---
CP2K is a free and open-source quantum chemistry and solid-state physics software package that is designed to perform atomistic simulations of a wide range of materials. It is capable of carrying out a variety of quantum mechanical calculations, including density functional theory (DFT), time-dependent DFT, and many-body perturbation theory (MBPT).

CP2K is optimized for running on massively parallel supercomputers, making it well-suited for large-scale simulations of complex systems. It includes a number of advanced algorithms and techniques for efficiently calculating electronic properties of materials, such as linear scaling algorithms for DFT and MBPT calculations.

CP2K is highly modular and flexible, allowing users to customize and extend its functionality by writing their own input files or by modifying the source code. It also includes a graphical user interface (GUI) for setting up and running simulations, as well as a number of built-in tools for analyzing simulation output.

CP2K is widely used in the fields of materials science, chemistry, and physics for studying a wide range of materials, including biomolecules, polymers, and solids.

## Availability

```python exec="on"
import pandas as pd

df = pd.read_csv('docs/assets/tables/module_wulver.csv')
soft = df.query('Software == "CP2K"')
print(soft.to_markdown(index=False))
```


## Application Information, Documentation
The documentation of CP2K is available at [CP2K Documentation](https://www.cp2k.org/docs). For any issues CP2K simulation, users can contact at [CP2K Forum](https://www.cp2k.org/howto:forum). 

## Using CP2K
CP2K MPI/OpenMP-hybrid Execution (PSMP), CP2K with Population Analysis capabilities- CP2K-popt

??? example "Sample Batch Script to Run CP2K : cp2k.submit.sh"

    ```slurm
    #!/bin/bash -l
    #SBATCH -J CP2K
    #SBATCH -o sn1-xtb_input.out
    #SBATCH -e sn1-xtb_input.err
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
    module load foss/2022b CP2K
    
    #Run the program

    inputFile=sn1-xtb_input.inp
    outputFile=sn1-xtb_input.out
    mpirun -np $SLURM_NTASKS cp2k.popt -i $inputFile -o $outputFile
    ```

The sample input file `sn1-xtb_input.inp` can be found in `/apps/testjobs/CP2K`

!!! important
    
    Please don't run anything on `/apps/testjobs/CP2K` as users have only read-only permission. You need to copy the submit script and input file from `/apps/testjobs/CP2K` to `$HOME` or `/project`.
    
## Related Applications

* [Gaussian](gaussian.md)
* [ORCA](orca.md)

## User Contributed Information

!!! info "Please help us improve this page"

    Users are invited to contribute helpful information and corrections through our [Github repository](https://github.com/arcs-njit-edu/Docs/blob/main/CONTRIBUTING.md).


