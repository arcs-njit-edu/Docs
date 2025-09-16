---
title: OpenFOAM
---
OpenFOAM (Open Field Operation and Manipulation) is a free and open-source computational fluid dynamics (CFD) software package that is used to simulate and analyze fluid flow, heat transfer, and other related phenomena. It is written primarily in C++ and can be used on various operating systems such as Linux, Windows, and macOS.

OpenFOAM offers a wide range of solvers, turbulence models, and physical models that can be used to model various engineering applications such as automotive, aerospace, chemical processing, and power generation. It also allows users to customize and extend its functionality to meet specific needs.

The software is widely used in academia, research, and industry, and is known for its robustness, flexibility, and scalability. It offers a high degree of parallelization, which allows it to be used on large clusters of computers for complex simulations. Because it is open source, it is often used by researchers and developers to create new solvers, models, and add-ons for specific applications.

## Availability

=== "Wulver"

    ```python exec="on"
    import pandas as pd
    
    df = pd.read_csv('docs/assets/tables/module_wulver_rhel9.csv')
    soft = df.query('Software == "OpenFOAM"')
    print(soft.to_markdown(index=False))
    ```

## Application Information, Documentation
The documentation of OpenFOAM is available at [OpenFOAM Documentation](https://www.openfoam.com/documentation/overview), where you can find the tutorials in OpenFOAM meshing (blockMesh), postprocessing, setting boundary conditions etc. 

## Using OpenFOAM
OpenFOAM can be used for both serial and parallel jobs. To run OpenFOAM in parallel, you need to use the following job script.

??? example "Sample Batch Script to Run OpenFOAM in parallel: openfoam_parallel.submit.sh"

    === "Wulver"
        
        ```slurm
        #!/bin/bash -l
        #SBATCH --job-name=openfoam_parallel
        #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
        #SBATCH --error=%x.%j.err # prints the error message
        #SBATCH --partition=general 
		#SBATCH --nodes=1
        #SBATCH --ntasks-per-node=32
		#SBATCH --mem-per-cpu=4000M # Maximum allowable mempry per CPU 4G
		#SBATCH --qos=standard
        #SBATCH --account=PI_ucid # Replace PI_ucid which the NJIT UCID of PI
		#SBATCH --time=71:59:59  # D-HH:MM:SS
        ################################################
        #
        # Purge and load modules needed for run
        #
        ################################################
        module purge
        module load wulver # Load slurm, easybuild
        module load foss/2024a OpenFOAM
        ################################################
        #
        # Source OpenFOAM bashrc
        # The modulefile doesn't do this
        #
        ################################################
        source $FOAM_BASH
        ################################################
        #
        # copy into cavity directory from /opt/site/examples/openFoam/parallel 
        # run blockMesh and
        # icoFoam. Note: this is running on one node and
        # using all 32 cores on the node
        #
        ################################################
        cp -r /apps/easybuild/examples/openFoam/parallel/cavity /path/to/destination
        # /path/to/destination is destination path where user wants to copy the cavity directory
        cd cavity
        blockMesh
        decomposePar -force
        srun icoFoam -parallel
        reconstructPar
        ```

!!! note
        
    === "Wulver"
        
        You can copy the tutorial `cavity` mentioned in the above job script from the `/apps/easybuild/examples/openFoam/parallel` directory.  


To run OpenFOAM in serial, the following job script can be used.

??? example "Sample Batch Script to Run OpenFOAM in serial: openfoam_serial.submit.sh"

    === "Wulver"
        
        ```slurm
        #!/bin/bash -l
        #SBATCH --job-name=openfoam_serial
        #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
        #SBATCH --error=%x.%j.err # prints the error message
        #SBATCH --partition=general 
		#SBATCH --nodes=1
        #SBATCH --ntasks-per-node=32
		#SBATCH --mem-per-cpu=4000M # Maximum allowable mempry per CPU 4G
		#SBATCH --qos=standard
        #SBATCH --account=PI_ucid # Replace PI_ucid which the NJIT UCID of PI
		#SBATCH --time=71:59:59  # D-HH:MM:SS
        ################################################
        #
        # Purge and load modules needed for run
        #
        ################################################
        module purge
        module load wulver # Load slurm, easybuild
        module load foss/2021b OpenFOAM
        ################################################
        #
        # Source OpenFOAM bashrc
        # The modulefile doesn't do this
        #
        ################################################
        source $FOAM_BASH
        ################################################
        #
        # copy into cavity directory from /apps/easybuild/examples/openFoam/serial 
        # run blockMesh and
        # icoFoam. Note: this is running on one node and
        # using all 32 cores on the node
        #
        ################################################
        cp -r /apps/easybuild/examples/openFoam/serial/cavity /path/to/destination
        # /path/to/destination is destination path where user wants to copy the cavity directory
        cd cavity
        blockMesh
        icoFoam
        ```

Submit the job script using the sbatch command: `sbatch openfoam_parallel.submit.sh` or `sbatch openfoam_serial.submit.sh`.

## Building OpenFOAM from source
Sometimes, users need to create a new solver or modify the existing solver by adding different functions for their research. In that case, users need to build openFOAM from source since user do not have the permission to add libraries in the root directory where OpenFOAM is installed. The following instructions are provided on how to build openFOAM from source on cluster. If you have any queries or issues regarding building OpenFOAM, please contact us at [hpc@njit.edu](mailto:hpc@njit.edu).

```bash

  # This is to build a completely self contained OpenFOAM using MPICH mpi. Everything from GCC on up will be built.
  
  # start an interactive session with compute node. Replace "PI_UCID" with the UCID of PI. Modify the other parameters if required.
  srun --partition=general --nodes=1 --ntasks-per-node=16 --mem-per-cpu=2G --account=PI_UCID --qos=standard --time=2:00:00 --pty bash  
     
  # purge all loaded modules
  module purge
  # Download the latest version of OpenFOAM, visit https://develop.openfoam.com/Development/openfoam/-/blob/master/doc/Build.md for details
  # Download the source
  wget https://dl.openfoam.com/source/v2212/OpenFOAM-v2212.tgz 
  # Download ThirdParty
  wget https://dl.openfoam.com/source/v2212/ThirdParty-v2212.tgz
        
  cd ThirdParty-v2212
        
  #Packages to download :
  wget https://ftp.gnu.org/gnu/gcc/gcc-4.8.5/gcc-4.8.5.tar.bz2
  wget https://src.fedoraproject.org/repo/pkgs/metis/metis-5.1.0.tar.gz/5465e67079419a69e0116de24fce58fe/metis-5.1.0.tar.gz
  wget ftp://ftp.gnu.org/gnu/gmp/gmp-6.2.0.tar.bz2
  wget ftp://ftp.gnu.org/gnu/mpfr/mpfr-4.0.2.tar.bz2
  wget ftp://ftp.gnu.org/gnu/mpc/mpc-1.1.0.tar.gz
  wget http://www.mpich.org/static/downloads/3.3/mpich-3.3.tar.gz
        
  # unpack the above packages
        
  vi ../OpenFOAM-v2212/etc/bashrc
  # Change the following in bashrc 
  # User needs to specify the full path of the project directory below, it can be either the research directory or $HOME directory.
    projectDir="path/to/OpenFOAM/2212/OpenFOAM-$WM_PROJECT_VERSION" 
    export WM_MPLIB=MPICH
    export WM_LABEL_SIZE=64
  
  vi ../OpenFOAM-v2212/etc/config.sh/compiler
  # Change the following in compiler
    default_gmp_version=gmp-system
    default_mpfr_version=mpfr-system
    default_mpc_version=mpc-system

    gmp_version="gmp-6.2.0"
    mpfr_version="mpfr-4.0.2"
    mpc_version="mpc-1.1.0"
  # Source the RC script
  source ../OpenFOAM-v2212/etc/bashrc FOAMY_HEX_MESH=yes
  # You might see the following warning message
  ===============================================================================
  Warning in /opt/site/apps/OpenFOAM/2212/OpenFOAM-v2212/etc/config.sh/settings:
  Cannot find 'Gcc' compiler installation
    /opt/site/apps/OpenFOAM/2212/ThirdParty-v2212/platforms/linux64/gcc-4.8.5

  Either install this compiler version, or use the system compiler by setting
  WM_COMPILER_TYPE to 'system' in $WM_PROJECT_DIR/etc/bashrc.
  ===============================================================================
  No completions for /opt/site/apps/OpenFOAM/2212/OpenFOAM-v2212/platforms/linux64GccDPInt64Opt/bin
  [ignore if OpenFOAM is not yet compiled]

  ./makeGcc
  wmRefresh
  # make MPICH
  ./makeMPICH
  wmRefresh

  # We should be able to make the rest of the utilities.
  # load the cmake module
  module load cmake
  
  /Allwmake -j 8

  cd ../OpenFOAM-v2212
  wmRefresh
  
  ./Allwmake -j 16
```

## Related Applications

* [FLUENT](fluent.md)

## User Contributed Information

!!! info "Please help us improve this page"
    
    Users are invited to contribute helpful information and corrections through our [Github repository](https://github.com/arcs-njit-edu/Docs/issues).



