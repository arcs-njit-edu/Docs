---
title: LAMMPS
---
[LAMMPS](https://lammps.sandia.gov/) is a large scale classical molecular dynamics code, and stands for Large-scale Atomic/Molecular Massively Parallel Simulator.  LAMMPS has potentials for soft materials (biomolecules,
polymers), solid-state materials (metals, semiconductors) and coarse-grained or
mesoscopic systems. It can be used to model atoms or, more generically, as a
parallel particle simulator at the atomic, meso, or continuum scale.

## Availability

=== "Wulver"

    ```python exec="on"
    import pandas as pd
    
    df = pd.read_csv('docs/assets/tables/module_wulver.csv')
    soft = df.query('Software == "LAMMPS"')
    print(soft.to_markdown(index=False))
    ```

=== "Lochness"

    ```python exec="on"
    import pandas as pd
    
    df = pd.read_csv('docs/assets/tables/module_lochness.csv')
    soft = df.query('Software == "LAMMPS"')
    print(soft.to_markdown(index=False))
    ```

!!! note

    To know the deatils about dependent toolchain please go to [Toolchains](compilers.md#toolchains)


## Application Information, Documentation and Support

The official LAMMPS is available at [LAMMPS Online Manual](https://lammps.sandia.gov/doc/Manual.html). LAMMPS has a large user base and a good user support. Question related to using LAMMPS can be posted to the [LAMMPS User forum](https://matsci.org/c/lammps/40). Archived [user mailing list](https://sourceforge.net/p/lammps/mailman/lammps-users/) are also useful to resolve some of the common user issues. 

!!! tip

    If *after* checking the above forum, if you believe that there is an issue
    with the module, please file a ticket with [Service Now](mailto:hpc@njit.edu)


## Using LAMMPS

??? example "Sample Batch Script to Run LAMMPS"
    
    === "Wulver"
    
        ```slurm
        #!/bin/bash
        #SBATCH -J test_lammps
        #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
        #SBATCH --error=%x.%j.err # prints the error message
        #SBATCH --partition=general 
		#SBATCH --nodes=1
        #SBATCH --ntasks-per-node=128
		#SBATCH --mem-per-cpu=4000M # Maximum allowable mempry per CPU 4G
		#SBATCH --qos=standard
        #SBATCH --account=PI_ucid # Replace PI_ucid which the NJIT UCID of PI
		#SBATCH --time=71:59:59  # D-HH:MM:SS
    
        ###############################################
        #
        # Purge and load modules needed for run
        #
        ################################################
        module purge
        module load wulver # Load slurm, easybuild
        module load foss/2021b LAMMPS
    
        srun -n $SLURM_NTASKS lmp -in test.in
        ```

    === "Lochness"

        ```slurm
        #!/bin/bash
        #SBATCH -J test_lammps
        #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
        #SBATCH --partition=public
        #SBATCH --nodes=2
        #SBATCH --ntasks-per-node=32
        #SBATCH --mem-per-cpu=10G # Adjust as necessary
        #SBATCH --time=00:01:00  # D-HH:MM:SS
        
        ###############################################
        #
        # Purge and load modules needed for run
        #
        ################################################
        module purge
        module load foss/2021b LAMMPS
    
        srun -n $SLURM_NTASKS lmp -in test.in
        ```

Then submit the job script using the sbatch command, e.g., assuming the job script name is `test_lammps.slurm`:

```console
sbatch test_lammps.slurm
```

## Building LAMMPS from source

Some users may be interested in building LAMMPS from source to enable more specific LAMMPS packages. 
The source files for LAMMPS can be [downloaded](https://www.lammps.org/download.html) as either a tar file 
or from the [LAMMPS Github repository](https://github.com/lammps/lammps). 

??? example "Building on Cluster"
	The following procedure was used to build LAMMPS on Wulver. 
    In the terminal:
    
    === "Wulver"

        ```bash
        module purge
        module load wulver
        module load foss
        module load CMake
    
        git clone https://github.com/lammps/lammps.git
        cd lammps
        mkdir build
        cd build
    
        cmake -DCMAKE_INSTALL_PREFIX=$PWD/../install_hsw -DCMAKE_CXX_COMPILER=mpicxx \
                    -DCMAKE_BUILD_TYPE=Release -D BUILD_MPI=yes -DKokkos_ENABLE_OPENMP=ON \
                    -DKokkos_ARCH_HSW=ON -DCMAKE_CXX_STANDARD=17 -D PKG_MANYBODY=ON \
                    -D PKG_MOLECULE=ON -D PKG_KSPACE=ON -D PKG_REPLICA=ON -D PKG_ASPHERE=ON \
                    -D PKG_RIGID=ON -D PKG_KOKKOS=ON -D DOWNLOAD_KOKKOS=ON \
                    -D CMAKE_POSITION_INDEPENDENT_CODE=ON -D CMAKE_EXE_FLAGS="-dynamic" ../cmake
        make -j16
        make install
        ```

    === "Lochness"

        ```bash
        module purge
        module load foss
        module load CMake
    
        git clone https://github.com/lammps/lammps.git
        cd lammps
        mkdir build
        cd build
    
        cmake -DCMAKE_INSTALL_PREFIX=$PWD/../install_hsw -DCMAKE_CXX_COMPILER=mpicxx \
                    -DCMAKE_BUILD_TYPE=Release -D BUILD_MPI=yes -DKokkos_ENABLE_OPENMP=ON \
                    -DKokkos_ARCH_HSW=ON -DCMAKE_CXX_STANDARD=17 -D PKG_MANYBODY=ON \
                    -D PKG_MOLECULE=ON -D PKG_KSPACE=ON -D PKG_REPLICA=ON -D PKG_ASPHERE=ON \
                    -D PKG_RIGID=ON -D PKG_KOKKOS=ON -D DOWNLOAD_KOKKOS=ON \
                    -D CMAKE_POSITION_INDEPENDENT_CODE=ON -D CMAKE_EXE_FLAGS="-dynamic" ../cmake
        make -j16
        make install
        ```

## Related Applications

* [GROMACS](gromacs.md)

## User Contributed Information

!!! info "Please help us improve this page"

    Users are invited to contribute helpful information and corrections through our [Github repository](https://github.com/arcs-njit-edu/Docs/blob/main/CONTRIBUTING.md).



