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
To specify the job, use `--account=$PI_ucid`.  You can specify `--account` as either an `sbatch` or `#SBATCH` parameter. If you don't know the UCID of PI, use`quota_info`, and you will see SLURM account you sre associated with. Check [`quota_info`](#check-quota) for details.

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

### Multi-Instance GPU (MIG)
MIG allows a single NVIDIA GPU (such as the A100) to be divided into multiple independent instances, each with dedicated compute and memory resources. This enables multiple users to share a GPU efficiently, making it ideal for smaller workloads that don’t require a full GPU.
Available MIG instance sizes include 10GB, 20GB, 40GB, 80GB, or one full GPU. 

#### Why You Should Use MIG Instances

* **Lower SU Cost for Smaller Workloads** 

    Using a smaller MIG instance (e.g., 10GB or 20GB) consumes fewer Service Units (SUs) compared to a full GPU. This helps you conserve your group’s annual SU allocation and run more jobs.

* **No Need to Reserve a Full GPU**

    If your job doesn’t need an entire GPU, you can request a MIG instance that matches your actual requirements—saving both resources and SUs.

* **Isolated Performance**

    Each MIG instance is fully isolated in terms of compute, memory, and cache. Your job won’t be impacted by other users running on the same GPU.

Please check the table below on how to request MIG in the slurm script.


| GPU MIG |          Slurm Directive           | 
|---------|:----------------------------------:|
| 10G MIG |      `--gres=gpu:a100_10g:1 `      |
| 20G MIG |      `--gres=gpu:a100_20g:1 `      |
| 40G MIG |      `--gres=gpu:a100_40g:1 `      |
| 80G MIG |        `--gres=gpu:a100:1`         |



