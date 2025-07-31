## Overview

Managing and monitoring your jobs effectively helps ensure efficient use of resources and enables quicker debugging when things go wrong. Slurm provides several built-in commands to track job status, usage, and troubleshoot issues.

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
 

## `Seff` command

- The `seff` command is a handy tool to assess how efficiently your job used the requested resources **after it has completed**. 
- Using `seff` can help you adjust your future job scripts to **request only as much memory/time as truly needed**, improving scheduler fairness and reducing wasted resources.


```shell
$ seff
Usage: seff [Options] <Jobid>
       Options:
       -h    Help menu
       -v    Version
       -d    Debug mode: display raw Slurm data
```
**Example output**

```shell
$ seff 575079
Job ID: 575079
Cluster: wulver
User/Group: ls565/ls565
State: COMPLETED (exit code 0)
Cores: 1
CPU Utilized: 00:00:19
CPU Efficiency: 67.86% of 00:00:28 core-walltime
Job Wall-clock time: 00:00:28
Memory Utilized: 4.21 MB
Memory Efficiency: 0.11% of 3.91 GB
```

