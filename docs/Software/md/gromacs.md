---
title: GROMACS
---

[GROMACS](https://www.gromacs.org) is a versatile package to perform molecular dynamics, i.e. simulate the Newtonian equations of motion for systems with hundreds to millions of particles.

It is primarily designed for biochemical molecules like proteins, lipids, and nucleic acids that have a lot of complicated bonded interactions, but since GROMACS is extremely fast at calculating the nonbonded interactions (that usually dominate simulations) many groups are also using it for research on non-biological systems, e.g. polymers.

## Availability

=== "Wulver"

    ```python exec="on"
    import pandas as pd
    
    df = pd.read_csv('docs/assets/tables/module_wulver.csv')
    soft = df.query('Software == "GROMACS"')
    print(soft.to_markdown(index=False))
    ```

## Application Information, Documentation
The documentation of GROMACS is available at [GROMACS Manual](https://manual.gromacs.org/current/index.html), where you can find the tutorials in topologies, input file format, setting parameters, etc. 

## Using GROMACS
GROMACS can be used on CPU or GPU. When using GROMACS with GPUs (Graphics Processing Units), the calculations can be significantly accelerated, allowing for faster simulations. You can use GROMACS with GPU acceleration, but you need to use GPU nodes on our cluster. 

??? example "Sample Batch Script to Run GROMACS"

    === "GPU"
        
        ```slurm
        #!/bin/bash -l
        # NOTE the -l (login) flag!
        #SBATCH -J gmx2023
        #SBATCH -o test.%x.%j.out
        #SBATCH -e test.%x.%j.err
        #SBATCH --mail-type=ALL
        #SBATCH --partition=gpu
        #SBATCH --qos=standard
        #SBATCH --time 72:00:00   # Max 3 days
        #SBATCH --nodes=2
        #SBATCH --ntasks-per-node=2
        #SBATCH --gpus-per-node=2  
        #SBATCH --account=$PI_ucid  # Replace PI_ucid with the UCID of PI

        module purge
        module load wulver
        module load foss/2022b GROMACS/2023.1-CUDA-12.0.0

        INPUT_DIR=${PWD}/INPUT
        OUTPUT_DIR=${PWD}/OUTPUT

        cp -r $INPUT_DIR/* $OUTPUT_DIR/
        cd $OUTPUT_DIR

        srun gmx_mpi mdrun -deffnm run -cpi -v -ntomp 1 -pin on -tunepme -dlb yes -nb gpu -noappend
        ```

    === "CPU"
        
        ```slurm
        #!/bin/bash -l
        # NOTE the -l (login) flag!
        #SBATCH -J gmx2021
        #SBATCH -o test.%x.%j.out
        #SBATCH -e test.%x.%j.err
        #SBATCH --mail-type=ALL
        #SBATCH --partition=general
        #SBATCH --qos=standard
        #SBATCH --time 72:00:00   # Max 3 days
        #SBATCH --nodes=1
        #SBATCH --ntasks-per-node=8
        #SBATCH --account=$PI_ucid  # Replace PI_ucid with the UCID of PI

        module purge
        module load wulver
        module load foss/2023b GROMACS/2024.1

        INPUT_DIR=${PWD}/INPUT
        OUTPUT_DIR=${PWD}/OUTPUT

        cp -r $INPUT_DIR/* $OUTPUT_DIR/
        cd $OUTPUT_DIR

        srun gmx_mpi mdrun -v -deffnm em -cpi -v -ntomp 1 -pin on -tunepme -dlb yes -noappend
        ```

    === "CPU with threads"
        
        ```slurm
        #!/bin/bash -l
        # NOTE the -l (login) flag!
        #SBATCH -J gmx2021
        #SBATCH -o test.%x.%j.out
        #SBATCH -e test.%x.%j.err
        #SBATCH --mail-type=ALL
        #SBATCH --partition=general
        #SBATCH --qos=standard
        #SBATCH --time 72:00:00   # Max 3 days
        #SBATCH --nodes=1
        #SBATCH --ntasks-per-node=8
        #SBATCH --account=$PI_ucid  # Replace PI_ucid with the UCID of PI

        module purge
        module load wulver
        module load foss/2023b GROMACS/2024.1

        INPUT_DIR=${PWD}/INPUT
        OUTPUT_DIR=${PWD}/OUTPUT

        cp -r $INPUT_DIR/* $OUTPUT_DIR/
        cd $OUTPUT_DIR

        srun gmx_mpi mdrun -v -deffnm em -cpi -v -ntomp $SLURM_CPUS_PER_TASK -pin on -tunepme -dlb yes -noappend
        ```
        
    
The tutorial in the above-mentioned job script can be found in `/apps/testjobs/gromacs`


## Related Applications

* [LAMMPS](lammps.md)

## User Contributed Information

!!! info "Please help us improve this page"

    Users are invited to contribute helpful information and corrections through our [Github repository](https://github.com/arcs-njit-edu/Docs/blob/main/CONTRIBUTING.md).


