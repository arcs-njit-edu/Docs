---
title: ORCA
---

## Availability

=== "Wulver"

    ```python exec="on"
    import pandas as pd
    
    df = pd.read_csv('docs/assets/tables/module_wulver_rhel9.csv')
    soft = df.query('Software == "ORCA"')
    print(soft.to_markdown(index=False))
    ```

## Application Information, Documentation
The documentation of Gaussian is available at [ORCA Documentation](https://www.orcasoftware.de/tutorials_orca/). For any issues Gaussian simulation, users can contact at [ORCA Forum](https://orcaforum.kofo.mpg.de/app.php/portal). 

## Using Gaussian
??? example "Sample Batch Script to Run ORCA : orca.submit.sh"
    
    === "Wulver"

        ```slurm
        #!/bin/bash -l
        #SBATCH --job-name=job_orca
        #SBATCH --output=%x.%j.out
        #SBATCH --error=%x.%j.err
        #SBATCH --partition=general
        #SBATCH --qos=standard
        #SBATCH --nodes=1
        #SBATCH --account=PI_UCID # Replace PI_UCID with the UCID of PI
        #SBATCH --ntasks-per-node=8
        #SBATCH --time=59:00  # D-HH:
        
        #module load command

        module purge > /dev/null 2>&1
        module load wulver
        module load foss/2024a ORCA
        
        #Run the program

        srun orca test.inp > geom.out
        ```

The sample input file `test.inp` can be found in `/apps/testjobs/ORCA`

!!! important
    
    Please don't run anything on `/apps/testjobs/ORCA` as users have only read-only permission. You need to copy the submit script and input file from `/apps/testjobs/ORCA` to `$HOME` or `/project`.

## Related Applications

* [Gaussian](gaussian.md)
* [CP2K](cp2k.md)

## User Contributed Information

!!! info "Please help us improve this page"

    Users are invited to contribute helpful information and corrections through our [Github repository](https://github.com/arcs-njit-edu/Docs/issues).