!!! info
    
    For an 80G MIG, it is considered a full GPU. In that case, you should specify `--gres=gpu:1` in your job script. If you want to use a partial GPU, please refer to the sample [GPU job scripts](#submitting-jobs-on-gpu-nodes).

### SU charges
Since resources are limited, each faculty PI is allocated 300,000 Service Units (SUs) per year upon request at no cost. These SUs can be used via the standard [priority](#priority-use-qos) on the SLURM job scheduler. 
One SU is defined as 1 CPU hour or 4 GB of RAM per hour. 

!!! tip "Important information on SU"
    
    * The SU allocation is per PI group, not per individual student.
    * The allocation resets each fiscal year.
    * Students are expected to use SUs efficiently, as excessive usage may deplete their group's SU balance quickly.

If a group exhausts its SU allocation early, the PI has the option to purchase additional SUs or leverage higher [priority](#priority-use-qos) queues through investment. For more details, refer to the  [Wulver Policies](wulver_policies.md) and [Condo Policies](condo_policies.md).
See the table below to see SU will be charged for different partitions. 

```python exec="on"
import pandas as pd 
import numpy as np
df = pd.read_csv('docs/assets/tables/SU.csv')
# Replace NaN with 'NA'
df.replace(np.nan, 'NA', inplace=True)
print(df.to_markdown(index=False))
```

!!! warning "Memory request via job scheduler"
    
    Please note that in the above SU calculation, MAX(CPUs, RAM/4GB) — this represents the maximum of the number of CPUs requested and the memory requested divided by 4GB.

    * If you do not specify `--mem` in your SLURM job script, the job will be allocated the default 4GB of memory per core, and you will be charged based on the number of CPUs requested.
    * If you do specify `--mem` to request more memory, the SU charge will be based on the maximum of CPU count and memory/4GB.
    Requesting more memory than the default will result in higher SU charges than if you had only specified CPUs.
    
    Therefore, please be mindful of the `--mem` setting. Requesting more memory than necessary can significantly increase your SU usage.

???+ example "Example of SU Charges"

    === "`general` Partition"
        | SLURM Directive            |    SU     |      Explaination |
        |---------------------|:---------:|:---------:|
        | 4 CPUs      |  MAX(4, 4*4G/4G) = 4  |     Since no memory requireemnt is specified, SU is charged based on the same number of CPUs       |
        | 4 CPUs + `--mem=64G`      |  MAX(4, 64G/4G) = 16 |    Since 64G memory is specified, the MAX function the evaluates the maximum of 4 CPUS, and 64G/4G= 16, resulting in a charge of 16 SUs         |
        | 4 CPUs + `--mem=4G`     |  MAX(4, 4G/4G) = 4 |   MAX function the evaluates the maximum of 4 CPUS, and 4G/4G= 1, resulting in a charge of 4 SUs          |
        | 4 CPUs + `--mem-per-cpu=8G`      |  MAX(4, 8G*4/4G) = 8 |  MAX function the evaluates the maximum of 4 CPUS, and 8G*4CPUs/4G = 8 , resulting in a charge of 8 SUs           |
    
    === "`bigmem` Partition"
        | SLURM Directive             |           SU                |                                                             Explaination                             |
        |-----------------------------|:---------------------------:|:----------------------------------------------------------------------------------------------------:|
        | 4 CPUs                      | MAX(4*1.5, 4*4G/4G) = 6     |                       On `bigmem` partion the usage factor is 1.5                     |
        | 4 CPUs + `--mem=64G`        | MAX(4*1.5, 64G/4G) = 16     | Since 64G memory is specified, the MAX function the evaluates the maximum of 4*1.5= 6 SUs, and 64G/4G= 16 SUs, resulting in a charge of 16 SUs |
        | 4 CPUs + `--mem=4G`         |  MAX(4*1.5, 4G/4G) = 6      |                    MAX function the evaluates the maximum of 4*1.5= 6 SUs, and 4G/4G= 1 SU, resulting in a charge of 4 SUs                    |
        | 4 CPUs + `--mem-per-cpu=8G` |  MAX(4*1.5, 8G*4/4G) = 8    |                MAX function the evaluates the maximum of *1.5= 6 SUs, and 8G*4CPUs/4G = 8 SUs , resulting in a charge of 8 SUs                |

    === "`gpu` Partition"
        | SLURM Directive            |    SU     |      Explaination |
        |---------------------|:---------:|:---------:|
        | 4 CPUs + 10MIG     |  MAX(4, 4*4G/4G) + 16 * (10G/80G) = 6  |     Since no memory requireemnt is specified, SU is charged based on the same number of CPUs and 10G of GPU memory      |
        | 4 CPUs + 20MIG      |  MAX(4, 4G/4G) + 16 * (20G/80G) = 8 |    SU is charged based on the same number of CPUs and 20G of GPU memory         |
        | 4 CPUs + 40MIG     |  MAX(4, 4G/4G) + 16 * (40G/80G) = 12 |   SU is charged based on the same number of CPUs and 40G of GPU memory          |
        | 4 CPUs + Full GPU      |  MAX(4, 4G/4G) + 16 * (80G/80G) = 20 |  SU is charged based on the same number of CPUs and 80G of GPU (A full GPU) memory            |
        | 4 CPUs + `--mem=64G` + Full GPU      |  MAX(4, 64G/4G) + 16 * (80G/80G) = 32 |  The MAX function the evaluates the maximum of 4 SUs (from CPUs), and 64G/4G= 16 SUs (from memory). In addition, 16 SUs are charged from 80G of GPU (A full GPU) memory, bringing the total SU charge to 32 SUs  |


### Check Quota

Users can check the SUs utilization in `--qos=standard`, and space usage via `quota_info UCID` command. 
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

    === "Using 1 core"
        ```slurm
        #!/bin/bash -l
        #SBATCH --job-name=job_nme
        #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
        #SBATCH --error=%x.%j.err
        #SBATCH --partition=general
        #SBATCH --qos=standard
        #SBATCH --account=$PI_ucid # Replace $PI_ucid which the NJIT UCID of PI
        #SBATCH --nodes=1
        #SBATCH --ntasks=1
        #SBATCH --time=59:00  # D-HH:MM:SS
        #SBATCH --mem-per-cpu=4000M

        ./myexe <input/output options> # myexe is the executable in this example.
        ```
    
    === "Using multiple cores"
        ```slurm
        #!/bin/bash -l
        #SBATCH --job-name=job_nme
        #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
        #SBATCH --error=%x.%j.err
        #SBATCH --partition=general
        #SBATCH --qos=standard
        #SBATCH --account=$PI_ucid # Replace $PI_ucid which the NJIT UCID of PI
        #SBATCH --nodes=1
        #SBATCH --ntasks-per-node=8
        #SBATCH --time=59:00  # D-HH:MM:SS
        #SBATCH --mem-per-cpu=4000M

        srun ./myexe <input/output options> # myexe is the executable in this example.
        ```

    === "Using multiple threads"
        ```slurm
        #!/bin/bash -l
        #SBATCH --job-name=job_nme
        #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
        #SBATCH --error=%x.%j.err
        #SBATCH --partition=general
        #SBATCH --qos=standard
        #SBATCH --account=$PI_ucid # Replace $PI_ucid which the NJIT UCID of PI
        #SBATCH --nodes=1
        #SBATCH --ntasks-per-node=8
        #SBATCH --time=59:00  # D-HH:MM:SS
        #SBATCH --mem-per-cpu=4000M

        OMP_NUM_THREADS=$SLURM_NTASKS ./myexe <input/output options>
        ```
        Use this script, if your code relies on threads instead of cores. 

    === "Using multiple cores and threads"
        ```slurm
        #!/bin/bash -l
        #SBATCH --job-name=job_nme
        #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
        #SBATCH --error=%x.%j.err
        #SBATCH --partition=general
        #SBATCH --qos=standard
        #SBATCH --account=$PI_ucid # Replace $PI_ucid which the NJIT UCID of PI
        #SBATCH --nodes=1
        #SBATCH --ntasks=64
        #SBATCH --cpus-per-task=2
        #SBATCH --time=59:00  # D-HH:MM:SS
        #SBATCH --mem-per-cpu=4000M

        srun gmx_mpi mdrun ... -ntomp $SLURM_CPUS_PER_TASK ...
        ```
        This is the example script of [GROAMCS](gromacs.md) which uses both CPUs and threads.      
!!! warning
    
    Do not request multiple cores unless your code is parallelized. Before using multiple cores, ensure that your code is capable of parallelizing tasks; otherwise, it will unnecessarily consume service units (SUs) and may negatively impact performance. Please review the code's documentation thoroughly and use a single core if it does not support parallel execution.  

* Here, the job requests 1 node on the `general` partition with `qos=standard`. Please note that the memory relies on the number of cores you are requesting. 
* As per the policy, users can request up to 4GB memory per core, therefore the flag  `--mem-per-cpu` is used for memory requirement. If you are using 1 core and need more memory, use `--mem` instead. 
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
    
    === "Using 1 core, 1 GPU"
        ```slurm
        #!/bin/bash -l
        #SBATCH --job-name=gpu_job
        #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
        #SBATCH --error=%x.%j.err
        #SBATCH --partition=gpu
        #SBATCH --qos=standard
        #SBATCH --account=$PI_ucid # Replace $PI_ucid which the NJIT UCID of PI
        #SBATCH --nodes=1
        #SBATCH --ntasks-per-node=1
        #SBATCH --gres=gpu:1
        #SBATCH --time=59:00  # D-HH:MM:SS
        #SBATCH --mem-per-cpu=4000M

        ./myexe <input/output options> # myexe is the executable in this example.
        ```

    === "Using multiple cores, 1 GPU"
        ```slurm
        #!/bin/bash -l
        #SBATCH --job-name=gpu_job
        #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
        #SBATCH --error=%x.%j.err
        #SBATCH --partition=gpu
        #SBATCH --qos=standard
        #SBATCH --account=$PI_ucid # Replace $PI_ucid which the NJIT UCID of PI
        #SBATCH --nodes=1
        #SBATCH --ntasks-per-node=8
        #SBATCH --gres=gpu:1
        #SBATCH --time=59:00  # D-HH:MM:SS
        #SBATCH --mem-per-cpu=4000M

        srun ./myexe <input/output options> # myexe is the executable in this example.
        ```

    === "Using multiple cores, GPUs"
        ```slurm
        #!/bin/bash -l
        #SBATCH --job-name=gpu_job
        #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
        #SBATCH --error=%x.%j.err
        #SBATCH --partition=gpu
        #SBATCH --qos=standard
        #SBATCH --account=$PI_ucid # Replace $PI_ucid which the NJIT UCID of PI
        #SBATCH --nodes=1
        #SBATCH --ntasks-per-node=8
        #SBATCH --gres=gpu:2
        #SBATCH --time=59:00  # D-HH:MM:SS
        #SBATCH --mem-per-cpu=4000M

        srun ./myexe <input/output options> # myexe is the executable in this example.
        ```
    
    === "Using MIGs"
        ```slurm
        #!/bin/bash -l
        #SBATCH --job-name=gpu_job
        #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
        #SBATCH --error=%x.%j.err
        #SBATCH --partition=gpu
        #SBATCH --qos=standard
        #SBATCH --account=$PI_ucid # Replace $PI_ucid which the NJIT UCID of PI
        #SBATCH --nodes=1
        #SBATCH --ntasks-per-node=8
        #SBATCH --gres=gpu:a100_10g:1  # This uses 10G MIG, to use 20G or 40G MIG, modify 10g to 20g or 40g 
        #SBATCH --time=59:00  # D-HH:MM:SS
        #SBATCH --mem-per-cpu=4000M

        srun ./myexe <input/output options> # myexe is the executable in this example.
        ```

!!! warning

    Do not use multiple GPUs unless you are certain that your job's performance will benefit from them. Most GPU jobs do not require multiple CPUs either. Please remember that unnecessarily requesting additional resources can negatively impact job performance and will also consume more service units (SUs).  

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
    #SBATCH --account=$PI_ucid # Replace $PI_ucid which the NJIT UCID of PI
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --time=7:59:00  # D-HH:MM:SS, Maximum allowable Wall Time 8 hours
    #SBATCH --mem-per-cpu=4000M

    ./myexe <input/output options>
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
     Use `ssh` or `srun` 

     `srun ./myexe <input/output options>` 
     or
     `ssh n0103`
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
     Use `ssh` or `srun` 

     `srun ./myexe <input/output options>` 
     or
     `ssh n0048`
     
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
     Use `ssh` or `srun`.

     `srun ./myexe <input/output options>` 
     or
     `ssh n0127`

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