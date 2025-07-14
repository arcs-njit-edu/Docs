---
title: SIESTA
---
SIESTA (Spanish Initiative for Electronic Simulations with Thousands of Atoms) is a free and open-source software package for performing electronic structure calculations of materials using density functional theory (DFT). It is particularly well-suited for simulating materials containing large numbers of atoms, such as nanomaterials and surfaces.

SIESTA uses a localized basis set approach that reduces the computational cost of DFT calculations by approximating the electronic wavefunction using a small number of basis functions centered around each atom. This allows SIESTA to efficiently simulate systems containing thousands of atoms with reasonable accuracy.

SIESTA is actively developed and maintained by a team of researchers at the Universidad Autónoma de Madrid in Spain, and is available as a free download under an open-source license. It is widely used in the fields of material science, chemistry, and physics for studying a wide range of materials, including metals, semiconductors, and biological molecules.

## Availability

=== "Wulver"

    ```python exec="on"
    import pandas as pd
    
    df = pd.read_csv('docs/assets/tables/module_wulver.csv')
    soft = df.query('Software == "Siesta"')
    print(soft.to_markdown(index=False))
    ```

## Related Applications

* 

## User Contributed Information

!!! info "Please help us improve this page"

    Users are invited to contribute helpful information and corrections through our [Github repository](https://github.com/arcs-njit-edu/Docs/issues).



