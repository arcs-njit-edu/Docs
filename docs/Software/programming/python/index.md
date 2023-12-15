# Python
[Python](https://www.python.org/) is a high-level, general-purpose programming language. Python supports multiple programming paradigms, including structured, object-oriented, and functional programming. It is used in a wide range of applications such as machine learning, molecular dynamics, scientific computing, automation, image processing, etc.

## Availability

=== "Wulver"

    ```python exec="on"
    import pandas as pd
    
    df = pd.read_csv('docs/assets/tables/module_wulver.csv')
    soft = df.query('Software == "Python"')
    soft = soft[~soft.apply(lambda row: row.astype(str).str.contains('bare').any(), axis=1)]
    print(soft.to_markdown(index=False))
    ```

=== "Lochness"

    ```python exec="on"
    import pandas as pd
    
    df = pd.read_csv('docs/assets/tables/module_lochness.csv')
    soft = df.query('Software == "Python"')
    soft = soft[~soft.apply(lambda row: row.astype(str).str.contains('bare').any(), axis=1)]
    print(soft.to_markdown(index=False))
    ```

## Python libraries
Apart from Python’s standard library, Python offers a wide range of additional libraries that need to be loaded as modules before users can use these. Here, we list these additional libraries. Please contact us to file a ticket with [Service Now](mailto:hpc@njit.edu) in case you do not find the libraries you want to use.

| Libraries  | Version | Python Version | Module load command                   |
|------------|---------|----------------|---------------------------------------|
| NumPy      | 1.21.3  | 3.9.6          | `module load foss/2021b SciPy-bundle` |
| Matplotlib | 3.4.3   | 3.9.6          | `module load foss/2021b matplotlib`   |
| SciPy      | 2021.10 | 3.9.6          | `module load foss/2021b SciPy-bundle` |

For using multiple libraries, you simply need to add the library name in `module load` command. For example, to load NumPy, Matplotlib, and SciPy together, you need to use the following command. 

```
module load foss/2021b SciPy-bundle matplotlib
```

## Using Conda or `pip` to Install Python Libraries

Since sometimes users a specific version of Python libraries, it is advisable to use Conda so that users can create their own environment where they can install required packages based on their requirements. Conda is a cross-language package manager that excels at managing environments and dependencies, making it suitable for scientific computing and data science projects. It can handle non-Python libraries and binaries, offering a comprehensive solution. On the other hand, pip is the default Python package installer, known for its simplicity and compatibility with the Python Package Index (PyPI). While both tools serve the same purpose, it is generally recommended to choose one and remain consistent within a project to avoid potential conflicts. Please see [Conda Documentation](conda.md) on how to install Python packages via Conda.