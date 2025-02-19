---
title: SLURM
---
Slurm (Simple Linux Utility for Resource Management) is an open-source workload manager and job scheduler designed for high-performance computing clusters. It is widely used in research, academia, and industry to efficiently manage and allocate computing resources such as CPUs, GPUs, memory, and storage for running various types of jobs and tasks. Slurm helps optimize resource utilization, minimizes job conflicts, and provides a flexible framework for distributing workloads across a cluster of machines. It offers features like job prioritization, fair sharing of resources, job dependencies, and real-time monitoring, making it an essential tool for orchestrating complex computational workflows in diverse fields.

## Availability

```python exec="on"
import pandas as pd
# Create a dictionary with data
data = {
    'Software': ['slurm'],
    'Module Load Command': ['`module load wulver`']
}
df = pd.DataFrame(data)
print(df.to_markdown(index=False))
```

Please note that the module `wulver` is already loaded when a user logs in to the cluster. If you use `module purge` command, make sure to use `module load wulver` in the slurm script to load SLURM.

## Application Information, Documentation
The documentation of SLURM is available at [SLURM manual](https://slurm.schedmd.com/documentation.html). 

### Managing and Monitoring Jobs

SLURM has numerous tools for monitoring jobs. Below are a few to get started. More documentation is available on the [SLURM website](https://slurm.schedmd.com/man_index.html).

The most common commands are: 

- List all current jobs: `squeue`
- Job deletion: `scancel [job_id]`
- Run a job: `sbatch [submit script]`
- Run a command: `srun <slurm options> <command name>`

### SLURM User Commands 

| Task                |              Command              | 
|---------------------|:---------------------------------:|
| Job submission:     |      `sbatch [script_file]`       |
| Job deletion:       |        `scancel [job_id]`         |
| Job status by job:  |         `squeue [job_id]`         |
| Job status by user: |      `squeue -u [user_name]`      |
| Job hold:           |     `scontrol hold [job_id]`      |
| Job release:        |    `scontrol release [job_id]`    |
| List enqueued jobs: |             `squeue`              |
| List nodes:         | `sinfo -N OR scontrol show nodes` |
| Cluster status:     |              `sinfo`              |
 

## Using SLURM on Wulver
In Wulver, SLURM submission will have new requirements, intended for a more fair sharing of resources without impinging on investor/owner rights to computational resources.  All jobs must now be charged to a PI-group (Principal Investigator) account.

### Account (Use `--account`)
To specify the job, use `--account=PI_ucid`.  You can specify `--account` as either an `sbatch` or `#SBATCH` parameter. If you don't know the UCID of PI, use`quota_info`, and you will see SLURM account you sre associated with. Check [`quota_info`](#check-quota) for details.

### Partition (Use `--partition`)
Wulver has three partitions, differing in GPUs or RAM available:

```python exec="on"
import pandas as pd 
import numpy as np
df = pd.read_csv('docs/assets/tables/partitions.csv')
# Replace NaN with 'NA'
df.replace(np.nan, 'NA', inplace=True)
print(df.to_markdown(index=False))
```
### Priority (Use `--qos`)
Wulver has three levels of “priority”, utilized under SLURM as Quality of Service (QoS):
```python exec="on"
import pandas as pd 
import numpy as np
from tabulate import tabulate
df = pd.read_csv('docs/assets/tables/slurm_qos.csv')
# Replace NaN with 'NA'
df.replace(np.nan, 'NA', inplace=True)
print(df.to_markdown(index=False))
```
### Check Quota

Faculty PIs are allocated 300,000 Service Units (SU) per year upon request at no cost, which can be utilized via `--qos=standard` on the SLURM job. It's important to regularly check the usage of SUs so that users can be aware of their consumption and switch to `--qos=low` to prevent exhausting all allocated SUs. Users can check their quota using the `quota_info UCID` command. 
```bash linenums="1"
[ab1234@login01 ~]$ module load wulver
[ab1234@login01 ~]$ quota_info $LOGNAME
Usage for account: xy1234
   SLURM Service Units (CPU Hours): 277557 (300000 Quota)
     User ab1234 Usage: 1703 CPU Hours (of 277557 CPU Hours)
   PROJECT Storage: 867 GB (of 2048 GB quota)
     User ab1234 Usage: 11 GB (No quota)
   SCRATCH Storage: 791 GB (of 10240 GB quota)
     User ab1234 Usage: 50 GB (No quota)
HOME Storage ab1234 Usage: 0 GB (of 50 GB quota)
```
Here, `xy1234` represents the UCID of the PI, and "SLURM Service Units (CPU Hours): 277557 (300000 Quota)" indicates that members of the PI group have already utilized 277,557 CPU hours out of the allocated 300,000 SUs, and the user `xy1234` utilized 1703 CPU Hours out of 277,557 CPU Hours. This command also displays the storage usage of directories such as `$HOME`, `/project`, and `/scratch`. Users can view both the group usage and individual usage of each storage. In the given example, the group usage from the 2TB project quota is 867 GB, with the user's usage being 11 GB out of that 867 GB. For more details file system quota, see [Wulver Filesystem](get_started_on_Wulver.md#wulver-filesystems).

### Example of slurm script
#### Submitting Jobs on CPU Nodes
??? example "Sample Job Script to use: submit.sh"

    ```slurm
    #!/bin/bash -l
    #SBATCH --job-name=job_nme
    #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
    #SBATCH --error=%x.%j.err
    #SBATCH --partition=general
    #SBATCH --qos=standard
    #SBATCH --account=PI_ucid # Replace PI_ucid which the NJIT UCID of PI
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=8
    #SBATCH --time=59:00  # D-HH:MM:SS
    #SBATCH --mem-per-cpu=4000M
    ```

* Here, the job requests 1 node with 8 cores, on the `general` partition with `qos=standard`. Please note that the memory relies on the number of cores you are requesting. 
* As per the policy, users can request up to 4GB memory per core, therefore the flag  `--mem-per-cpu` is used for memory requirement. 
* In this above script `--time` indicates the wall time which is used to specify the maximum amount of time that a job is allowed to run. The maximum allowable wall time depends on SLURM QoS, which you can find in [QoS](slurm.md#using-slurm-on-cluster). 
* To submit the job, use `sbatch submit.sh` where the `submit.sh` is the job script. Once the job has been submitted, the jobs will be in the queue, which will be executed based on priority-based scheduling. 
* To check the status of the job use `squeue -u $LOGNAME` and you should see the following 
```bash
  JOBID PARTITION     NAME     USER  ST    TIME    NODES  NODELIST(REASON)
   635   general     job_nme   ucid   R   00:02:19    1      n0088
```
Here, the `ST` stands for the status of the job. You may see the status of the job `ST` as `PD` which means the job is pending and has not been assigned yet. The status change depends upon the number of users using the partition and resources requested in the job. Once the job starts, you will see the output file with an extension of `.out`. If the job causes any errors, you can check the details of the error in the file with the `.err` extension.

#### Submitting Jobs on GPU Nodes
In case of submitting the jobs on GPU, you can use the following SLURM script 

??? example "Sample Job Script to use: gpu_submit.sh"

    ```slurm
    #!/bin/bash -l
    #SBATCH --job-name=gpu_job
    #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
    #SBATCH --error=%x.%j.err
    #SBATCH --partition=gpu
    #SBATCH --qos=standard
    #SBATCH --account=PI_ucid # Replace PI_ucid which the NJIT UCID of PI
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=8
    #SBATCH --gres=gpu:2
    #SBATCH --time=59:00  # D-HH:MM:SS
    #SBATCH --mem-per-cpu=4000M
    ```
This will request 2 GPUS per node on the `GPU` partition.

#### Submitting Jobs on `debug`
The `debug` QoS in Slurm is intended for debugging and testing jobs. It usually provides a shorter queue wait time and quicker job turnaround. Jobs submitted with the `debug` QoS have access to a limited set of resources (Only 4 CPUS on Wulver), making it suitable for rapid testing and debugging of applications without tying up cluster resources for extended periods. 

??? example "Sample Job Script to use: debug_submit.sh"

    ```slurm
    #!/bin/bash -l
    #SBATCH --job-name=debug
    #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
    #SBATCH --error=%x.%j.err
    #SBATCH --partition=debug
    #SBATCH --qos=debug
    #SBATCH --account=PI_ucid # Replace PI_ucid which the NJIT UCID of PI
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=4
    #SBATCH --time=7:59:00  # D-HH:MM:SS, Maximum allowable Wall Time 8 hours
    #SBATCH --mem-per-cpu=4000M
    ```
To submit the jobs, `sbatch` command.
### Interactive session on a compute node

 Interactive sessions are useful for tasks that require direct interaction with the compute node's resources and software environment. To start an interactive session on the compute node, use `interactive` after logging into Wulver.

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
     Starting an interactive session with the general partition and 1 core for 01:00:00 of walltime in standard priority
     salloc: Pending job allocation 466577
     salloc: job 466577 queued and waiting for resources
     salloc: job 466577 has been allocated resources
     salloc: Granted job allocation 466577
     salloc: Nodes n0103 are ready for job   
     ```
=== "GPU Nodes"

     ```bash
     $ interactive -a $PI_UCID -q standard -j gpu
     Starting an interactive session with the GPU partition, 1 core and 1 GPU for 01:00:00 of walltime in standard priority
     salloc: Pending job allocation 466579
     salloc: job 466579 queued and waiting for resources
     salloc: job 466579 has been allocated resources
     salloc: Granted job allocation 466579
     salloc: Nodes n0048 are ready for job
     ```
=== "Debug Nodes"

     ```bash
     $ interactive -a $PI_UCID -q debug -j cpu -p debug
     Starting an interactive session with the debug partition and 1 core for 01:00:00 of walltime in debug priority
     salloc: Pending job allocation 466581
     salloc: job 466581 queued and waiting for resources
     salloc: job 466581 has been allocated resources
     salloc: Granted job allocation 466581
     salloc: Waiting for resource configuration
     salloc: Nodes n0127 are ready for job
     ```

Replace `$PI_UCID` with PI's NJIT UCID. 
Now, once you get the confirmation of job allocation, you can either use `srun` or `ssh` to access the particular node allocated to the job. 

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

#### Additional Resources

- [SLURM Tutorial List](https://slurm.schedmd.com/tutorials.html)