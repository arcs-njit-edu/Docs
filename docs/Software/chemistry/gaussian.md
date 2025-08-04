---
title: Gaussian
---


## Availability

=== "Wulver"

    ```python exec="on"
    import pandas as pd
    
    df = pd.read_csv('docs/assets/tables/module_wulver.csv')
    soft = df.query('Software == "Gaussian"')
    print(soft.to_markdown(index=False))
    ```

!!! important 

    Due to licensing restrictions, Gaussian is not automatically accessible to all HPC users. Students are required to contact [hpc@njit.edu](mailto:hpc@njit.edu) to request access to Gaussian.

## Application Information, Documentation
The documentation of Gaussian is available at [Gaussian Documentation](https://gaussian.com/man/). For any issues Gaussian simulation, users can contact at [Gaussian Support](https://gaussian.com/techsupport/). 

## Using Gaussian
??? example "Sample Batch Script to Run Gaussian : g16.submit.sh"
    
    === "Wulver"

        ```slurm
        #!/bin/bash -l
        #SBATCH -J g16
        #SBATCH --nodes=1
        #SBATCH --ntasks-per-node=4
        #SBATCH --mem-per-cpu=3G
        #SBATCH --time=10:00:00
        #SBATCH --partition=general
        #SBATCH --account=PI_UCID # Replace PI_UCID with the UCID of PI
        #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
        #SBATCH --error=%x.%j.err
        #SBATCH --qos=standard
        
        #module load command

        module purge > /dev/null 2>&1
        module load wulver
        module load Gaussian
        
        #Run the program

        g16 test_g98.com
        ```

The sample input file `test_g98.com` can be found in `/apps/testjobs/Gaussian`

!!! important
    
    Please don't run anything on `/apps/testjobs/Gaussian` as users have only read-only permission. You need to copy the submit script and input file from `/apps/testjobs/Gaussian` to `$HOME` or `/project`.

## Related Applications

* [CP2K](cp2k.md)
* [ORCA](orca.md)

## User Contributed Information

!!! info "Please help us improve this page"

    Users are invited to contribute helpful information and corrections through our [Github repository](https://github.com/arcs-njit-edu/Docs/issues).


