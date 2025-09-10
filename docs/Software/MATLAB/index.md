# MATLAB

MATLAB (matrix laboratory) is a multi-paradigm numerical computing environment and proprietary programming language developed by MathWorks. MATLAB allows matrix manipulations, plotting of functions and data, implementation of algorithms, creation of user interfaces, and interfacing with programs written in other languages. Although MATLAB is intended primarily for numerical computing, an optional toolbox uses the MuPAD symbolic engine allowing access to symbolic computing abilities. An additional package, Simulink, adds graphical multi-domain simulation and model-based design for dynamic and embedded systems.

## Availability

=== "Wulver"

    ```python exec="on"
    import pandas as pd
    
    df = pd.read_csv('docs/assets/tables/module_wulver_rhel9.csv')
    soft = df.query('Software == "MATLAB" | Software == "matlab"')
    print(soft.to_markdown(index=False))
    ```

## Application Information, Documentation
The documentation of MATLAB is available at [MATLAB Tutorial](https://www.mathworks.com/support/learn-with-matlab-tutorials.html).

## Using MATLAB

### Serial Job
??? exmaple "Sample Batch Script to run MATLAB: matlab-serial.sh"

    === "Wulver"

        ```slurm
        #!/bin/bash
        #SBATCH -J test_matlab
        #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
		#SBATCH --error=%x.%j.err # prints the error message
        #SBATCH --partition=general
        #SBATCH --nodes=1
        #SBATCH --ntasks-per-node=1
        #SBATCH --mem-per-cpu=4000M # Maximum allowable mempry per CPU 4G
		#SBATCH --qos=standard
        #SBATCH --account=PI_ucid # Replace PI_ucid which the NJIT UCID of PI
		#SBATCH --time=71:59:59  # D-HH:MM:SS
        
        # Load matlab module
        module purge
        module load wulver # Load the slurm, easybuild 
        module load MATLAB
    
        matlab -nodisplay -nosplash -r test
    
        ```

??? example "Sample MATLAB script"

    ```matlab
    A = [ 1 2; 3 4]
    A.^2
    ```

### Parallel Job

### Single node parallelization
??? exmaple "Sample Batch Script to run MATLAB: matlab_parallel.sh"

    === "Wulver"

        ```slurm
        #!/bin/bash
        #SBATCH -J test_matlab
        #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
		#SBATCH --error=%x.%j.err # prints the error message
        #SBATCH --partition=general
        #SBATCH --nodes=1
        #SBATCH --ntasks-per-node=32
        #SBATCH --mem-per-cpu=4000M # Maximum allowable mempry per CPU 4G
		#SBATCH --qos=standard
        #SBATCH --account=PI_ucid # Replace PI_ucid which the NJIT UCID of PI
		#SBATCH --time=71:59:59  # D-HH:MM:SS
        
        # Load matlab module
        module purge
        module load wulver # Load the slurm, easybuild
        module load MATLAB
    
        # Run matlab
        matlab -nodisplay -nosplash -r 'cd('/path/to/for_loop.m');for_loop; quit'
        ```
        Replace `cd('/path/to/for_loop.m')` with the actual path of the matlab script. You don't need to use `cd('/path/to/for_loop.m')` if the Matlab script and job script are in the same directory. In that case, use `matlab -nodisplay -nosplash -r 'for_loop; quit' `


??? example "Sample Parallel MATLAB script: for_loop.m"

    ```matlab
    poolobj = parpool('local',32);
    fprintf('Number of workers: %g\n', poolobj.NumWorkers);

    tic
    n = 2000;
    A = 500;
    a = zeros(n);
    parfor i = 1:n
        a(i) = max(abs(eig(rand(A))));
    end
    toc
    ```

## Multi node parallelization
If you want to learn how to install a version of MATLAB on your local system and use it to run jobs on Wulver, please see [Using Local MATLAB on Wulver](matlab_local.md)


