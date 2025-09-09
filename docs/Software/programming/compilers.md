---
title: Compilers and Toolchains
---

## GNU and Intel Compilers 
We offer both GNU and Intel compilers. Here is the list of compilers you can find on our cluster.

=== "Wulver"

    ```python exec="on"
    import pandas as pd
    
    df = pd.read_csv('docs/assets/tables/module_wulver_rhel9.csv')
    # Header values to be added
    #column_names=["Compilers","modules"]
    soft = df.query('Software == "GCC" | Software == "intel-compilers"')
    soft = soft[~soft.apply(lambda row: row.astype(str).str.contains('system').any(), axis=1)]
    
    print(soft.to_markdown(index=False))
    ```

## MPI Libraries
MPI (Message Passing Interface) libraries are a set of software tools that allow for parallel computing on distributed memory systems, such as computer clusters. These libraries provide a standardized interface for communication between processes running on different nodes of the cluster. There are several implementations of MPI libraries available, such as OpenMPI, MPICH, and Intel MPI. Currently, the following MPI libraries on our cluster.

=== "Wulver"

    ```python exec="on"
    import pandas as pd
    df = pd.read_csv('docs/assets/tables/module_wulver_rhel9.csv')
    
    soft = df.query('Software == "OpenMPI" | Software == "impi"')
    #soft.columns = column_names
    print(soft.to_markdown(index=False))
    ```


## Toolchains
We use [EasyBuild](https://easybuild.io) to install the packages as modules and to avoid too many packages tol load as a module, we use pre-defined build environment modules called toolchains which include a combination of tools such as compilers, libraries etc. We use `foss` and `intel` toolchains in Wulver. The advantage of using toolchains is that user can load either `foss` or `intel` as base package and the additional libraries such as MPI, LAPACK and other math libraries will be automatically loaded. 
### Free Open Source Software (foss)
The `foss` toolchains are versioned with a yearletter scheme, e.g. `foss/2021b` is the second foss toolchain composed in 2021. The `foss` toolchain comprises the following 

```tree
foss
    gompi 
        GCC
            GCCcore
            zlib
            binutils
        OpenMPI
        numactl
        XZ
        libxml2
        libpciaccess
        hwloc
        OpenSSL
        libevent
        UCX
        libfabric
        PMIx
        UCC
    FFTW
    OpenBLAS
    ScaLAPACK
    FlexiBLAS
```
=== "Wulver"

    ```python exec="on"
    import pandas as pd
    
    df = pd.read_csv('docs/assets/tables/module_wulver_rhel9.csv')
    # Header values to be added
    #column_names=["Toolchains","modules"]
    soft = df.query('Software == "foss"')
    #soft.columns = column_names
    print(soft.to_markdown(index=False))
    ```

To see GCC and OpenMPI versions details in each toolchain, see the list of [compiler versions](compilers.md#gnu-and-intel-compilers) and [OpenMPI versions](compilers.md#mpi-libraries).
### Intel
Like `foss`, `intel` toolchains are versioned with yearletter scheme, e.g. `intel/2021b` is the second intel toolchain composed in 2021.

```tree
intel
    intel-compilers
        GCCcore   
        zlib
        binutils
    iimpi
        iccifort
        Intel MPI
        numactl
        UCX
    Intel Math Kernel Library
```

=== "Wulver"

    ```python exec="on"
    import pandas as pd
    
    df = pd.read_csv('docs/assets/tables/module_wulver_rhel9.csv')
    # Header values to be added
    #column_names=["Toolchains","modules"]
    soft = df.query('Software == "intel"')
    #soft.columns = column_names
    print(soft.to_markdown(index=False))
    ```

The `intel-compilers` and `impi` versions in `intel` toolchains are tabulated in [intel versions](compilers.md#gnu-and-intel-compilers) and [impi versions](compilers.md#mpi-libraries).
To see the versions of `GCCcore` and `mkl` libraries of `intel` toolchain, please load the intel toolchain module with yearletter version, e.g. `module load intel/2021b` and then use `module li`.