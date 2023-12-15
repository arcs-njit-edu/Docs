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

=== "Lochness"

    ```python exec="on"
    import pandas as pd
    
    df = pd.read_csv('docs/assets/tables/module_lochness.csv')
    soft = df.query('Software == "GROMACS"')
    print(soft.to_markdown(index=False))
    ```

## Application Information, Documentation
The documentation of OpenFOAM is available at [GROMACS Documentation](https://manual.gromacs.org/current/index.html), where you can find the tutorials in topologies, input file format, setting parameters etc. 

## Using GROMACS
GROMACS can be used on CPU or GPU. When using GROMACS with GPUs (Graphics Processing Units), the calculations can be significantly accelerated, allowing for faster simulations. You can use GROMACS with GPU acceleration, but you need to use GPU nodes on our cluster. 

??? example "Sample Batch Script to Run GROMACS on GPU gmx_gpu.submit.sh"

    === "Wulver"
        
        ```slurm
        #!/bin/bash -l
        # NOTE the -l (login) flag!
        #SBATCH -J gmx2023
        #SBATCH -o test.out
        #SBATCH -e test.err
        #SBATCH --mail-type=ALL
        #SBATCH --partition=gpu
        #SBATCH --qos=standard
        #SBATCH --time 72:00:00   # Max 3 days
        #SBATCH --nodes=1
        #SBATCH --ntasks-per-node=4
        #SBATCH --cpus-per-task=2
        #SBATCH --gres=gpu:2  
        #SBATCH --account=PI_ucid  # Replace PI_ucid with the UCID of PI, if you don't know PI's UCID use "sacctmgr show user username" on the login screen, replace "username" with your UCID

        module purge
        module load wulver
        module load foss/2022b GROMACS/2023.1-CUDA-12.0.0

        INPUT_DIR=${PWD}/INPUT
        OUTPUT_DIR=${PWD}/OUTPUT

        cp -r $INPUT_DIR/* $OUTPUT_DIR/
        cd $OUTPUT_DIR

        gmx mdrun -v -deffnm em -ntmpi 8 -ntomp 2 -nb gpu
        ```
    === "Lochness"
        
        ```slurm
        #!/bin/bash -l
        #SBATCH --job-name=gpu-esculentin
        #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
        #SBATCH --partition=datasci
        #SBATCH --nodes=1
        #SBATCH --ntasks-per-node=16
        #SBATCH --gres=gpu:1 # Number of GPUs per node
        #SBATCH --time=24:59:00  # D-HH:MM:SS
        #SBATCH --mail-type=ALL
        
        ################################################
        #
        # Purge and load modules needed to run
        #
        ################################################
        module purge
        module load foss/2021b CUDA/11.4.1
        module load GROMACS/2021.5-CUDA-11.4.1

        ###############################################
        #
        # cd into case directory if required
        #
        ################################################
        INPUT_DIR=${PWD}/input_files_v2020
        OUTPUT_DIR=${PWD}/output
        
        cp -r $INPUT_DIR/* $OUTPUT_DIR/
        cd $OUTPUT_DIR

        ###############################################
        #
        # Run simulation
        #
        ##############################################
        gmx mdrun -v -deffnm em -nt 16 -nb gpu
        ```
??? example "Sample Batch Script to Run GROMACS on CPU gmx_cpu.submit.sh"

    === "Wulver"
        
        ```slurm
        #!/bin/bash -l
        # NOTE the -l (login) flag!
        #SBATCH -J gmx2021
        #SBATCH -o test.out
        #SBATCH -e test.err
        #SBATCH --mail-type=ALL
        #SBATCH --partition=general
        #SBATCH --qos=standard
        #SBATCH --time 72:00:00   # Max 3 days
        #SBATCH --nodes=1
        #SBATCH --ntasks-per-node=4
        #SBATCH --cpus-per-task=2
        #SBATCH --account=PI_ucid  # Replace PI_ucid with the UCID of PI, if you don't know PI's UCID use "sacctmgr show user username" on the login screen, replace "username" with your UCID

        module purge
        module load wulver
        module load foss/2021b GROMACS/2021.5

        INPUT_DIR=${PWD}/INPUT
        OUTPUT_DIR=${PWD}/OUTPUT

        cp -r $INPUT_DIR/* $OUTPUT_DIR/
        cd $OUTPUT_DIR

        gmx mdrun -v -deffnm em -ntmpi 8 -ntomp 2 -nb gpu
        ```
    === "Lochness"
        
        ```slurm
        #!/bin/bash -l
        #SBATCH --job-name=gpu-esculentin
        #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
        #SBATCH --partition=datasci
        #SBATCH --nodes=1
        #SBATCH --ntasks-per-node=16
        #SBATCH --gres=gpu:1 # Number of GPUs per node
        #SBATCH --time=24:59:00  # D-HH:MM:SS
        #SBATCH --mail-type=ALL
        
        ################################################
        #
        # Purge and load modules needed to run
        #
        ################################################
        module purge
        module load foss/2021b 
        module load GROMACS/2021.5

        ###############################################
        #
        # cd into case directory if required
        #
        ################################################
        INPUT_DIR=${PWD}/input_files_v2020
        OUTPUT_DIR=${PWD}/output
        
        cp -r $INPUT_DIR/* $OUTPUT_DIR/
        cd $OUTPUT_DIR

        ###############################################
        #
        # Run simulation
        #
        ##############################################
        gmx mdrun -v -deffnm em -nt 16 -nb gpu
        ```
The tutorial in the above-mentioned job script can be found in 

=== "Wulver" 

    `/apps/testjobs/gromacs`

=== "Lochness"
    
    `/opt/site/examples/gromacs`

## Related Applications

* [LAMMPS](lammps.md)

## User Contributed Information

!!! info "Please help us improve this page"

    Users are invited to contribute helpful information and corrections through our [Github repository](https://github.com/arcs-njit-edu/Docs/blob/main/CONTRIBUTING.md).


