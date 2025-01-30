# Software Environment
All software and numerical libraries available at the cluster can be found at `/apps/easybuild/software/`. We use [EasyBuild](https://docs.easybuild.io/en/latest) to install, build and manage different version of packages. 

If you could not find software or libraries on HPC cluster, please submit a request for [HPC Software Installation](https://njit.service-now.com/sp?id=sc_cat_item&sys_id=0746c1f31b6691d04c82cddf034bcbe2&sysparm_category=405f99b41b5b1d507241400abc4bcb6b) by visiting the [Service Catalog](https://njit.service-now.com/sp?id=sc_category). The list of installed software or packages on HPC cluster can be found in [Software List](#software-list).

## Modules
We use Environment Modules to manage the user environment in HPC, which help users to easily load and unload software packages, switch between different versions of software, and manage complex software dependencies. [Lmod](https://lmod.readthedocs.io/en/latest) is an extension of the Environment Modules system, implemented in Lua. It enhances the functionality of traditional Environment Modules by introducing features such as hierarchical module naming, module caching, and improved flexibility in managing environment variables.

### Search for Specific Package
You can check specific packages and list of their versions using `module spider`. For example, the list of Python installed on cluster can be checked by using

```console
module spider Python

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Description:
      Python is a programming language that lets you work more quickly and integrate your systems more effectively.

     Versions:
        Python/2.7.18-bare
        Python/3.9.6-bare
        Python/3.9.6
        Python/3.10.4-bare
        Python/3.10.4
        Python/3.10.8-bare
        Python/3.10.8
        Python/3.11.5
     Other possible modules matches:
        Biopython  Boost.Python  Python-bundle-PyPI  meson-python  python3  python39

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  To find other possible module matches execute:

      $ module -r spider '.*Python.*'

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  For detailed information about a specific "Python" package (including how to load the modules) use the module's full name.
  Note that names that have a trailing (E) are extensions provided by other modules.
  For example:

     $ module spider Python/3.11.5
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


```
This will show the different versions of Python available on Wulver. 

To see how to load the specific version of software (for example `Python/3.9.6`), the following command needs to be used.

```console
module spider Python/3.9.6
```
This will show the which prerequisite modules need to be loaded prior to loading `Python/3.9.6`

```console
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Python: Python/3.9.6
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Description:
      Python is a programming language that lets you work more quickly and integrate your systems more effectively.


    You will need to load all module(s) on any one of the lines below before the "Python/3.9.6" module is available to load.

      easybuild  GCCcore/11.2.0
      slurm/wulver  GCCcore/11.2.0

    Help:
      Description
      ===========
      Python is a programming language that lets you work more quickly and integrate your systems
       more effectively.


      More information
      ================
       - Homepage: https://python.org/
```
If you are unsure about the version, you can also use `module spider Python` to see the different versions of Python and prerequisite modules to be loaded. 

### Load Modules 
To use specific package, you need to use `module load` command which modified the environment to load the software package(s).

!!! Note

    * The `module load` command will load dependencies automatically as needed, however you may still need to load prerequisite modules to load specific software package(s). For that you need to use `module spider` command as described above.
    * For running jobs via batch script, you need to add module load command(s) to your submission script.

For example, to load `Python` version `3.9.6` as shown in the above example, you need to load `GCCcore/11.2.0` module first before loading the Python module is available to load. To use `Python 3.9.6`, use the following command
```console
module load GCCcore/11.2.0 Python
```
You can verify whether Python is loaded using

```console
module li
```
and this will result is the following output
```console
Currently Loaded Modules:
  1) easybuild   2) wulver   3) slurm/wulver   4) null   5) GCCcore/11.2.0   6) zlib/1.2.11   7) binutils/2.37   8) bzip2/1.0.8   9) ncurses/6.2  10) libreadline/8.1  11) Tcl/8.6.11  12) SQLite/3.36  13) XZ/5.2.5  14) GMP/6.2.1  15) libffi/3.4.2  16) OpenSSL/1.1  17) Python/3.9.6

```
### Module unload

To unload a specific module that you've previously loaded:
```console
module unload Python
```
You can unload all modules at once with
```console
module purge
```
### Module Save Collections
Since some package(s) require to load prerequisite modules to load, every time it might be inconvenient to users to load those modules everytime. Therefore, you can save those modules in particular environment after loading those modules. For example
```console
module save environment_name
```
This will save the collection of  modules in `environment_name`. 

### Module List Collections
To get a list of your collections, run:
```console
module savelist
```
### Module Command Summary
Here are the list of `module` commands

| Command                           | Description                                                                            | 
|-----------------------------------|----------------------------------------------------------------------------------------|
| `module list`                     | 	Show active modules loaded in the user environment                                    |
| `module av [module]`	             | Show list of available modules in MODULEPATH                                           |
| `module spider [module]`          | 	Query all modules in MODULEPATH and any module hierarchy                              |
| `module overview [module]`        | 	List all modules with count of each module                                            |
| `module load [module]`            | 	Load a module file in the users environment                                           |
| `module unload [module]`          | 	Remove a loaded module from the user environment                                      |
| `module purge`                    | 	Remove all modules from the user environment                                          |
| `module swap [module1] [module2]` | 	Replace module1 with module2                                                          |
| `module show [module]`            | 	Show content of commands performed by loading module file                             |
| `module --raw show [module]`      | 	Show raw content of module file                                                       |
| `module help [module]`            | 	Show help for a given module                                                          |
| `module whatis [module]`          | 	A brief description of the module, generally single line                              |
| `module savelist`                 | 	List all user collections                                                             |
| `module save [collection]`        | 	Save active modules in a user collection                                              |
| `module describe [collection]`    | 	Show content of user collection                                                       |
| `module restore [collection]`     | 	Load modules from a collection                                                        |
| `module disable [collection]`     | 	Disable a user collection                                                             |
| `module --config`                 | 	Show Lmod configuration                                                               |
| `module use [-a] [path]`          | 	Prepend or Append path to MODULEPATH                                                  |
| `module unuse [path]`             | 	Remove path from MODULEPATH                                                           |
| `module --show_hidden av`         | 	Show all available modules in MODULEPATH including hidden modules                     |
| `module --show_hidden spider`     | 	Show all possible modules in MODULEPATH and module hierarchy including hidden modules |

### Further Reading
You can check the documentation of `module` on the cluster using the following command:
```
man module
```


## Software List

The following applications are installed on Wulver and Lochness.

=== "Wulver"

    ```python exec="on"
    import pandas as pd
    df = pd.read_csv('docs/assets/tables/module_wulver.csv')
    df = df.sort_values(by=df.columns[0])  # Sorts by the first column alphabetically
    print(df.to_markdown(index=False))
    ```

