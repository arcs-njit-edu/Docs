## Overview
Interactive jobs allow users to directly access a compute node in real time — as if you were working on your personal computer, but with the power of HPC behind it.

Unlike batch jobs, which are queued and run in the background, interactive jobs open a live terminal session on a compute node. This is useful for:

- Testing code or software modules
- Debugging runtime issues
- Running Jupyter notebooks
- Exploring the system environment or dependencies

You still need to request resources via Slurm, but instead of submitting a script with sbatch, you request an interactive shell using our `interative` command.

#### The `interactive` Command
We provide a built-in shortcut command, `interactive`, that allows you to quickly and easily request a session in compute node.

The `interactive` command acts as a convenient wrapper for Slurm’s [salloc](https://slurm.schedmd.com/salloc.html) command. Similar to [sbatch](https://slurm.schedmd.com/sbatch.html), which is used for batch jobs, `salloc` is specifically designed for interactive jobs. 

```bash
$ interactive -h
Usage: interactive -a ACCOUNT -q QOS -j JOB_TYPE
Starts an interactive SLURM job with the required account and QoS settings.

Required options:
  -a ACCOUNT       Specify the account to use.
  -q QOS           Specify the quality of service (QoS).
  -j JOB_TYPE      Specify the type of job: 'cpu' for CPU jobs or 'gpu' for GPU jobs.

Example: Run an interactive GPU job with the 'test' account and 'test' QoS:
  /apps/site/bin/interactive -a test -q test -j gpu

This will launch an interactive job on the 'gpu' partition with the 'test' account and QoS 'test',
using 1 GPU, 1 CPU, and a walltime of 1 hour by default.

Optional parameters to modify resources:
  -n NTASKS        Specify the number of CPU tasks (Default: 1).
  -t WALLTIME      Specify the walltime in hours (Default: 1).
  -g GPU           Specify the number of GPUs (Only for GPU jobs, Default: 1).
  -p PARTITION     Specify the SLURM partition (Default: 'general' for CPU jobs, 'gpu' for GPU jobs).

Use '-h' to display this help message.
```

=== "CPU Nodes"

    ```bash
    $ interactive -a $PI_UCID -q standard -j cpu
    Job Type: cpu
    Starting an interactive session with the general partition and 1 core for 01:00:00 of walltime in standard priority
    srun: job 584280 queued and waiting for resources
    srun: job 584280 has been allocated resources
    ```
    
=== "GPU Nodes"

    ```bash
    $ interactive -a $PI_UCID -q standard -j gpu
    Job Type: gpu
    Starting an interactive session with the GPU partition, 1 core and 1 GPU for 01:00:00 of walltime in standard priority
    srun: job 584279 queued and waiting for resources
    srun: job 584279 has been allocated resources
    ```  
     
=== "Debug Nodes"

    ```bash
    $ interactive -a $PI_UCID -q debug -j cpu -p debug
    Job Type: cpu
    Starting an interactive session with the debug partition and 1 core for 01:00:00 of walltime in debug priority
    srun: job 584281 queued and waiting for resources
    srun: job 584281 has been allocated resources
    ```

Replace `$PI_UCID` with PI's NJIT UCID. 
Now, once you get the confirmation of job allocation, you will be assigned to a compute node.

#### Customizing Your Resources
Please note that, by default, this interactive session will request 1 core (for CPU jobs), 1 GPU (for GPU jobs), with a 1-hour walltime. To customize the resources, use the `-h` option for help. Run `interactive -h` for more details. Here is an explanation of each flag given below.

```python exec="on"
import pandas as pd 
import numpy as np
df = pd.read_csv('docs/assets/tables/interactive.csv')
df.replace(np.nan, 'NA', inplace=True)
print(df.to_markdown(index=False))
```
!!! warning

    Login nodes are not designed for running computationally intensive jobs. You can use the head node to edit and manage your files, or to run small-scale interactive jobs. The CPU usage is limited per user on the head node. Therefore, for serious computing either submit the job using `sbatch` command or start an interactive session on the compute node.

!!! note 
       
    Please note that if you are using GPUs, check whether your script is parallelized. If your script is not parallelized and only depends on GPU, then you don't need to request more cores per node. In that case, do not use `-n` while executing the `interactive` command, as the default option will request 1 CPU per GPU. It's important to keep in mind that using multiple cores on GPU nodes may result in unnecessary CPU hour charges. Additionally, implementing this practice can make service unit accounting significantly easier.