---
title: OVITO
---
OVITO is a scientific visualization and analysis software tool designed for the analysis of atomistic simulation data. It is used primarily in the field of materials science and computational chemistry, and is particularly well-suited for the analysis of molecular dynamics simulations and other atomistic simulation techniques.

OVITO provides a graphical user interface (GUI) that allows users to interactively visualize and analyze large datasets of atomistic simulation data. It supports a wide range of file formats commonly used in molecular dynamics simulations, including LAMMPS, GROMACS, and DL_POLY.

In addition to its visualization capabilities, OVITO also provides a set of built-in analysis tools that allow users to compute various properties of the simulated systems. These include calculation of radial distribution functions, Voronoi tessellation, and common structural analysis metrics like bond order parameters and coordination numbers.

## Availability

=== "Wulver"

    ```python exec="on"
    import pandas as pd
    
    df = pd.read_csv('docs/assets/tables/module_wulver.csv')
    soft = df.query('Software == "OVITO"')
    print(soft.to_markdown(index=False))
    ```

## Related Applications

* 

## User Contributed Information

!!! info "Please help us improve this page"

    Users are invited to contribute helpful information and corrections through our [Github repository](https://github.com/arcs-njit-edu/Docs/issues).


